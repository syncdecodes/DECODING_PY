print("Python can be used to perform operations on a file. (read and write data)")
print("RAM - random access memory")


"""
Mode | Meaning              | File must exist? | Erases file?
-----|-----------------------|------------------|--------------
r    | Read                 | YES              | NO
w    | Write                | NO               | YES
a    | Append               | NO               | NO
r+   | Read + Write         | YES              | NO
w+   | Write + Read         | NO               | YES
a+   | Append + Read        | NO               | NO
rb   | Read Binary          | YES              | NO
wb   | Write Binary         | NO               | YES
ab   | Append Binary        | NO               | NO
rb+  | Read + Write Binary  | YES              | NO
wb+  | Write + Read Binary  | NO               | YES
ab+  | Append + Read Binary | NO               | NO

"""


"""
Method                | Meaning / What it Does
----------------------|------------------------------------------------------------
open()                | Opens a file and returns a file object.
close()               | Closes the file.
read()                | Reads entire file as a single string.
read(n)               | Reads first n characters/bytes.
readline()            | Reads one line from file.
readlines()           | Reads all lines and returns a list of strings.
write(str)            | Writes a string to the file.
writelines(list)      | Writes a list of strings to the file.
seek(pos)             | Moves the file pointer to position 'pos'.
seek(offset, whence)  | Moves pointer relative to start(0), current(1), end(2).
tell()                | Returns current cursor/file pointer position.
flush()               | Forces writing of buffered data to file.
truncate(size)        | Cuts file to given size (if no size → truncates to current pos).
fileno()              | Returns system file descriptor (low-level number).
isatty()              | Returns True if file is connected to terminal (rarely used).
readable()            | Returns True if file can be read.
writable()            | Returns True if file can be written.
seekable()            | Returns True if file pointer can be moved.

"""