# the open() function has three parameters: 
# 1. the name of the file to be opened - filename 
# 2. the mode in which the file is to be opened - w for write, r for read, a for append
# 3. the encoding of the file - utf-8 for unicode

with open("../files/basic.csv", encoding="utf-8") as f:
    read_data = f.read()

    for line in read_data.split(","):
        print(line)