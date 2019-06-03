#imports section
import re
#open log file
with open('LogsToSplit.txt') as logFile:
    #readout text
    logs = logFile.read()
    #list of different activities
    activityList = []
    #running regex on text to find only codes of activity
    codes = re.finditer(r"(?<=^(([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))" + 
            r"T.{2}:[0-5][0-9]:[0-5][0-9].{15}\[))(.{1,10})(?=\])", logs, re.MULTILINE)
    #iterate over matches
    for code in codes:
        #printout string of match
        try:
            activityList.index(int(code.group()))
        except ValueError as identifier:
            activityList.append(int(code.group()))
    #sorting activityList
    activityList.sort()
    #logs of different activities
    activitySortedLogs = []
    #taking logStrings for each activity code
    for activity in activityList:
        #looking for log entries, which contains current activity code
        activityLog = re.finditer(r"^(([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))" + 
            r"T.{2}:[0-5][0-9]:[0-5][0-9].{15}\[)" + str(activity) + r"\].*?" + 
                r"(?=\n^(([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))T.{2}:[0-5][0-9]:[0-5][0-9].{15}\[))", logs, re.DOTALL | re.MULTILINE)
        #prepare str for collect all logs in one
        activityLogStr = ""
        #squash logs
        for activityLogLine in activityLog:
            activityLogStr = activityLogStr + activityLogLine.group() + "\n"
        #push collected logs to array
        activitySortedLogs.append(activityLogStr)
    #iterate over all logs and write them to separete files
    for i in range(0, activityList.__len__()):
        f = open("activity["+ str(activityList[i]) +"]SortedLog.log", "w")
        f.write(activitySortedLogs[i])
        f.close()
    
    #iterate over all logs and write them to one file
    f = open("SortedLog.log", "w")
    for activitySortedLog in activitySortedLogs:
        f.write(activitySortedLog)
    f.close()