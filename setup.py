from setuptools import setup
import os
import os.path

progName = 'andross'
progVersion = '0.1.0'
progDescription = 'A tool for moving drawable resources into the correct directories for an Android application'
progAuthor = 'Scott Johnson'
progEmail = 'jaywir3@gmail.com'
progUrl = 'http://github.com/jwir3/andross'
entryPoints = {
  'console_scripts': [ 'andross = andross.console:main' ]
}

requirements = [
]

curDir = os.path.dirname(os.path.realpath(__file__))

setup(name=progName,
      version=progVersion,
      description=progDescription,
      author=progAuthor,
      author_email=progEmail,
      url=progUrl,
      packages=['andross'],
      entry_points=entryPoints,
    #   test_suite='tests',
      license='Mozilla Public License v2.0',
      install_requires=requirements
)
