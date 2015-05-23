'''
Created on 2015-05-22

@author: kandalafti
'''

import backupscleaner.builder
from hamster.widgets.timechart import DAY

class BackupsCleaner(object):
    '''
    classdocs
    '''

    def __init__(self, backups_file_list, daily=14, weekly=6, monthly=4, annually=2):
        '''
        Constructor
        '''
        self.backups_file_list = backups_file_list.copy() 
        self.retention_schedule = {
                            'daily': daily,
                            'weekly': weekly,
                            'monthly': monthly,
                            'annualy': annually
                         }
        
    def clean(self, dry_run=False):
        self.__flag_retainable_backups(self.backups_file_list, self.retention_schedule)
    
    def __flag_retainable_backups(self, file_list, schedule):
        retained = {
                    'daily': 0,
                    'weekly': 0,
                    'monthly': 0,
                    'annually': 0
                    }
        
        for bucket in file_list.values():
            for year in reversed(sorted(bucket.keys())):
                for month in reversed(sorted(bucket[year].keys())):
                    for day in reversed(sorted(bucket[year][month].keys())):
                        print year, month, day
                        if retained['daily'] < schedule['daily']:
                            print "retain"
                            retained['daily'] += 1
    
    #def __flag_daily(self):
        
    #def __flag_weekly(self):
        
    #def __flag_monthly(self):
        
    #def __flag_annually(self):