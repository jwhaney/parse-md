# **parse-md**

### description
a python script to iterate through a directory of markdown files (md_files), pull frontmatter key/value pairs, and create a csv using the unique keys as fields for all md files.

### setup
- built with python 3.5.2
- script only requires native python3 os and csv libraries

### run it
1. place script in root directory of your project
2. copy your own markdown (.md or .markdown) files to the md_files subdirectory
3. if you wish, change the output csv filename you want to create
4. open the terminal and `cd` into the project `root` directory
5. type `python3 parse-md.py` and press enter
