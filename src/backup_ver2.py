import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = ['/home/jenkinset/development/documents/python/thinkpython', '/home/jenkinset/development/documents/python/byteofpython']

# 2. The backup must be stored in a main backup directory.
target_dir = '/home/jenkinset/tmp/'

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory in the main directory.
today = target_dir + time.strftime('%Y%m%d')
# The current time is the name of the zip archive.
now = time.strftime('%H%M%S')

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today) # Make directory
    print 'Successfully created directory', today
    
# The name of the zip file
target = today + os.sep + now + '.zip'

# 5. We use the zip command (in Linux) to put the files in a zip archive.
tar_command = "zip -r '%s' %s" % (target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'