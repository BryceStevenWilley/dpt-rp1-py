import serial
from subprocess import Popen, PIPE

ser = serial.Serial('/dev/ttyACM0')
print('Sending bytestring to ' + str(ser.name))
ser.write(b"\x01\x00\x00\x01\x00\x00\x00\x01\x00\x04")
ser.close()

# TODO run dmesg and avahi-resolve -n and print out what to use for the address.
process = Popen(['avahi-resolve', '-n', 'digitalpaper.local'], stdout=PIPE)
(output, err) = process.communicate()
exit_code = process.wait()

process2 = Popen(['dmesg'], stdout=PIPE)
process3 = Popen(['tail', '-n', '2'], stdin=process2.stdout, stdout=PIPE)
(output3, err3) = process3.communicate()
print(output)
print(output3)

