contents =["This should go in A.txt","This should go in B.txt","This should go in C.txt"]
filenames = ["A.txt","B.txt","C.txt"]

for content, filename in zip(contents,filenames):
    file = open(f"../files/{filename}",'w')
    file.write(content)
