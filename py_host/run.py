from spi import write_2bytes, gpio_close
import time
import requests

numServos = 5
refreshRate = 0.1
maxPacketRate = 0.05
packets = [-1]*numServos

def convert(response):
    values = response.split()
    res = []
    for value, servo in zip(values, range(numServos)):
        packet = int(value.strip())
        packet += (servo * (2**9))
        res.append(packet)

    return res

def setServo(indx, angle):
    packet = int(angle) + (2**9)*indx
    write_2bytes(packet)

def websync():
    response = requests.get('http://10.205.0.34:8000/raw_position').text.strip()
    data = convert(response)

    for packet, indx in zip(data, range(len(data))):
        if packets[indx] != packet:
	    print('Writing ' + str(packet))
            write_2bytes(packet)
            packets[indx] = packet
            time.sleep(maxPacketRate)

while(True):
    websync()
    time.sleep(refreshRate)
