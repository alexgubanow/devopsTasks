#imports section
import re
#short version of logs, for testing
#with open('efvdf.txt') as logFile:
#looking for non heartbeat lines
with open('LogsForRegex.log') as logFile:
    #readout text
    logs = logFile.read()
    #running regex on text
    #'^' working as inverse
    #'()' - grouping
    #'?!' - A negative lookahead
    #'heartbeat' - word to avoid
    #'.' - any char
    #'$' - in the end of string
    #'+' - One or more occurrences
    importantThings = re.finditer(r"^((?!heartbeat).)+$", logs, re.MULTILINE)
    #iterate over matches
    for thing in importantThings:
        #printout string of match
        print(thing.group())
    