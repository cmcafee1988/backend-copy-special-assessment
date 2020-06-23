#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "Study hall"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    # get list of files in directory (imports)
    os.listdir(dirname)
    paths = os.listdir(dirname)
    print(paths)


    # identify "special" file --"_w_"
    special_paths = []
    for filename in paths:
        match = re.findall(r'__(\w+)__', filename)
        if match:
            special_paths.append(os.path.abspath(
                os.path.join(dirname, filename)))
    print(special_paths)
    return special_paths
    # return absolute paths to special files


    #return
    #parser.add_argument('--tozip', help='dest zipfile for special files')


def copy_to(path_list, dest_dir):
    """Copy files into destination directory"""
    # your code here
    return


def zip_to(path_list, dest_zip):
    """Copy files into destination zip"""
    # your code here
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='directory where special paths is located')

    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        exit(1)
    special_paths = get_special_paths(ns.from_dir)



    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    if ns.todir:
        copy_to(special_paths, ns.todir)
    
    if ns.tozip:
        zip_to(special_paths, ns.tozip)

    if not ns.todir and ns.tozip:
        print('\n'.join(special_paths))

if __name__ == "__main__":
    print(sys.argv)
    main(sys.argv[1:])

