import calendar
year=int(input("/n Enter year : "))
isLeap=calendar.isleap(year)
if isLeap:
    print(" Given year is Leap year : ",year)
else:
    print(" Given yera is notleap year :",year)
