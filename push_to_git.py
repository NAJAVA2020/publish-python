#!/usr/bin/env python
"""
This script is used to push the changes to the git repository in CSV format.
"""
import os
import secrets
import time


def push_to_git():
    """
    This function is used to push the changes to the git repository.
    """
    os.system("git add .")
    random_string = secrets.token_hex(16)
    os.system("git commit -m '{random_string}'")

    # Assuming the branch is 'main', change if necessary
    os.system("git push origin main")
    print("[INFO] --- Pushed the changes to the git repository. ---")


if __name__ == "__main__":
    while True:
        push_to_git()
        time.sleep(10)