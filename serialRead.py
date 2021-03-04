from serial import Serial
import binascii

serial = Serial("COM3", 115200)

while True:
    value = serial.read(1).hex()
    print(value ," | " ,int(value, 16))