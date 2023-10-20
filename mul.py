import calendar
year=int(input("/n Enter year : "))
isLeap=calendar.isleap(year)
if isLeap:
    print("/n Given year is Leap year : ",year)
else:
    print("/n Given yera is notleap year :",year)