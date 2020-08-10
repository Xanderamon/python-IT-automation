#!/usr/bin/env python3

import os
import multiprocessing
import subprocess

#In this test /src/ and /dest/ are in the same folder of the script
source = os.path.join(os.getcwd(),"src")
destination = os.path.join(os.getcwd(),"dest")

def get_pathlist(folder):
    pathlist = []
    #No need for the FULL path of the dir/file
    #The source directory is in a global variable
    for root,dirs,files in os.walk(folder):
        for f in files:
            #Extract the sub-folder (if any)
            path = root[len(folder):]
            #Extract the filename
            item = f
            #Store the RELATIVE path in a tuple
            pathlist.append((path,item))
        for d in dirs:
            #Extract the sub-folder (if any)
            path = root[len(folder):]
            #Extract the folder name
            item = d
            #Store the RELATIVE path in a tuple
            pathlist.append((path,item))
    #Return the list of tuples
    return pathlist

def backup(path):
    #Source = root, path[0] = sub-folder, path[1] = file/dir name
    #NB: We input the FULL path of the source file/folder
    src = os.path.join(source,path[0],path[1])
    #Destination = root, path[0] = sub-folder
    #NB: We input the destination folder only (no need for the file/folder name)
    dest = os.path.join(destination,path[0])
    subprocess.call(['rsync', '-azq', src, dest])

if __name__ == "__main__":
    src_pathlist = get_pathlist(source)

    with multiprocessing.Pool(len(src_pathlist),maxtasksperchild=1) as mpool:
        mpool.map(backup,src_pathlist)
