import pkg_resources
import argparse
import sys
import os
import shutil

gDrawableFolders=['drawable', 'drawable-ldpi', 'drawable-mdpi',
                 'drawable-hdpi', 'drawable-xhdpi', 'drawable-xxhdpi',
                 'drawable-xxxhdpi']

class DrawableTosser:
    """
    An object that can traverse a path of resource files and move them to a
    previously determined Android project location.
    """

    def __init__(self, aSourcePath, aDestPath):
        """
        Construct a new DrawableTosser object with a source path and a
        destination path.

        @param aSourcePath The path to the set of drawable* folders which should
               be copied into the given project path
        @param aDestPath The path to the top-most level of an Android project
               with a res/ directory somewhere underneath it
        """
        self.mSourcePath = os.path.abspath(aSourcePath)
        self.mDestPath = os.path.abspath(aDestPath)

    def tossDrawables(self):
        """
        'Toss' (i.e. move) drawable files from the hierarchy of drawable files
        in this DrawableTosser's source directory to the correct resource
        hierarchy within the Android project directory specified for this object.
        """
        global gDrawableFolders
        resourcePath = self._findResourcePath(self.mDestPath)
        if not resourcePath:
            raise OSError('Resource directory not found in project path: '
                          + self.mDestPath)

        for nextSubPath in gDrawableFolders:
            absSubPath = os.path.join(self.mSourcePath, nextSubPath)
            if os.path.exists(absSubPath):
                # Move all files in each of these absSubPath directories to
                # their counterparts in the project resource directory
                fullResourceSubPath = os.path.join(resourcePath, nextSubPath)

                if not os.path.exists(fullResourceSubPath):
                    os.mkdir(fullResourceSubPath)

                files = [f for f in os.listdir(absSubPath) if os.path.isfile(f)]

                for nextFile in files:
                    fileToMove = os.path.abspath(os.path.join(absSubPath, nextFile))
                    shutil.copyfile(fileToMove, os.path.join(fullResourceSubPath, nextFile))

    def _findResourcePath(self, aPath):
        """
        Find the res/ directory beneath a given Android project path.

        @param aPath The path beneath which to search for a resource directory

        @return The absolute path of the resource directory beneath the given
                path, if it exists; None, otherwise.
        """
        for root, dirs, files in os.walk(aPath):
            # Skip generated directories
            if 'build' in root:
                continue

            if 'AndroidManifest.xml' in files:
                # Our resource folder should be one level up, in res/
                return os.path.abspath(os.path.join(root, '../res'))

        return None

def createParser():
    """
    Create an ArgumentParser object for use within the main method of this
    program for command-line use of this script.
    """
    version = pkg_resources.require('drawabletosser')[0].version
    parser = argparse.ArgumentParser(prog='drawabletosser', description='''
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
    construct a new DrawableTosser object from these arguments, and use the
    DrawableTosser.tossDrawables() method to move drawable files from one
    location in the file system to another.
    """
    parser = createParser()
    parsedArgs = parser.parse_args(sys.argv[1:])

    if not parsedArgs.appPath:
        parser.print_help()

    tosser = DrawableTosser(parsedArgs.srcPath, parsedArgs.appPath)
    tosser.tossDrawables()

if __name__ == '__main__':
    exit(main())
