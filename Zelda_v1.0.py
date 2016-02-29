# coding: utf-8

"""
---------------------------------------
   Princess Zelda, clean this mess !
---------------------------------------

Usage:
    1) Edit Zelda in order to configure it
    2) Update sourcDir and regex
    3) in shell : python Zelda.py

---------------------------------------
Zelda is used to sort pod/dates the pod's mess
"""

import os, shutil, re
import glob

def trier(srcDir, myPattern):

    # get all files in correct raw directory
    fichiers = glob.glob("{}/???/*.*".format(srcDir))

    # main loop
    for f in fichiers:
    
        # get name/pod/dir according to path
        f_rep, f_name = os.path.split(f)
        podnumber = f_rep[-3::]
        
        # apply regex in order to get elements
        mo = myPattern.search(f_name)
        
        # if regex is KO abandon
        if mo == None:
            continue
        else:
            moteur = mo.group(1)
            useless = mo.group(2) 
            banc = mo.group(3)
            pod = mo.group(4)
            useless = mo.group(5)
            run = mo.group(6)
            date = mo.group(7)
            heure = mo.group(8)
            
            if date == None:
                continue
            else :
                # build path for destination directory
                dstDir = os.path.join(srcDir, date, 'pod{}'.format(podnumber))
                # make directory if necessary
                if not os.path.exists(dstDir):
                    os.makedirs(dstDir)
               
                srcPath = f
                # srcPath = os.path.join(srcDir, f_name)
                dstPath = os.path.join(dstDir, f_name)
                
                print 'from {}\nto   {}\n'.format(srcPath, dstPath)
                # move file from src to dst
                shutil.move(srcPath, dstPath)

if __name__ == '__main__':

    srcDir =  os.getcwd()
    myPattern = re.compile(r"""(.*)_(.*)_(.*)_(.*)_(.*)_(.*)-(.{8})-(.*).datx_(.*)""", re.VERBOSE)
    
    trier(srcDir, myPattern)