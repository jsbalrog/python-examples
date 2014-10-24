import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = ['/home/jenkinset/development/documents/python/thinkpython', '/home/jenkinset/development/documents/python/byteofpython']

# 2. The backup must be stored in a main backup directory.
target_dir = '/home/jenkinset/tmp'

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time.
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5. We use the zip command (in Linux) to put the files in a zip archive.
zip_command = "zip -r '%s' %s" % (target, ' '.join(source))

# Run the backup
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'