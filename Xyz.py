#coding=utf-8
import os, sys, platform
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('OLDCRACK.so'):
        os.system('curl -L https://github.com/younis-dgk/old_crack_facebook/blob/main/OLDCRACK.cpython-311.so') 
        import OLDCRACK
    else:
        import OLDCRACK
 
elif bit == '32bit':
    exit()
 
