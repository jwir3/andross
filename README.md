Andross
=============

__andross__ (n.) : From **An**droid **Dr**awable T**oss**er. A tool used for moving entire hierarchies of drawable resources into an Android resource file.

This utility is designed to preserve the hirearchy of drawable folders of a specific resolution, while copying files into your android project directory.

When using, for example, the [Android Asset Studio](http://romannurik.github.io/AndroidAssetStudio ), the drawables come prepared in a folder hierarchy like the following:

```
- res/
  | - drawable-hdpi/
    |- image.png
  | - drawable-xhdpi/
    |- image.png
    ...
```

Unfortunately, copying each of these by dragging and dropping into Android Studio leads to a number of cumbersome and repetitive operations. On Mac computers, simply dragging each respective folder using the Finder onto one another causes other, existing drawables to be replaced. Andross solves this problem for you by copying the files in each directory, and preserving the resource hierarchy, so you can perform one copy operation, and move on with your life.

Command Line Usage
-------------------

```
$ andross -s <source directory> <android project directory>
```
