import serial

ser = serial.Serial('/dev/ttyACM0')
print('Sending bytestring to ' + str(ser.name))
ser.write(b"\x01\x00\x00\x01\x00\x00\x00\x01\x00\x04")
ser.close()

