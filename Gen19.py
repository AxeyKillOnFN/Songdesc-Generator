import os
import sys
import fileinput
import shutil

try:
    os.mkdir("output19")
    print('Output folder created succesfully!')

except:
    pass
print('Songdesc Generator for Just Dance 2019 by jdaxey!')
print('Working please wait...')
print('')
print('')
f= open("songdesc.txt","w+")
f.write('\n')
f.writelines('\n')
lines = ['{', '    "COMPONENTS": [{', '            "Artist": "Sample",', '            "CountInProgression": 1,', '            "Credits": "Sample Credits",', '            "DancerName": "Unknown Dancer",', '            "DefaultColors": {', '                "lyrics": [1.0, 1.0, 1.0, 0.035296],', '                "theme": [1, 1, 1, 1]', '            },', '            "Difficulty": 1,', '            "JDVersion":2019,', '            "LocaleID": 4294967295,', '            "LyricsType": 0,', '            "MainCoach": -1,', '            "MapName": "Sample",', '            "MojoValue": 0,', '            "NumCoach": 1,', '            "OriginalJDVersion": 2019,', '            "PhoneImages": {', '                "coach1": "world/maps/sample/menuart/textures/sample_coach_1_phone.png",', '                "cover": "world/maps/sample/menuart/textures/sample_cover_phone.jpg"', '            },', '            "Status": 3,', '            "SweatDifficulty": 1,', '            "Tags": ["main"],', '            "Title": "Sample",', '            "VideoPreviewPath": "",', '            "__class": "JD_SongDescTemplate",', '            "backgroundType": 0', '        }', '    ],', '    "FORCEISENVIRONMENT": 0,', '    "LOWUPDATE": 0,', '    "PROCEDURAL": 0,', '    "STARTPAUSED": 0,', '    "UPDATE_LAYER": 0,', '    "WIP": 0,', '    "__class": "Actor_Template"', '}']
with open('songdesc.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

old_file = r"songdesc.txt"
new_file = r"songdesc.tpl.ckd"

os.rename(old_file, new_file)
shutil.move("songdesc.tpl.ckd", "output19/songdesc.tpl.ckd") 
input('Done! Press ENTER to exit and have fun modding!')



