print("We have to open file before reading and writing and should close the files at the end")

"""
f = open("file_name", "mode")
file_name eg - sample.txt or demo.docx
mode eg - r: red mode and w: write mode by default it is in read mode

data = f.read() # read entire file
data = f.readline() # read one line at a time (note if .read is alreday executed .readline wont work)

f.close() # do close the file at the end
"""

file = open("demo2.txt", "r")
data = file.read()
print(data)
print(type(data))
file.close()



"""
file2 = open("demo2.txt", "r")
line1 = file2.readline()
print(line1)
line2 = file2.readline()
print(line2)

code wont work bcs we already read it before
"""