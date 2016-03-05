# coding: utf-8

from gooey import Gooey, GooeyParser

import Zelda
import sys
import os


@Gooey
def main():
    parser = GooeyParser(description='Zelda clean this mess\nReorganize date/pod -> pod/date')
    parser.add_argument('pattern', nargs='?', default=r"""(.*)_(.*)_(.*)_(.*)_(.*)_(.*)-(.{8})-(.*).datx_(.*)""",
                        help="pattern which allow to get groups\nmoteur = mo.group(1)\nuseless = mo.group(2)\nbanc = mo.group(3)\npod = mo.group(4)\nuseless = mo.group(5)\nrun = mo.group(6)\ndate = mo.group(7)\nheure = mo.group(8)")
    parser.add_argument('srcDir', nargs='?', default=os.getcwd(), widget='FileChooser',
                        help='Engine directory : root/???/*.*')

    args = parser.parse_args()
    Zelda.trier(args.srcDir, args.pattern)


if __name__ == '__main__':
    nonbuffered_stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    sys.stdout = nonbuffered_stdout
    main()
