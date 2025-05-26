#!/usr/bin/env python3
'''Lab 3 part 2 using subprocess'''
# Author ID: kadhikari9

import subprocess

def free_space():
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", 
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE, 
                         stdin=subprocess.PIPE, 
                         shell=True)
    output = p.communicate()
    return output[0].decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
