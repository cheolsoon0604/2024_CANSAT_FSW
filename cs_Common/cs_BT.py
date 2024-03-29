import serial
import time

def Bluetooth_Init_Set() :
    global BT_serial
    global BT_buf
    # connect esd110
    # BT_serial = serial.Serial('/dev/ttyUSB0',115200, parity='N', timeout=0.001) #when connect to usb
    BT_serial = serial.Serial('/dev/ttyAMA0', 115200, parity='N', timeout=0.001)  # when connect to GPIO pins (tx4,rx5)
    BT_buf = ""  # for esd110

def BT_STOP() :
    BT_serial.write(b'+') # str.encode('+')
    BT_serial.write(b'+')
    BT_serial.write(b'+')
    BT_serial.write(b'0x0D')
    BT_serial.write(b'0x0A')

def BT_921600() :
    BT_serial.write(b'a')
    BT_serial.write(b't')
    BT_serial.write(b'+')
    BT_serial.write(b'u')
    BT_serial.write(b'a')
    BT_serial.write(b'r')
    BT_serial.write(b't')
    BT_serial.write(b'c')
    BT_serial.write(b'o')
    BT_serial.write(b'n')
    BT_serial.write(b'f')
    BT_serial.write(b'i')
    BT_serial.write(b'g')
    BT_serial.write(b',')
    BT_serial.write(b'9')
    BT_serial.write(b'2')
    BT_serial.write(b'1')
    BT_serial.write(b'6')
    BT_serial.write(b'0')
    BT_serial.write(b'0')
    BT_serial.write(b',')
    BT_serial.write(b'N')
    BT_serial.write(b',')
    BT_serial.write(b'1')
    BT_serial.write(b',')
    BT_serial.write(b'0')
    BT_serial.write(b'0x0D')
    BT_serial.write(b'0x0A')

def BT_115200() :
    BT_serial.write(b'a')
    BT_serial.write(b't')
    BT_serial.write(b'+')
    BT_serial.write(b'u')
    BT_serial.write(b'a')
    BT_serial.write(b'r')
    BT_serial.write(b't')
    BT_serial.write(b'c')
    BT_serial.write(b'o')
    BT_serial.write(b'n')
    BT_serial.write(b'f')
    BT_serial.write(b'i')
    BT_serial.write(b'g')
    BT_serial.write(b',')
    BT_serial.write(b'1')
    BT_serial.write(b'1')
    BT_serial.write(b'5')
    BT_serial.write(b'2')
    BT_serial.write(b'0')
    BT_serial.write(b'0')
    BT_serial.write(b',')
    BT_serial.write(b'N')
    BT_serial.write(b',')
    BT_serial.write(b'1')
    BT_serial.write(b',')
    BT_serial.write(b'0')
    BT_serial.write(b'0x0D')
    BT_serial.write(b'0x0A')

def BT_MODE() :
    BT_serial.write(b'a')
    BT_serial.write(b't')
    BT_serial.write(b'+')
    BT_serial.write(b'b')
    BT_serial.write(b't')
    BT_serial.write(b'm')
    BT_serial.write(b'o')
    BT_serial.write(b'd')
    BT_serial.write(b'e')
    BT_serial.write(b',')
    BT_serial.write(b'3')
    BT_serial.write(b'0x0D')
    BT_serial.write(b'0x0A')

def BT_ATS() :
    BT_serial.write(b'a')
    BT_serial.write(b't')
    BT_serial.write(b's')
    BT_serial.write(b'1')
    BT_serial.write(b'0')
    BT_serial.write(b'=')
    BT_serial.write(b'1')
    BT_serial.write(b'0x0D')
    BT_serial.write(b'0x0A')

def BT_ATZ() :
    BT_serial.write(b'a')
    BT_serial.write(b't')
    BT_serial.write(b'z')
    BT_serial.write(b'0x0D')
    BT_serial.write(b'0x0A')

def BT_Org_Init() :
    BT_STOP()
    BT_MODE()
    BT_921600()
    BT_ATZ()

def BT_Init() :
    Bluetooth_Init_Set()
    BT_Org_Init()


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

