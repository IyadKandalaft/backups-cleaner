'''
Created on 2015-05-22

@author: Iyad Kandalaft <iyad.kandalaft@agr.gc.ca>
'''

import os
import re
import time


class BackupsFileList(dict):
    
    '''
    classdocs
    '''
    
    def __init__(self, path, filename_regex=None, follow_links=True):
        '''
        Constructor
        '''
        self.original_path = path
        self.bucket_pattern = filename_regex
        
        if filename_regex is not None:
            self.__traverse_path(path, follow_links, re.compile(filename_regex))
        else:
            self.__traverse_path(path, follow_links)

    
    def __traverse_path(self, path, follow_links = True, bucket_matcher = None):
        for root, dirs, files in os.walk(self.original_path, topdown=True, followlinks=follow_links):
            for name in files:
                filename = os.path.join(root, name)
                backup_file = BackupsFile(filename)
                
                if backup_file.is_link():
                    continue
                
                (tm_year,tm_mon,tm_mday,tm_hour,tm_min, tm_sec,tm_wday,tm_yday,tm_isdst) = backup_file.mtime()
                if bucket_matcher is not None:
                    matches = bucket_matcher.match(backup_file.basename())
                    if matches is None:
                        continue
                    
                    bucket = ''.join(matches.groups())
                else:
                    bucket = 'all_files'
                
                self.__create_keys(bucket, tm_year, tm_mon, tm_mday)                   
                self[bucket][tm_year][tm_mon][tm_mday][backup_file.path] = backup_file

    def __create_keys(self, *hierarchy):
        # Create nested dictionaries
        obj = self
        for item in hierarchy:
            if not obj.has_key(item):
                obj[item] = {}
            obj = obj[item]
                    
class BackupsFile(object):
    def __init__(self, path):
        self.path = path
            
    def is_link(self):
        return os.path.islink(self.path)
    
    def parent_dir(self):
        return os.path.dirname(self.path)
    
    def mtime(self):
        if not self.is_link():
            return time.localtime(os.path.getmtime(self.path))
        
    def basename(self):
        return os.path.basename(self.path)