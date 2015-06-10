import sys
import os
import shutil

gDrawableFolders=['drawable', 'drawable-ldpi', 'drawable-mdpi',
                 'drawable-hdpi', 'drawable-xhdpi', 'drawable-xxhdpi',
                 'drawable-xxxhdpi']

class Tosser:
    """
    An object that can traverse a path of resource files and move them to a
    previously determined Android project location.
    """

    def __init__(self, aSourcePath, aDestPath):
        """
        Construct a new Tosser object with a source path and a
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
        in this Tosser's source directory to the correct resource
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

                files = [f for f in os.listdir(absSubPath)]

                for nextFile in files:
                    if not os.path.isdir(nextFile):
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
