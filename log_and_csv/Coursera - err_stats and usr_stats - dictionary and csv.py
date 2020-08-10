#!/usr/bin/env python3

import re
import csv
import operator

err_stats = {}
usr_stats = {}

with open("syslog.log", 'r') as syslog:
    regex = r"ticky: (INFO|ERROR):? (.*?) ?(\[#\d+\])? \((\w+\.?\w+)\)"
    for log in syslog:
        result = re.search( regex, log)
        log_type = result.group(1)
        log_msg = result.group(2)
        log_usr = result.group(4)

        if log_usr in usr_stats.keys():
            usr_stats[log_usr] = ( usr_stats[log_usr][0]+int(log_type=='INFO'),usr_stats[log_usr][1]+int(log_type=='ERROR') )
        else:
            usr_stats[log_usr] = ( int(log_type=='INFO'),int(log_type=='ERROR') )
        if log_msg in err_stats.keys():
            err_stats[log_msg] += 1
        elif log_type == 'ERROR':
            err_stats[log_msg] = 1
#syslog.close()

#Transformation from {dict} to [list of {dict}]
error_statistics = [ {'Error':item[0],'Count':item[1]} for item in err_stats.items() ]
user_statistics = [ {'Username':item[0],'INFO':item[1][0],'ERROR':item[1][1]} for item in usr_stats.items() ]

#Sorting
error_statistics.sort(key=operator.itemgetter('Count'),reverse=True)
user_statistics.sort( key=operator.itemgetter('Username') )

with open("error_message.csv", 'w') as csvfile:
    writer = csv.DictWriter( csvfile, fieldnames=['Error','Count'])
    writer.writeheader()
    writer.writerows(error_statistics)
#csvfile.close()

with open("user_statistics.csv", 'w') as csvfile:
    writer = csv.DictWriter( csvfile, fieldnames=['Username','INFO','ERROR'])
    writer.writeheader()
    writer.writerows(user_statistics)
#csvfile.close()
