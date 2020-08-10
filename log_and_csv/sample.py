#!/usr/bin/env python3

import re
import csv
import operator
import subprocess

errStats_A = {}		#Dict: {*errMsg:*errCount, ...}
errStats_B = []	#List of Dict: [{'errMsg':*errMsg, 'errCount':*errCount}, ...]
userStats_A = {}	#Dict: {*username:*(*infoCount,*errCount), ...}
userStats_B = []	#List of Dict: [{'username':*username, 'infoCount':*INT, 'errCount':*INT}, ...]

sample1 =	[{"INT":1,"STR":'one'},
			 {"INT":2,"STR":'two'},
			 {"INT":3,"STR":'three'}]

sample2 =	[{'aaa':(1,1) , 'bbb':(2,2) , 'ccc':(3,3)},
			 {'aaa':(1,2) , 'bbb':(2,3) , 'ccc':(3,4)},
			 {'aaa':(1,3) , 'bbb':(2,4) , 'ccc':(3,5)}]

sample3 =	[{'username':'pippo','INFO':1,'ERR':1},
			 {'username':'topolino','INFO':2,'ERR':2},
			 {'username':'paperino','INFO':3,'ERR':3}]

'''
print(sample1[1])				#prints --> {'INT': 2, 'STR': 'two'}
print(sample1[1]["STR"])		#prints --> two
print(sample2[1])				#prints --> {'aaa': (1, 2), 'bbb': (2, 3), 'ccc': (3, 4)}
print(sample2[1]['ccc'])		#prints --> (3, 4)

print( type(sample1) )			#prints --> <class 'list'>
print(sample1)					#prints --> [{'INT': 1, 'STR': 'one'}, {'INT': 2, 'STR': 'two'}, {'INT': 3, 'STR': 'three'}]
#print(sample1.items())			#prints --> AttributeError: 'list' object has no attribute 'items'
print(sample1[0].items()) 		#prints --> dict_items([('INT', 1), ('STR', 'one')])
print(sample1[1].keys())		#prints --> dict_keys(['INT', 'STR'])
print(sample1[2].values())		#prints --> dict_values([3, 'three'])

print( type(sample2) )			#prints --> <class 'list'>
print(sample2)					#prints --> *full list of dicts*
print(sample2[0].items())		#prints --> dict_items([('aaa', (1, 1)), ('bbb', (2, 2)), ('ccc', (3, 3))])
print(sample2[1].keys())		#prints --> dict_keys(['aaa', 'bbb', 'ccc'])
print(sample2[2].values())		#prints --> dict_values([(1, 3), (2, 4), (3, 5)])
'''

# print( [item for item in sample3] )

with open("log.log", "r") as logfile:
	#userStats_A & errStats_A :: Dictionary
	regex = r"(INFO|ERROR): ([\w+ \w]+) \((\w+)\)"
	for log in logfile:
		result = re.search(regex,log)
		logType = result.group(1)
		logText = result.group(2)
		logUser = result.group(3)

		tmp_userInfoCount = 0
		tmp_userErrCount = 0
		tmp_errCount = 0

		if result == None:
			print("ERROR: " + str(log) + " DOES NOT MATCH THE REGEX")
		else:
			if logType == 'INFO':
				#if user c'è
				if logUser in userStats_A.keys():
					#user[info]++
					tmp_userInfoCount = userStats_A[logUser][0]+1
					tmp_userErrCount = userStats_A[logUser][1]
				else:
				#user[info]=1, user[error]=0
					tmp_userInfoCount = 1
					tmp_userErrCount = 0
			elif logType == 'ERROR':
				if logUser in userStats_A.keys():
					tmp_userInfoCount = userStats_A[logUser][0]
					tmp_userErrCount = userStats_A[logUser][1]+1
				else:
					tmp_userInfoCount = 0
					tmp_userErrCount = 1
				if logText in errStats_A.keys():
					tmp_errCount = errStats_A[logText]+1
				else:
					tmp_errCount = 1
				errStats_A[logText] = tmp_errCount
			userStats_A[logUser] = (tmp_userInfoCount,tmp_userErrCount)
logfile.close()

