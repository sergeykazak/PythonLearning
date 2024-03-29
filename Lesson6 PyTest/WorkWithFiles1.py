import docx

# file_name = 'Test file.docx'
# file = open(file_name, "r", encoding='utf-8')
# print(file)
# content = file.read()
# print(content)
# file.close()

file_name = 'TestFile.txt'
file = open(file_name, mode="r", encoding='utf-8')
print(file) #<_io.TextIOWrapper name='TestFile.txt' mode='r' encoding='utf-8'>
# content = file.read()
# print(content.strip())

#!!! for file reading mode = 'r' may not be added for open
# !!!for file writing mode = 'w' - must be provided for open

# Reopen the file to read again
file = open(file_name, mode="r", encoding='utf-8')
content2 = [i.strip() for i in file.readlines()] # via i.strip() for i in we remove all spaces before and after
print(content2) #['          Hello\n', '        Goodbye'] - printed if i.strip() for i in ... is not used above
file.close()

#
# file_name1 = 'TestFile_New.txt'
# file = open(file_name1, 'a', encoding='utf-8') #a - to add, w -write
# file.write("\nLet's Go!!")
#
#!!! for w - write - file will be either created (if it doesn't exist) or will be updated (if exists)
# file.close()
