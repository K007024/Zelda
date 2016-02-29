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

from gooey import Gooey, GooeyParser

import os, shutil, re
import glob

def trier(srcDir, regex):

    # convert string to pattern
    pattern = re.compile(regex, re.VERBOSE)
    
    # get all files in correct raw directory
    fichiers = glob.glob("{}/???/*.*".format(srcDir))

    # main loop
    for f in fichiers:
    
        # get name/pod/dir according to path
        f_rep, f_name = os.path.split(f)
        podnumber = f_rep[-3::]
        
        # apply regex in order to get elements
        mo = pattern.search(f_name)
        
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

@Gooey
def main():
    
    parser = GooeyParser(description='Zelda clean this mess\nReorganize date/pod -> pod/date')
    parser.add_argument('pattern', nargs='?', default=r"""(.*)_(.*)_(.*)_(.*)_(.*)_(.*)-(.{8})-(.*).datx_(.*)""",
        help="pattern which allow to get groups\nmoteur = mo.group(1)\nuseless = mo.group(2)\nbanc = mo.group(3)\npod = mo.group(4)\nuseless = mo.group(5)\nrun = mo.group(6)\ndate = mo.group(7)\nheure = mo.group(8)")
    parser.add_argument('srcDir', nargs='?', default=os.getcwd(), widget='FileChooser', 
        help='Engine directory : root/???/*.*')	
    
    args = parser.parse_args()
    trier(args.srcDir, args.pattern)
		
if __name__ == '__main__':
	main()
