import codecs 

# file size to be decoded
BLOCKSIZE = 64400 
with codecs.open("name.txt", "r", "currentEncoding") as sourceFile:
    with codecs.open('name2.txt', "w", "desiredEncoding") as targetFile:
        while True:
            contents = sourceFile.read(BLOCKSIZE)
            if not contents:
                break
            targetFile.write(contents)

# reads the file, saves it to var and then prints it to the screen
var = open('name2.txt', 'r', errors='ignore')
var2 = var.readlines()
print(var2) 
