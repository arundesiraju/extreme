# Imports
import re
import numpy as np

def checkTimeValidity(inputTime):
	if(len(inputTime) != 3):
		print("Time format invalid")
		exit()
	if(int(inputTime[0]) < 0 or int(inputTime[0]) > 24):
		print("Time format invalid")
		exit()
	if(int(inputTime[1]) < 0 or int(inputTime[1]) > 59):
		print("Time format invalid")
		exit()
	if(int(inputTime[2]) < 0 or int(inputTime[2]) > 59):
		print("Time format invalid")
		exit()
		
def convertToSeconds(inputTime):
	return int(inputTime[0])*60*60+int(inputTime[1])*60+int(inputTime[2])
		
#Start and end times user input
startTime = input("Enter start time in HH:MM:SS\n")
startTime = re.split(':', startTime)
checkTimeValidity(startTime)

endTime = input("Enter end time in HH:MM:SS\n")
endTime = re.split(':', endTime)
checkTimeValidity(endTime)

#Find time difference by converting to seconds
startSeconds = convertToSeconds(startTime)
endSeconds = convertToSeconds(endTime)
diff = endSeconds-startSeconds
if(diff < 0):
	print("End time should be after start time")
	exit()

# File related
f = open("134.141.123.1.txt", 'r')
lines = f.readlines()

# Initialize metrics
success = 0
failure = 0
rtt = []

# Read line-by-line and split tokens
for line in lines:
	splitLine = re.split('\[|\]| ', line)
	inputTime = re.split(':', splitLine[2]) #Parse Time
	if(splitLine[3] == "PM"): # add 12 hours to the time if "PM" to convert to HH:MM:SS format
		inputTime[0] = int(inputTime[0]) + 12
		
	if(convertToSeconds(inputTime) >= startSeconds and convertToSeconds(inputTime)<endSeconds):
		if("Reply" in splitLine[6]):
			success = success+1
			value = int(splitLine[11])
			rtt.append(value)
		else:
			failure = failure+1
f.close()

if(success != 0):
	print("Success: " + str(success) + ", Failure: " + str(failure) + " (" + str("{:.2f}".format(failure*100/success))+"%)")
	print("RTT (avg/min/max/std) = (" + str("{:.2f}".format(np.mean(rtt))) + "/" + str(min(rtt)) + "/" + str(max(rtt)) + "/" + str("{:.2f}".format(np.std(rtt))) + ")")
else:
	print("Success: " + str(success) + ", Failure: " + str(failure))
	