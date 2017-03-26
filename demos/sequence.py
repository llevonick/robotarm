import time
import requests

def run(servos, angles):
  for servo, angle in zip(servos, angles):
    requests.get('http://10.205.0.34:8000/set_servo?servo=' + str(servo) + '&angle=' + str(angle))

def sequence(angleSeq):
    for angles in angleSeq:
        run([0,1,2,3,4], angles)
        time.sleep(0.2)
