import os

os.makedirs("mk_dir_1/mk_dir_2")
os.chdir("mk_dir_1")
print(os.getcwd())
os.chdir("mk_dir_2")
print(os.getcwd())