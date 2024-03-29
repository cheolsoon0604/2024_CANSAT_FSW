import serial 
import time

# connect esd110
#BT_serial = serial.Serial('/dev/ttyUSB0',115200, parity='N', timeout=0.001) #when connect to usb
BT_serial = serial.Serial('/dev/ttyAMA0', 115200, parity='N', timeout=0.001) #when connect to GPIO pins (tx4,rx5)
BT_buf = "" # for esd110

BT_serial.isOpen()

def BT_receive_Op() :

    

    # read esd110 value 
    while BT_serial.inWaiting():

        BT_Raw_data = str(BT_serial.read()).strip()
        
        # print(data) # for debuging

        BT_buf += BT_Raw_data # buffering
        if BT_Raw_data[3] == "n": # last data of one line is '\n' so when data[3] is n then do decode 
            BT_buf = BT_buf.replace("'","") # remove (') and (b) because data has (') and (b) like this b'10.55' 
            BT_buf = BT_buf.replace("b","") 

            BT_buf = ""

def BT_send_Op() :

    BT_serial.write(queue_data)


for i in range(10):
    BT_receive_Op()
    time.sleep(0.1)
    