with open("log.log", "r") as logfile:
	#userStats_B & errStats_B :: LIST of Dictionaries
	regex = r"(INFO|ERROR): ([\w+ \w]+) \((\w+)\)"
	for log in logfile:
		result = re.search(regex,log)
		logType = result.group(1)
		logText = result.group(2)
		logUser = result.group(3)

		if result == None:
			print("ERROR: " + str(log) + " DOES NOT MATCH THE REGEX")
		else:
			usr_found = False
			err_found = False
			for index,dict in enumerate(userStats_B):
				if dict.get('USERNAME') == logUser:
					usr_found = True
					userStats_B[index] = {'USERNAME':logUser, 'INFO':dict['INFO']+int(logType=='INFO'), 'ERROR':dict['ERROR']+int(logType=='ERROR')}
					break
			for index,dict in enumerate(errStats_B):
				if dict.get('ERROR') == logText:
					err_found = True
					errStats_B[index] = {'ERROR':logText, 'COUNT':dict['COUNT']+1}
					break
			if not usr_found:
				userStats_B.append( {'USERNAME':logUser, 'INFO':int(logType=='INFO'), 'ERROR':int(logType=='ERROR')} )
			if not err_found and logType == 'ERROR':
				errStats_B.append( {'ERROR':logText, 'COUNT':1} )
logfile.close()

with open("sampleCsv_1.csv", "w") as csvfile:
	writer = csv.DictWriter( csvfile, fieldnames=['INT', 'STR'])
	writer.writeheader()
	writer.writerows( sample1 )
csvfile.close()

with open("sampleCsv_2.csv", "w") as csvfile:
	writer = csv.DictWriter( csvfile, fieldnames=['aaa', 'bbb', 'ccc'])
	writer.writeheader()
	writer.writerows( sample2 )
csvfile.close()

with open("sampleCsv_3.csv", "w") as csvfile:
	writer = csv.DictWriter( csvfile, fieldnames=['username','INFO','ERR'])
	writer.writeheader()
	writer.writerows( sample3 )
csvfile.close()

with open("sampleErrCount_A.csv", 'w') as csvfile:
#	single_dict = {'a':1,'b':2}
#	dicts_list = [ {'key':d[0], 'value':d[1]} for d in single_dict.items() ]
	errCount = [ {'ERROR':dict[0], 'COUNT':dict[1]} for dict in errStats_A.items()]
	writer = csv.DictWriter( csvfile, fieldnames=['ERROR','COUNT'] )
	writer.writeheader()
	writer.writerows( sorted( errCount, key=operator.itemgetter("COUNT"), reverse=True  ) )
csvfile.close()

with open("sampleErrCount_B.csv", 'w') as csvfile:
	writer = csv.DictWriter( csvfile, fieldnames=['ERROR','COUNT'] )
	writer.writeheader()
	writer.writerows( sorted( errStats_B, key=operator.itemgetter("COUNT"), reverse=True ) )
csvfile.close()

with open("sampleUsrStats_A.csv", 'w') as csvfile:
#	dict = {'a':(1,2),'b':(3,4)}
#	dicts = [ {'name':d[0], 'val1':d[1][0], 'val2':d[1][1]} for d in dict.items() ]
	usrStat = [ {'USERNAME':dict[0], 'INFO':dict[1][0], 'ERROR':dict[1][1]} for dict in userStats_A.items() ]
	writer = csv.DictWriter( csvfile, fieldnames=['USERNAME','INFO','ERROR'] )
	writer.writeheader()
	writer.writerows( sorted( usrStat, key=operator.itemgetter('USERNAME') ) )
csvfile.close()

with open("sampleUsrStats_B.csv", 'w') as csvfile:
	writer = csv.DictWriter( csvfile, fieldnames=['USERNAME','INFO','ERROR'] )
	writer.writeheader()
	writer.writerows( sorted( userStats_B, key=operator.itemgetter("USERNAME") ) )
csvfile.close()


print("-------------------sampleCsv_1.csv-------------------")
subprocess.run( ['cat', "sampleCsv_1.csv"] )

print("-------------------sampleCsv_2.csv-------------------")
subprocess.run( ['cat', "sampleCsv_2.csv"] )

print("-------------------sampleCsv_3.csv-------------------")
subprocess.run( ['cat', "sampleCsv_3.csv"] )

print("----------------sampleErrCount_A.csv----------------")
subprocess.run( ['cat', "sampleErrCount_A.csv"] )

print("----------------sampleErrCount_B.csv----------------")
subprocess.run( ['cat', "sampleErrCount_B.csv"] )

print("----------------sampleUsrStats_A.csv----------------")
subprocess.run( ['cat', "sampleUsrStats_A.csv"] )

print("----------------sampleUsrStats_B.csv----------------")
subprocess.run( ['cat', "sampleUsrStats_B.csv"] )
