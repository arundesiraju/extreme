import pandas as pd
import re

def checkTimeValidity(inputTime):
	inputTime = re.split(',|:| ', inputTime)
	if(len(inputTime) != 8):
		print("Time format invalid")
		exit()
		
#Start and end times user input
startTime = input("Enter start time in the following format : May 5, 2021 6:59:31 PM\n")
checkTimeValidity(startTime)

endTime = input("Enter end time in the following format : May 5, 2021 6:59:31 PM\n")
checkTimeValidity(endTime)
	
# Read the csv
df = pd.read_csv("XCC_StationEventsLog.csv")

# Filter 
df_filtered = df.loc[(df['Time'] >= startTime) & (df['Time'] < endTime) & (df['MAC Address'] == '94:9B:2C:0E:C8:30') & (df['Event Type'] == 'Roam')]

# Print count for each AP
print(df_filtered.groupby('AP Name')['Event Type'].agg(['count']))









