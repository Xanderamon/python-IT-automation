#!/usr/bin/env python3

import os

src = os.path.join(os.getcwd(), "src")

def printlist(list):
    for x in list:
        print(x)

def get_pathlist(path):
    pathlist = []
    filelist = []
    # pathlist = []
    for root, dirs, files in os.walk(path, topdown=True):
        for d in dirs:
            pathlist.append(os.path.join(root, d))
            # pathlist[0].append(os.path.join(root, d))
        for f in files:
            filelist.append(os.path.join(root, f))
            # pathlist[1].append(os.path.join(root, f))
    # printlist(pathlist)
    # printlist(filelist)
    pathlist += filelist
    return pathlist

def main():
    printlist(get_pathlist(src))

if __name__ == "__main__":
    main()
