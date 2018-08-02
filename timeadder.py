secondstotal = 0

# Convert inputs to total seconds
while True :
    time = input("What is the next time? [eg 06:10] END to sum up and end.\n")
    if time == 'END' :
        break

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
