#!/usr/bin/env python3

import os
import multiprocessing
import subprocess

src = os.path.join(os.getcwd(), "src")
dest = os.path.join(os.getcwd(), "dest")

def printlist(l):
    for item in l:
        print(item)
        print("---------------------------------------")


def get_pathlist(source):
    pathlist = []
    for root, dirs, files in os.walk(source, topdown=True):
        # pathlist.append(root)
        for d in dirs:
            # pathlist.append(str(os.path.join(root,d))[len(source):])
            pathlist.append(str(os.path.join(root,d)))
        for f in files:
            # pathlist.append(str(os.path.join(root,f))[len(source):])
            pathlist.append(str(os.path.join(root,f)))
    return pathlist

def get_pathlists(source):
    dirlist = []
    filelist = []
    for root, dirs, files in os.walk(source, topdown=True):
        # pathlist.append(root)
        for d in dirs:
            dirlist.append(str(os.path.join(root,d))[len(source):])
        for f in files:
            filelist.append(str(os.path.join(root,f))[len(source):])
    return dirlist,filelist

def backup(path):
    print("Processing " + path)
    # source = os.path.join(src,path)
    source = path
    # destination = os.path.join(dest,path)
    destination = dest
    subprocess.call(['rsync', '-apqz', source, destination])

def rsync(path):
    print("RSYNCing... " + path)
    source = path
    destination = dest
    subprocess.call(['rsync', '-apqz', source, destination])

def back_folders(path):
    print("From path: " + src)
    source = os.path.join(src,path)
    print("Processing DIR: " + os.path.join(source,path))
    destination = os.path.join(dest,path)
    print("...to: " + destination)
    subprocess.call(['rsync', '-q', source, destination])

def back_files(path):
    print("Processing FILE: " + path)
    source = os.path.join(src,path)
    destination = os.path.join(dest,path)
    subprocess.call(['rsync', '-apqz', source, destination])


if __name__ == "__main__":
    # os.mkdir(dest)
    src_pathlist = get_pathlist(src)
    dirlist,filelist = get_pathlists(src)
    printlist(src_pathlist)

    # subprocess.call(['rsync','-av -f"+ */" -f"- *"',src,dest ])
    with multiprocessing.Pool(len(dirlist),maxtasksperchild=1) as pool:
    #     pool.map(rsync,[src,])
        pool.map(back_folders,dirlist)
    # with multiprocessing.Pool(len(filelist),maxtasksperchild=1) as pool:
        # pool.map(back_files,filelist)
        # pool.map(backup,src_pathlist)
    print("#######################################")

    dest_pathlist = get_pathlist(dest)
    printlist = dest_pathlist
    if dest_pathlist == src_pathlist:
        print("!!SUCCESS!!")
    else:
        print("...not yet :(")
