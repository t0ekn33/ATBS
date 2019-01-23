import os

os.chdir('/home/toeknee/test')

for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename)    #uncomment to delete
        print(filename)    #test to view which files will be deleted