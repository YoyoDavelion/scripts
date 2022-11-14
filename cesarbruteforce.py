# Author David Moreno
# Github https://github.com/YoyoDavelion
# Developed 14-11-2022
import os, sys
replace_numbers = False
def code(text, key, mode):
        #text = input("Text here: ")
        #key = int(input("Number of key: "))
        #mode = ""
       # while mode != "1" and mode != "2":
        #        mode = input("Select alphabet: [1: Spanish] [2: English] : ")
        numbers = "0123456789"
        if mode == 1:
                abc_l = "abcdefghijklmnñopqrstuvwxyz"
                abc_u = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        else:
                abc_l = "abcdefghijklmnopqrstuvwxyz"
                abc_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        decoded = ""
        for character in text:
                if character in abc_l:
                        if abc_l.index(character) + key < len(abc_l):
                                decoded += abc_l[(abc_l.index(character) + key)]
                        else:
                              decoded += abc_l[(abc_l.index(character) + key) - len(abc_l)]
                elif character in abc_u:
                        if abc_u.index(character) + key < len(abc_u):
                                decoded += abc_u[(abc_u.index(character) + key)]
                        else:
                                decoded += abc_u[(abc_u.index(character) + key) - len(abc_u)]
                elif character in numbers and replace_numbers:
                        if int(character) + key < len(abc_u):
                                decoded += abc_u[int(character) + key]
                        else:
                                decoded += abc_u[(int(character) + key) - len(abc_u)]
                else:
                        decoded += character
        print(decoded)
        os.system('echo Key: {} >> results.txt' .format(key))
        os.system('echo {} >> results.txt'.format(decoded.strip('\n')))
def bruteforce(text):
    modes = [0, 27, 26]
    lenguages = ["", "Spanish", "English"]
    for i in range (1,len(modes)):
        print("\nBruteforce with " + lenguages[i] + " alphabet.\n")
        os.system('echo ---------------------------- >> results.txt')
        os.system('echo {} alphabet: >> results.txt' .format(lenguages[i]))
        for key in range(modes[i]):
            print("Key number {}".format(key))
            code(text, key, i)
def fileforce(file):
    file = open(file, 'r', encoding='UTF-8')
    for line in file:
        bruteforce(line)

def decodefile(file, key, mode):
    file = open(file, 'r', encoding='UTF-8')
    for line in file:
        code(line, key, mode)
if len(sys.argv) < 2:
        print("Usage: python3" + sys.argv[0] + " <file> [options]")
        print("Options: [-n](replace numbers, ignore by default. Ex: 0->A; 1->B)")
else:
        os.system('rm results.txt || del results.txt')
        if "-n" in sys.argv:
                replace_numbers = True
                fileforce(sys.argv[1])
                print("Results exported to results.txt")
        else:
                fileforce(sys.argv[1])
                print("Results exported to results.txt")
                