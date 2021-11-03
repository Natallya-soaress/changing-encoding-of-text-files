with open("name.txt" , "rb") as  fin :
    text = fin.read()

text.decode('currentEncoding').encode('desiredEncoding')
print(text)