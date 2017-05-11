# this code given directory it will search all the directory and subdirectory
import os
import sys


def recurse_dir(path_directory, recurse_depth = 0):
    if recurse_depth< 1:
      print("Parent_directory:",path_directory)
    for files in os.listdir(path_directory):
        path = os.path.join(path_directory,files)
        direcrry_exist = os.path.isdir(path)
        if not direcrry_exist:
            print("\t"* recurse_depth, files)
            
        else:
            print("\t"*recurse_depth + "directory level {}:".format(recurse_depth), files)
            recurse_dir(path,recurse_depth = recurse_depth + 1)

            
recurse_dir(sys.argv[1])

