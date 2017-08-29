# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

`pwd` Print working directory  
`mkdir [directory]` Create a directory  
`rmdir [directory]` Remove a directory  
`touch [file]` Creates files or modifies the accessed/modified data of files  
`rm [file]` Removes a file  
`mv [file]` Moves or renames a file  
`ls -a or ls-A ` Will show all files, included hidden ones. The latter command does not include . and .. directories.  
`cp [origin] [destination]` Copies a file from one location to another  
`cat [file]` Used to view the contents of text files, concatenate files, or create files.  
`grep [flags] [pattern] [file/directory]` Used to search for text within files  
`sed "s/[word]/[replacement]/[flags]"` Stream editor. This specific command replaces words in a text file  
`clear` Clears the console.  
`alias [alias]='command'` Sets an alias for a command  
`echo [Text to print]` Prints the text to standard output  

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls` Lists the files and directories in the current working directory  
`ls -a` Lists all the files and directories including hidden files (files that begin with ".")  
`ls -l` Lists files in long form, showing permissions, number of hard links, group owner, user owner, file size, last modified and name  
`ls -lh` Same as above except lists file size in human readable form  
`ls -lah` Combination of -l, -a, and -h. i.e. longform, show hidden files, and human readable  
`ls -t` Lists files in order of last modified, newest first  
`ls -Glp` Lists files in long form, excluding group info, with "/" appending to directories  

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

`ls -R` Shows subdirectories and their contents  
`ls -1` Displays each entry on a line  
`ls -u` Display each entry by access time  
`ls -o` Essentially `ls -Gl`  
`ls -A` Shows all files and directories, exluding the current and previous directory ("." and "..")


---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

`xargs` takes a command (default being echo) and similar to a loop, will run the command on each word/element in stdin delimited by a space or line.

An example could be deleting all files with a certain extension from all subdirectories.  
`find . -name *.md | xargs rm -f`  
The first command will find all occurances with the extension ".md". This results in a list that is piped into xargs which is given the rm command with the -f flag. The command is run with each element in the list, thus removing all files with the extension ".md".

 

