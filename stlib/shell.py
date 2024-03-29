import subprocess, re, os, functools
from . import util

def shellReturnOutput(what, cwd=None):
   rv = subprocess.run(what, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, cwd=cwd)
   return rv.stdout.decode('utf-8').rstrip()

def shellShowOutput(name, cmd, newenv = {}, cwd=None, show_name = True):
    env = os.environ.copy()
    for vn in newenv:
        env[vn] = newenv[vn]

    use_shell = False
    if isinstance(cmd,str):
        use_shell=True

    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         env=env, universal_newlines=True,shell=use_shell,cwd=cwd)
    for line in p.stdout:
        if show_name:
            print('{:<7}: {}'.format(name,line.rstrip()))
        else:
            print(line.rstrip())
    p.wait()
    return p

def shellDetach(what):
    cmd = what[0]
    if cmd is not None:
        os.execvp(cmd,what)

@functools.lru_cache
def repoinfo():
    root = shellReturnOutput('git rev-parse --show-toplevel')
    if root is None or re.match(r'fatal',root):
        return None

    url = shellReturnOutput('git config --get remote.origin.url')
    if url is None or re.match(r'fatal',url):
        util.die('Not in a git repo?')

    # get canonical name of repo
    repo_url = shellReturnOutput('git remote get-url origin')
    repo = os.path.splitext(os.path.basename(repo_url))[0]

    branch = shellReturnOutput('git rev-parse --abbrev-ref HEAD')
    commit = shellReturnOutput('git rev-parse HEAD')
    return {
        'root': root, 'url': url, 'name':repo, 'branch':branch, 'commit': commit
    }

