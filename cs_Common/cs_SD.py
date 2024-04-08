import cs_Time

# make file and open


nowtime = cs_Time.Time_Return()
filePath = "Cansat_Log/cs_Log/"
fileName = f"{filePath}CANSAT_LOG_{nowtime}"

try:
    f = open(fileName, 'w')
    log = open(fileName,'w')
except:
    print("Failed to open file")
