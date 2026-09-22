import sys, os, glob, re
from pathlib import PurePath

from . import shell

def die(msg):
    print('-Error- {}'.format(msg))
    sys.exit(-1)

def getSpecifierList(config, repo):
    usage = []

    def makeName(t, config):
        is_default = isinstance(config,dict) and config.get('default',False)
        asterisk = '(*)' if is_default else ''
        return f'-{t}{asterisk}'

    categories = {
        'type': config['code_file_types'],
        'path': config['code_search_paths'][repo],
        'editor':config['editor']['editors']
    }
    for group in categories:
        c = categories[group]
        names = ', '.join(sorted([ makeName(t,c[t]) for t in c ]))
        usage.append(f'{group:6} specifiers: {names}')

    return usage

def fileGlob(paths, types, fpats=None):
    """Walk each scope once, pruning exclusions before collecting matches.

    Do not descend into directory symlinks discovered inside a scope. An
    explicitly selected root may itself be a symlink. Ordinary file symlinks
    remain searchable. Hidden directories retain glob's default exclusion;
    hidden files require an explicitly dotted pattern.
    """
    patterns = []
    for kind in types:
        if fpats is None:
            patterns.append('*.{}'.format(kind['suffix']))
            patterns.extend(kind.get('grep_extra_glob', []))
        else:
            patterns.extend('*{}*.{}'.format(pat, kind['suffix'])
                            for pat in fpats)

    found = {}
    for scope in paths:
        exclude = re.compile(scope['exclude']) if scope.get('exclude') else None

        def excluded(path, directory=False):
            return exclude is not None and (
                exclude.search(path) or
                (directory and exclude.search(path + os.sep)))

        # Preserve wildcard include roots, but never recursively glob the tree.
        for root in glob.glob(scope['include']):
            root = os.path.normpath(root)
            if excluded(root, directory=True):
                continue
            for directory, dirs, files in os.walk(root, followlinks=False):
                dirs[:] = sorted(name for name in dirs
                                 if not name.startswith('.')
                                 and not os.path.islink(os.path.join(directory, name))
                                 and not excluded(os.path.join(directory, name), True))
                for name in sorted(files):
                    path = os.path.join(directory, name)
                    if excluded(path):
                        continue
                    relative = PurePath(os.path.relpath(path, root))
                    if any(relative.match(pattern)
                           and (not name.startswith('.') or
                                PurePath(pattern).name.startswith('.'))
                           for pattern in patterns):
                        found[path] = None
    return list(found)


def makeTypeList(config, adict):
    ftypes = []
    for n in config['code_file_types']:
        if n in adict:
           ftypes.append(n)
    if not len(ftypes):
        ftypes = list(filter(lambda x: config['code_file_types'][x]['default'], config['code_file_types']))

    return [ {'suffix':n, 'grep_extra_glob':config['code_file_types'][n].get('grep_extra_glob',[])} for n in ftypes ]


def makeSearchPathList(config, adict):
    pnames = []
    repoinfo = adict['repoinfo']
    if repoinfo is None:
        die('need to be inside a git repo')
    reponame = repoinfo['name']
    if reponame not in config['code_search_paths']:
        die(f'Repo "{reponame}" is not in config file.')

    possibles = list(config['code_search_paths'][reponame].keys())
    for n in possibles:
        if n in adict:
            pnames.append(n)

    if not len(pnames):
        pnames = list(filter(lambda x: config['code_search_paths'][reponame][x]['default'], possibles));
    
    root = repoinfo['root']
    paths = []
    for x in pnames:
        for y in config['code_search_paths'][reponame][x].get('include'):
            npath = os.path.join(root,y)
            paths.append({ 'include': npath, 'exclude': config['code_search_paths'][reponame][x].get('exclude') })
    return paths


def editFiles(config, adict, found):
    count_ok = len(found) and len(found) < config['editor']['max_files']
    edit_req = None 
    for en in config['editor']['editors']:
        if en in adict:
            edit_req = en 
            break

    if edit_req:
        if count_ok:
            shell.shellDetach(config['editor']['editors'][edit_req] + found)
        else:
            print("\n{} is too many files to edit".format(len(found)))
