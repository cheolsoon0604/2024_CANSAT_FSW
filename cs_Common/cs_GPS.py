import serial
import time

global GPS_serial
global GPS_buf

def GPS_Init_Set() :
    GPS_serial = serial.Serial('/dev/ttyAMA0', 9600, parity='N', timeout=0.001)  # when connect to GPIO pins

    GPS_serial.isOpen()

    if GPS_serial.isOpen() == True:
        print("GPS connected")
    else:
        print("[GPS_Error] GPS not connected")

    GPS_buf = ""

def GPS_Op() :
    while GPS_serial.inWaiting():

        GPS_Raw_data = str(GPS_serial.read()).strip()

        GPS_buf += GPS_Raw_data # buffering
        #print(GPS_Raw_data) # for debug

        GPS_buf = GPS_buf.replace("'","") # remove (') and (b) because data has (') and (b) like this b'10.55' -> 10.55
        GPS_buf = GPS_buf.replace("b","") 

        print(GPS_buf) # for debug 

        if GPS_Raw_data[0:6] == '$GPGGA': # gpgga 형식 처리
            # $GPGGA,202530.00,5109.0262,N,11401.8407,W,5,40,0.5,1097.36,M,-17.00,M,18,TSTR*61
            (header, utc, latitude, lat_dir, longitude, long_dir, quality, sats, hdop, alt, 
             a_units, undulation, u_units, age, stn_ID, Check_sum) = map(float, GPS_buf[1:-4].split(','))
            #print(latitude, lat_dir, longitude, long_dir) # for debug

        #else : 
            #print("[GPS_Error] satilite not connected")

        GPS_buf = ""
    





