import os

os.chdir('/home/toeknee/test')
#test
for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)