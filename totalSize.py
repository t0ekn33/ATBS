#! python3

import os

#lists files in /test and outputs total file size in bytes

totalSize = 0
for filename in os.listdir('/home/toeknee/test'):
    if not os.path.isfile(os.path.join('/home/toeknee/test', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('/home/toeknee/test', filename))
    print(totalSize)