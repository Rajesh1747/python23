import subprocess
new_datatime="2023-01-01 12:00:00"
try:
    subprocess.rum(["sudo","data","-s",new_datatime])
    subprocess.run(["sudo","hwclock","--systoch"])
    print("Data and time  change to :",new_datatime)
except Exception as e:
    print("Faild to change the Data and Time : ",str)