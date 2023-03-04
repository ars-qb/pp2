name = input("Enter name of file: ")
f = open(name, "w")

def get():
    return input("Enter line of text: ")
line = get()
while line:
    f.write(line+'\n')
    line = get()

f.close()
with open(name, "r") as f:
    print(f.read())