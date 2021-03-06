
COLORS= {
    'black': 0,
    'red': 1,
    'green': 2,
    'yellow': 3,
    'blue': 4,
    'magenta': 5,
    'cyan': 6,
    'white': 7,
}

RESET = '\033[0m'

def makeColorCode(color = {}):
    codes = []
    if 'fg' in color:
        color_num = COLORS.get(color['fg'],None)
        if color_num is not None:
            codes.append('3%d;1' % color_num)
    if 'bg' in color:
        color_num = COLORS.get(color['bg'],None)
        if color_num is not None:
            codes.append('10%d' % color_num)
    if color.get('bold',False):
        codes.append('1')
    if color.get('underline',False):
        codes.append('4')
  
    return '\033[%sm' % ';'.join(codes) if codes else ''
    
def colorize(msg, color= {}):
    return ''.join((makeColorCode(color),msg,RESET))


#####
# we are not actually using the table below!

# See https://jonasjacek.github.io/colors/
# or other sources for list of Xterm color codes

xterm_colors_map = {
    'Black': 0,
    'Maroon': 1,
    'Green': 2,
    'Olive': 3,
    'Navy': 4,
    'Purple': 5,
    'Teal': 6,
    'Silver': 7,
    'Grey': 8,
    'Red': 9,
    'Lime': 10,
    'Yellow': 11,
    'Blue': 12,
    'Fuchsia': 13,
    'Aqua': 14,
    'White': 15,
    'Grey0': 16,
    'NavyBlue': 17,
    'DarkBlue': 18,
    'Blue3': 19,
    'Blue3': 20,
    'Blue1': 21,
    'DarkGreen': 22,
    'DeepSkyBlue4': 23,
    'DeepSkyBlue4': 24,
    'DeepSkyBlue4': 25,
    'DodgerBlue3': 26,
    'DodgerBlue2': 27,
    'Green4': 28,
    'SpringGreen4': 29,
    'Turquoise4': 30,
    'DeepSkyBlue3': 31,
    'DeepSkyBlue3': 32,
    'DodgerBlue1': 33,
    'Green3': 34,
    'SpringGreen3': 35,
    'DarkCyan': 36,
    'LightSeaGreen': 37,
    'DeepSkyBlue2': 38,
    'DeepSkyBlue1': 39,
    'Green3': 40,
    'SpringGreen3': 41,
    'SpringGreen2': 42,
    'Cyan3': 43,
    'DarkTurquoise': 44,
    'Turquoise2': 45,
    'Green1': 46,
    'SpringGreen2': 47,
    'SpringGreen1': 48,
    'MediumSpringGreen': 49,
    'Cyan2': 50,
    'Cyan1': 51,
    'DarkRed': 52,
    'DeepPink4': 53,
    'Purple4': 54,
    'Purple4': 55,
    'Purple3': 56,
    'BlueViolet': 57,
    'Orange4': 58,
    'Grey37': 59,
    'MediumPurple4': 60,
    'SlateBlue3': 61,
    'SlateBlue3': 62,
    'RoyalBlue1': 63,
    'Chartreuse4': 64,
    'DarkSeaGreen4': 65,
    'PaleTurquoise4': 66,
    'SteelBlue': 67,
    'SteelBlue3': 68,
    'CornflowerBlue': 69,
    'Chartreuse3': 70,
    'DarkSeaGreen4': 71,
    'CadetBlue': 72,
    'CadetBlue': 73,
    'SkyBlue3': 74,
    'SteelBlue1': 75,
    'Chartreuse3': 76,
    'PaleGreen3': 77,
    'SeaGreen3': 78,
    'Aquamarine3': 79,
    'MediumTurquoise': 80,
    'SteelBlue1': 81,
    'Chartreuse2': 82,
    'SeaGreen2': 83,
    'SeaGreen1': 84,
    'SeaGreen1': 85,
    'Aquamarine1': 86,
    'DarkSlateGray2': 87,
    'DarkRed': 88,
    'DeepPink4': 89,
    'DarkMagenta': 90,
    'DarkMagenta': 91,
    'DarkViolet': 92,
    'Purple': 93,
    'Orange4': 94,
    'LightPink4': 95,
    'Plum4': 96,
    'MediumPurple3': 97,
    'MediumPurple3': 98,
    'SlateBlue1': 99,
    'Yellow4': 100,
    'Wheat4': 101,
    'Grey53': 102,
    'LightSlateGrey': 103,
    'MediumPurple': 104,
    'LightSlateBlue': 105,
    'Yellow4': 106,
    'DarkOliveGreen3': 107,
    'DarkSeaGreen': 108,
    'LightSkyBlue3': 109,
    'LightSkyBlue3': 110,
    'SkyBlue2': 111,
    'Chartreuse2': 112,
    'DarkOliveGreen3': 113,
    'PaleGreen3': 114,
    'DarkSeaGreen3': 115,
    'DarkSlateGray3': 116,
    'SkyBlue1': 117,
    'Chartreuse1': 118,
    'LightGreen': 119,
    'LightGreen': 120,
    'PaleGreen1': 121,
    'Aquamarine1': 122,
    'DarkSlateGray1': 123,
    'Red3': 124,
    'DeepPink4': 125,
    'MediumVioletRed': 126,
    'Magenta3': 127,
    'DarkViolet': 128,
    'Purple': 129,
    'DarkOrange3': 130,
    'IndianRed': 131,
    'HotPink3': 132,
    'MediumOrchid3': 133,
    'MediumOrchid': 134,
    'MediumPurple2': 135,
    'DarkGoldenrod': 136,
    'LightSalmon3': 137,
    'RosyBrown': 138,
    'Grey63': 139,
    'MediumPurple2': 140,
    'MediumPurple1': 141,
    'Gold3': 142,
    'DarkKhaki': 143,
    'NavajoWhite3': 144,
    'Grey69': 145,
    'LightSteelBlue3': 146,
    'LightSteelBlue': 147,
    'Yellow3': 148,
    'DarkOliveGreen3': 149,
    'DarkSeaGreen3': 150,
    'DarkSeaGreen2': 151,
    'LightCyan3': 152,
    'LightSkyBlue1': 153,
    'GreenYellow': 154,
    'DarkOliveGreen2': 155,
    'PaleGreen1': 156,
    'DarkSeaGreen2': 157,
    'DarkSeaGreen1': 158,
    'PaleTurquoise1': 159,
    'Red3': 160,
    'DeepPink3': 161,
    'DeepPink3': 162,
    'Magenta3': 163,
    'Magenta3': 164,
    'Magenta2': 165,
    'DarkOrange3': 166,
    'IndianRed': 167,
    'HotPink3': 168,
    'HotPink2': 169,
    'Orchid': 170,
    'MediumOrchid1': 171,
    'Orange3': 172,
    'LightSalmon3': 173,
    'LightPink3': 174,
    'Pink3': 175,
    'Plum3': 176,
    'Violet': 177,
    'Gold3': 178,
    'LightGoldenrod3': 179,
    'Tan': 180,
    'MistyRose3': 181,
    'Thistle3': 182,
    'Plum2': 183,
    'Yellow3': 184,
    'Khaki3': 185,
    'LightGoldenrod2': 186,
    'LightYellow3': 187,
    'Grey84': 188,
    'LightSteelBlue1': 189,
    'Yellow2': 190,
    'DarkOliveGreen1': 191,
    'DarkOliveGreen1': 192,
    'DarkSeaGreen1': 193,
    'Honeydew2': 194,
    'LightCyan1': 195,
    'Red1': 196,
    'DeepPink2': 197,
    'DeepPink1': 198,
    'DeepPink1': 199,
    'Magenta2': 200,
    'Magenta1': 201,
    'OrangeRed1': 202,
    'IndianRed1': 203,
    'IndianRed1': 204,
    'HotPink': 205,
    'HotPink': 206,
    'MediumOrchid1': 207,
    'DarkOrange': 208,
    'Salmon1': 209,
    'LightCoral': 210,
    'PaleVioletRed1': 211,
    'Orchid2': 212,
    'Orchid1': 213,
    'Orange1': 214,
    'SandyBrown': 215,
    'LightSalmon1': 216,
    'LightPink1': 217,
    'Pink1': 218,
    'Plum1': 219,
    'Gold1': 220,
    'LightGoldenrod2': 221,
    'LightGoldenrod2': 222,
    'NavajoWhite1': 223,
    'MistyRose1': 224,
    'Thistle1': 225,
    'Yellow1': 226,
    'LightGoldenrod1': 227,
    'Khaki1': 228,
    'Wheat1': 229,
    'Cornsilk1': 230,
    'Grey100': 231,
    'Grey3': 232,
    'Grey7': 233,
    'Grey11': 234,
    'Grey15': 235,
    'Grey19': 236,
    'Grey23': 237,
    'Grey27': 238,
    'Grey30': 239,
    'Grey35': 240,
    'Grey39': 241,
    'Grey42': 242,
    'Grey46': 243,
    'Grey50': 244,
    'Grey54': 245,
    'Grey58': 246,
    'Grey62': 247,
    'Grey66': 248,
    'Grey70': 249,
    'Grey74': 250,
    'Grey78': 251,
    'Grey82': 252,
    'Grey85': 253,
    'Grey89': 254,
    'Grey93': 255,
}

def makeColorCode256(color = {}):
    codes = []
    if 'fg' in color:
        color_num = xterm_colors_map.get(color['fg'],None)
        if color_num is not None:
            codes.append('38;5;%d' % color_num)
    if 'bg' in color:
        color_num = xterm_colors_map.get(color['bg'],None)
        if color_num is not None:
            codes.append('48;5;%d' % color_num)
    if color.get('bold',False):
        codes.append('1')
    if color.get('underline',False):
        codes.append('4')
  
    return '\033[%sm' % ';'.join(codes) if codes else ''
    
def colorize256(msg, color= {}):
    return ''.join((makeColorCode256(color),msg,RESET))


def clear_screen():
    return '\033[2J\033[H'

if __name__ == '__main__':
    print(''.join((colorize('hello',{'fg':'red', 'bold':True}),
                   colorize('world',{'fg':'blue','underline':True})
                  )))


    print(''.join((colorize256('hello',{'fg':'Thistle1', 'bold':True}),
                   colorize256('world',{'fg':'MistyRose1','underline':True})
                  )))




