import os

print("Songdesc Generator 1.0 by jdaxey")
print("This tool works on PS4 PS3 WII WIIU Switch X1 Xbox series S and X")
print("")
print("")
print("For what verion of just dance you want to create the songdesc?")
print("")
print("[1] Just Dance 2017")
print("[2] Just Dance 2018")
print("[3] Just Dance 2019")
print("[4] Just Dance 2020")
print("[5] Just Dance 2021")
print("[6] Just Dance 2022")
print("")
print("")
print("[7] Clean the output folders")

jdver = input("Type here!:\n")
print(f'You chose option {jdver}')

if jdver == "1":
    os.system("python Gen17.py")

if jdver == "2":
    os.system("python Gen18.py")
    
if jdver == "3":
    os.system("python Gen19.py")

if jdver == "4":
    os.system("python Gen20.py")

if jdver == "5":
    os.system("python Gen21.py")

if jdver == "6":
    os.system("python Gen22.py")
    
if jdver == "7":
    os.system("python outcleaner.py")