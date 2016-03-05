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

import glob
import os
import re
import shutil
from argparse import ArgumentParser


def trier(srcdir, regex):
    # convert string to pattern
    pattern = re.compile(regex, re.VERBOSE)

    # get all files in correct raw directory
    fichiers = glob.glob("{}/???/*.*".format(srcdir))

    # main loop
    for f in fichiers:

        # get name/pod/dir according to path
        f_rep, f_name = os.path.split(f)
        podnumber = f_rep[-3::]

        # apply regex in order to get elements
        mo = pattern.search(f_name)

        # if regex is KO abandon
        if mo is None:
            continue
        else:
            # moteur = mo.group(1)
            # useless = mo.group(2)
            # banc = mo.group(3)
            # pod = mo.group(4)
            # useless = mo.group(5)
            # run = mo.group(6)
            date = mo.group(7)
            # heure = mo.group(8)

            if date is None:
                continue
            else:
                # build path for destination directory
                dstdir = os.path.join(srcdir, date, 'pod{}'.format(podnumber))
                # make directory if necessary
                if not os.path.exists(dstdir):
                    os.makedirs(dstdir)

                srcpath = f
                # srcPath = os.path.join(srcDir, f_name)
                dstpath = os.path.join(dstdir, f_name)

                print 'from {}\nto   {}\n'.format(srcpath, dstpath)
                # move file from src to dst
                shutil.move(srcpath, dstpath)
    print('job done')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('pattern', nargs='?', default=r"""(.*)_(.*)_(.*)_(.*)_(.*)_(.*)-(.{8})-(.*).datx_(.*)""")
    parser.add_argument('srcDir', nargs='?', default=os.getcwd())

    args = parser.parse_args()

    trier(args.srcDir, args.pattern)
