from spi import write_2bytes, gpio_close
import time

numServos = 5

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
    data = convert(testResponse)
    for packet, indx in zip(data, range(len(data))):
        print("Writing packet ", str(packet))
        if packets[indx] != packet:
            write_2bytes(packet)
            packets[indx] = packet
            time.sleep(0.3)
    #time.sleep(10)
    gpio_close()

def setAll(angle):
    for i in range(numServos):
        setServo(i, angle)
        time.sleep(0.3)
