print("Make sure the file is formatted correctly. \nIt must, unfortunately, end with a line break.")

file = input("What is the file of bandcamp times?\n")
fhand = open(file)

timelist = list()
for line in fhand :
    if ':' not in line :
        continue

    loc = line.find("\n")
    line = line.rstrip()
    timestr = line[loc-5:]

    # Convert time to xx:xx format
    if len(timestr) != 5 :
        timestr = "0" + timestr

    # Append to list
    timelist.append(timestr)

# print(timelist)

#####################

secondstotal = 0
#

# Convert inputs to total seconds
for time in timelist :

    tenmin = float(time[0])
    onemin = float(time[1])
    sec = float(time[3:])

    secondstotal = secondstotal + tenmin*600 + onemin*60 + sec

# Convert seconds total back into time units
hours = int(secondstotal/3600)
secondstotal = secondstotal % 3600
mins = int(secondstotal/60)
seconds = secondstotal % 60

print("Total length is", hours, "hours,", mins, "mins, and", seconds, "seconds.")
