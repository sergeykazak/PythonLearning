file_name = 'TestFileW.txt'

with open(file_name, "r", encoding="utf-8") as file:
    content = [i.strip() for i in file.readlines()]
    print(content)

for i in content:
    print(i)

# Using with statements ensures that files are properly closed
# after use, even if exceptions occur during processing. This is a safer and more Pythonic way to work with files.