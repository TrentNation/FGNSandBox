#Import os Library
import os

# Source file path
def link_directory(src, dst):
    os.link(src, dst)
    return

