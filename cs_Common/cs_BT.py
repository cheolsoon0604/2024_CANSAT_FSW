import serial
from queue import Queue

RX_Queue_Idx = 0
TX_Queue_Idx = 0
RX_Queue = Queue()
TX_Queue = Queue()

global BT_serial
global BT_buf

def BT_Port_Speed_Set(Baurate) :
    # connect esd110
    # BT_serial = serial.Serial('/dev/ttyUSB0',115200, parity='N', timeout=0.001) #when connect to usb
    BT_serial.Serial('/dev/ttyAMA0', Baurate, parity='N', timeout=0.001) # when connect to GPIO pins (tx4,rx5)

def Bluetooth_Init_Set() :
    BT_serial.isOpen()
    BT_Port_Speed_Set(9600) # default baud rate : 9600
    BT_ATZ()
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
    BT_serial.write(b'N') # NO parity
    BT_serial.write(b',')
    BT_serial.write(b'1') # STOP bit
    BT_serial.write(b',')
    BT_serial.write(b'0') # HW flow control
    BT_serial.write(b'0x0D')
    BT_serial.write(b'0x0A')
    BT_ATZ()
    BT_Port_Speed_Set(921600)

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
    BT_serial.write(b'N') # NO parity
    BT_serial.write(b',')
    BT_serial.write(b'1') # STOP bit
    BT_serial.write(b',')
    BT_serial.write(b'0') # HW flow control
    BT_serial.write(b'0x0D')
    BT_serial.write(b'0x0A')
    BT_ATZ()
    BT_Port_Speed_Set(115200)

def BT_9600() :
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
    BT_serial.write(b'6')
    BT_serial.write(b'0')
    BT_serial.write(b'0')
    BT_serial.write(b',')
    BT_serial.write(b'N') # NO parity
    BT_serial.write(b',')
    BT_serial.write(b'1') # STOP bit
    BT_serial.write(b',')
    BT_serial.write(b'0') # HW flow control
    BT_serial.write(b'0x0D')
    BT_serial.write(b'0x0A')
    BT_ATZ()
    BT_Port_Speed_Set(9600)

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


def BT_ATZ() : # software reset
    BT_serial.write(b'a')
    BT_serial.write(b't')
    BT_serial.write(b'z')
    BT_serial.write(b'0x0D')
    BT_serial.write(b'0x0A')

def BT_Org_Init() :
    BT_STOP()
    BT_9600()
    BT_MODE()
    BT_921600()

def BT_Init() :
    Bluetooth_Init_Set()
    BT_Org_Init()

def BT_Tx_Byte(data) :
    BT_serial.write(str.encode(data))

def BT_Trans_UART_Until(cnt) :
    for loop_cnt in range (cnt) :
        BT_Tx_Byte(TX_Queue.get())

def BT_Rx_OP() :

    # read esd110 value 
    while BT_serial.inWaiting():

        BT_Raw_data = str(BT_serial.read()).strip()
        
        # print(data) # for debug

        BT_buf += BT_Raw_data # buffering
        BT_buf = BT_buf.replace("'", "")  # remove (') and (b) because data has (') and (b) like this b'10.55'
        BT_buf = BT_buf.replace("b", "")

        RX_Queue.put(BT_buf)
        RX_Queue_Idx = RX_Queue_Idx + 1

        BT_buf = ""





