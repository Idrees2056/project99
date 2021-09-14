import os 
#os.system("date") 
os.mkdir("C:/Users/Admin/Desktop/Python/os and shuttle/hope")
c=os.getcwd()
print("this is the current working directory"+c)

path="C:/Users/Admin/Desktop/Python/os and shuttle/code"
o=os.path.exists(path)
print(o)

path2="C:/Users/Admin/Desktop/Python/os and shuttle/os 1.py"
d=os.path.splitext(path2)
print(d)

k=os.listdir()
print(k)