import serial
import time

global GPS_serial
global GPS_buf
global GPS_Raw_data

GPS_Buf = ''
GPS_DATA = ''
tmp = ''

def GPS_Init_Set() :
    GPS_serial = serial.Serial('/dev/ttyAMA0', 9600, parity='N', timeout=0.001)  # when connect to GPIO pins

    GPS_serial.isOpen()

    if GPS_serial.isOpen() == True:
        print("GPS connected")
    else:
        print("[GPS_Error] GPS not connected")


def GPS_Op() :
    while GPS_serial.in_waiting:
        GPS_Raw_data = str(GPS_serial.read()).strip()

        GPS_Buf += GPS_Raw_data
        GPS_Buf = GPS_Buf.replace("'", "")
        GPS_Buf = GPS_Buf.replace("b", "")

        # $GPGGA,,,,,,0,00,,,M,0.0,M,,0000*48\r\n

        GPS_DATA += GPS_Buf

        # print(GPS_DATA)

        if GPS_DATA[0:5] == 'GPGGA' and GPS_Buf == '$':
            tmp += GPS_DATA[:-1]
            print(tmp)
            GPS_DATA = ''
            tmp = ''

        if GPS_DATA[0:6] != '$GPGGA' and BT_Buf == '$':
            GPS_DATA = ''
            tmp = ''

        BT_Buf = ''

        '''
        if GPS_Raw_data[0:6] == '$GPGGA': # gpgga 형식 처리
            # $GPGGA,202530.00,5109.0262,N,11401.8407,W,5,40,0.5,1097.36,M,-17.00,M,18,TSTR*61
            (header, utc, latitude, lat_dir, longitude, long_dir, quality, sats, hdop, alt, 
             a_units, undulation, u_units, age, stn_ID, Check_sum) = map(float, GPS_buf[1:-4].split(','))
            #print(latitude, lat_dir, longitude, long_dir) # for debug

        #else : 
            #print("[GPS_Error] satilite not connected")
        '''
    





