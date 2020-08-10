#!/usr/bin/env python3

import os
import sys
import random
import subprocess

verbose = True
input_dirname = ''
input_dirnum = 3
input_dirdepth = 0

def verb(message): #DeBug-Printer
    if verbose:
        print(message)

def get_inputs():
    global input_dirname
    global input_dirnum
    global input_dirdepth
    try:
        input_dirname = sys.argv[1]
    except IndexError:
        while input_dirname == '':
            input_dirname = input("Please insert the Directories base name: ")
    try:
        input_dirnum = int( sys.argv[2] )
    except IndexError:
        input_dirnum = int( input("Please insert the number of desired Directories per depth level: ") )
    try:
        input_dirdepth = int( sys.argv[3] )
    except IndexError:
        input_dirdepth = int( input("Please insert the number of the desired depth level: ") )

def make_dir(dirname, dirnum, dirdepth, filechanche):
    dirs_made = []
    filecounter = 0
    for depth in range(0,(dirdepth+1)*dirnum):
        dirpath = os.getcwd() + '/'
        for n in range(0,dirnum):
            dir_namepath = dirpath + dirname + str(n+1)
            verb("Making Directory " + dir_namepath)
            os.mkdir(dir_namepath)
            if perchanche(filechanche):
                filename = 'file'+str(random.randint(1,101))+'.txt'
                verb("Making File " + filename)
                subprocess.run(['touch',filename])
                filecounter += 1
            dirs_made.append(dir_namepath)
        os.chdir(dirs_made[depth])
    verb("Made " + str(filecounter) + " files.")

def perchanche(percentage):
#  verb("We have " + str(percentage) + "% rate of success")
  chanche = random.randint(1,101)
#  verb("Randint(1,101) = " + str(chanche))
  if chanche  <= percentage:
    return True
  return False

if __name__ == '__main__':
    get_inputs()
    make_dir(input_dirname, input_dirnum, input_dirdepth, 65)
