fn = input("enter a file name : ")
str = fn.split(".")
ext = "wrong file name"
if str[1] == "py" :
    ext="python"
elif str [1] == "c" :
    ext="c"
elif str [1] == "cpp" :
    ext="c++"
elif str [1] == "java" :
    ext="java"
elif str [1] == "doc" :
    ext="document"
elif str [1] == "ppt" :
    ext="power point presentation"

print("The extension of the file is : '"+ext+"'")

# output :
# C:\Users\rudre\OneDrive\Desktop\pythonmc>filename.py
# enter a file name : abc.py
# The extension of the file is : 'python'
