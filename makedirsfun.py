import os

os.makedirs("myfirst_dir1/mysecond_dir1")
os.chdir("myfirst_dir1")
print(os.listdir())