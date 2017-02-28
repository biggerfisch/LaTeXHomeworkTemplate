# LaTeXHomeworkTemplate

This template is what I use for my programming assignments that have to be handed in along with their output and generated images.
It mostly automates the process of compiling the components together into a suitable PDF.
It's currently setup for python, though it shouldn't be hard to change, especially to another uncompiled language. 
A compiled language might want to either move the source files to a subdirectory with its own makefile, or append this one.

### Usage:
1. Create your python files in the naming scheme of `problem-NUMBER-SECTION.py`. If there is no section, omit that and the last dash
2. Edit `hw.tex`, changing the title parameters to fit YOU
3. For each problem, create a new `homeworkProblem` section (`\begin{homeworkProblem}`). The problem number will auto increment for each section. 
  1. In that section, if your problem is split into parts, start a _named_ `homeworkSection` (`\begin{homeworkSection}{NAME}`). NAME can be any string (I think).
  2. Now, for each problem or section, the following commands are available and very automated:
     - `\homeworkPython`
       - Includes the python code
     - `\homeworkOutput`
       - Includes the stdout from running the python
     - `\homeworkGraph`
       - Include an image with name `problem-NUMBER[-SECTION].png`. Currently, only one image per section will work automatically.
  3. Add any description or text you like
4. Run `make` in the directory. This will generate your PDF as `hw.pdf` and you'll be good to go!

### Other notes
Subsub sections do not work right now. ie, you cannot have 1.a.i yet, without naming a section "a.i".

`python` is hardcoded at the moment, might want to change that...

This has only been tested on OS X so far. Something might fail elsewhere! Please report if it does and I'll look into it eventually.

##Pull requests welcome!
