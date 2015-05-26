'''
Created on 2015-05-22

@author: kandalafti
'''

import backupscleaner.builder
import datetime
from hamster.widgets.timechart import DAY

class BackupsCleaner(object):
    '''
    classdocs
    '''

    def __init__(self, backups_file_list, daily=14, weekly=6, monthly=6, annually=3):
        '''
        Constructor
        '''
        self.backups_file_list = backups_file_list.copy() 
        self.retention_schedule = {
                            'daily': daily,
                            'weekly': weekly,
                            'monthly': monthly,
                            'annually': annually
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
        
        
        #retain_days_date = today - datetime.timedelta(days=14)
        
        for bucket in file_list.values():
            for year in reversed(sorted(bucket.keys())):
                for month in reversed(sorted(bucket[year].keys())):
                    for day in reversed(sorted(bucket[year][month].keys())):
                        print year, month, day
                            #backup_date = datetime.date(year, month, day)
                            #if backup_date > retain_days_date:
                            #elif month > today.month - 2:
                                
                            #bucket[year][month][day]['retain'] = True
                            
                            #retained['daily'] += 1
        self.__flag_monthly(file_list, schedule)
        self.__flag_annually(file_list, schedule)
    
    #def __flag_daily(self):
        
    #def __flag_weekly(self):
        
    def __flag_monthly(self, file_list, schedule):
        today = datetime.date.today()
        for multiplier in range(1, schedule['monthly']):
            ret_date = (today - datetime.timedelta(days=30*multiplier))
            for bucket in file_list.keys():
                if file_list[bucket].has_key(ret_date.year) and file_list[bucket][ret_date.year].has_key(ret_date.month):
                    oldest_day = reversed(sorted(file_list[bucket][ret_date.year][ret_date.month].keys())).pop()
                    file_list[bucket][ret_date.year][ret_date.month][oldest_day]['retain'] = True
                    print ret_date.year, ret_date.month, oldest_day
                else:
                    print 'No monthly backup for ', bucket, ret_date.year, ret_date.month
                
            #print month 
    def __flag_annually(self, file_list, schedule):
        today = datetime.date.today()
        for multiplier in range(1, schedule['annually']):
            ret_date = (today - datetime.timedelta(days=365*multiplier))
            for bucket in file_list.values():
                if bucket.has_key(ret_date.year):
                    oldest_month = reversed(sorted(bucket.keys())).pop()
                    oldest_day = reversed(sorted(bucket[oldest_month].kceys())).pop()
                    bucket[ret_date.year][oldest_month][oldest_day]['retain'] = True
                    print ret_date.year, oldest_month, oldest_day
                else:
                    print 'No yearly backup for ', bucket, ret_date.year