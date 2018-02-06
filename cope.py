#!/usr/bin/python
# Filename: cope.py

import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = [r'C:\Users\user\Desktop\py', r'C:\Users\user\Desktop\algorithm']
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that  'C:\\Documents'

# 2. The backup must be stored in a main backup directory
target_dir = r'C:\Users\user\Desktop\py\py' # Remember to change this to what you will be using

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr %s %s" % (target, ' '.join(source))
#rar a 命令也可以，此命令隐藏文件也会压缩进去，zip -qr不会       zip_command = "rar a %s %s" % (target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'