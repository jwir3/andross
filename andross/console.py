import argparse
import pkg_resources
import sys
from tosser import Tosser

def createParser():
    """
    Create an ArgumentParser object for use within the main method of this
    program for command-line use of this script.
    """
    version = pkg_resources.require('andross')[0].version
    parser = argparse.ArgumentParser(prog='andross', description='''
    Move drawable resources already organized into a hierarchy into the
    resources folder for a given android application
    ''', add_help=True)
    parser.add_argument('-v', '--version', help='display the version information for %(prog)s', action='version', version='%(prog)s version ' + str(version))
    parser.add_argument('-s', '--source', dest='srcPath', metavar='<source path>', default='.', help='path containing the drawable resources to be moved', action='store')
    parser.add_argument('appPath', metavar='<app path>', help='path to the android application where the drawable resources should be added', action='store')
    return parser

def printVersion():
    """
    Use the ArgumentParser object created as part of createParser() to print the
    version information about this program.
    """
    parser = createParser()
    parser.parse_args(['--version'])

def main():
    """
    Parse arguments passed on the command line using an ArgumentParser,
    construct a new Tosser object from these arguments, and use the
    Tosser.tossDrawables() method to move drawable files from one
    location in the file system to another.
    """
    parser = createParser()
    parsedArgs = parser.parse_args(sys.argv[1:])

    if not parsedArgs.appPath:
        parser.print_help()

    tosser = Tosser(parsedArgs.srcPath, parsedArgs.appPath)
    tosser.tossDrawables()

if __name__ == '__main__':
    exit(main())
