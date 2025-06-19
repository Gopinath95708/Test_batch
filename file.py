txt=input("Enter a word to create txt: ")
txt_1=txt.replace(" ","\n")
file_name=input("Enter a file to open: ")
file=open(f"{file_name}", "w")
file.write(txt_1)
try:
    with open(f"{file_name}", "a") as f1:
        f1.write(" Good luck")
except IOError:
    print("file not found")
else:
    print("Successfully runned")            

