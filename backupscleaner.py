from backupscleaner.builder import BackupsFileList
from posix import mkdir
import tempfile
from backupscleaner.cleaner import BackupsCleaner

def setup_test():
    temp_dir = tempfile.mkdtemp()
    file_list = ('/tmp/2015/05/05_abc.bak',
'/tmp/2015/05/04_abc.bak',
'/tmp/2015/05/03_abc.bak',
'/tmp/2015/05/02_abc.bak',
'/tmp/2015/05/01_abc.bak',
'/tmp/2015/04/30_abc.bak',
'/tmp/2015/04/29_abc.bak',
'/tmp/2015/04/28_abc.bak',
'/tmp/2015/04/27_abc.bak',
'/tmp/2015/04/26_abc.bak',
'/tmp/2015/04/25_abc.bak',
'/tmp/2015/04/24_abc.bak',
'/tmp/2015/04/23_abc.bak',
'/tmp/2015/04/22_abc.bak',
'/tmp/2015/04/22_abc.bak',
'/tmp/2015/04/22_abc.bak',
'/tmp/2015/04/22_abc.bak',
'/tmp/2015/04/22_abc.bak',
'/tmp/2015/04/22_abc.bak',
'/tmp/2015/04/22_abc.bak',
'/tmp/2015/04/22_abc.bak',
'/tmp/2015/04/22_abc.bak',
'/tmp/2015/04/22_abc.bak',
'/tmp/2015/04/22_abc.bak',
'/tmp/2015/04/22_abc.bak')

backups_list = BackupsFileList('/servershare/TV Shows/2 Broke girls')

print backups_list

cleaner = BackupsCleaner(backups_list, daily=4)
cleaner.clean()