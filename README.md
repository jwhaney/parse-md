# **parse-md**

### description
a python script to iterate through a directory of markdown files (/md_files), pull frontmatter key/value pairs, and create a csv using the unique keys as fields for all md files.

### setup
- built with python 3.5.2
- script only requires native os and csv libraries

### run it
1. `clone` or download this repo
2. copy and paste your own markdown (.md or .markdown) files to the md_files subdirectory
3. *optional:* change the output csv filename (line 87)
4. open terminal and `cd` into this repo
5. type `python3 parse-md.py` and press enter
