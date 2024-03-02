#!/usr/bin/env python
"""
This script is used to push the changes to the git repository in CSV format.
"""
import os
import time


def push_to_git():
    """
    This function is used to push the changes to the git repository.
    """
    os.system("git add .")
    os.system(f"git commit -m 'Updated the files at {time.ctime()}'")
    os.system("git push origin master")
    print("[INFO] --- Pushed the changes to the git repository. ---")
