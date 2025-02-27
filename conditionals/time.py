# Robert Nelson, How to get time of day or Time of Day - Python

import time

#first instance of time in progamming
first_time = time.gmtime
# print(first_time)

# Current time in seconds
current = time.time()
#print(current) # seconds since Jan 1 1970

# Current date and time like we see normally
now = time.ctime(current)
# print(now)

# Get just a part of time
local_time = time.localtime(current)
day = local_time.tm_wday
hour = local_time.tm_hour # military time (0-23 hours)

#print(hour)

if hour >=0 and hour <=12: #<= if always starts the conditional
    print("Good morning")
    
elif hour >=12 and hour <=17: #<= everything in between should be elif
    print("Good afternoon")
    """
elif hour >=17 and hour <=23:
    print("Good evening")"""
else: #<= else always ends the conditional
    print("Good evening")


#< less than
#> greater than
#<= less than or equal to
#>= greater than or equal to
#== Equal to
#=== *Doesn't exist in Python*
#! Not