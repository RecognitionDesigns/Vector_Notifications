#!/usr/bin/env python3

import http.client, urllib
import anki_vector
from anki_vector.util import degrees, Angle, Pose
import time
import requests
from key import (token, user)
from serial import (<ROBOT NAME HERE>)

n = 0

def count(n):
    while n < 5:
        if robot.status.is_picked_up or robot.status.is_cliff_detected:
            print("Vector might be stuck!")
            print(n)
            n = n+1        
            time.sleep(3)
            
        else:
            n = 0
            time.sleep(2)
            
    print("Vector is stuck!")
    
    image = robot.camera.capture_single_image()
 
    image.raw_image.save('stuck_pic.jpeg', 'JPEG')
    
    alert_message = ("Vector is stuck!")
    
    r = requests.post("https://api.pushover.net/1/messages.json", data = {
      "token": token,
      "user": user,
      "message": (alert_message)
    },
    files = {
      "attachment": ("image.jpg", open("stuck_pic.jpeg", "rb"), "image/jpeg")
    })
    print("Sending alert...")
    
    n = 0
    
    while True:
        time.sleep(10)
        if robot.status.is_picked_up or robot.status.is_cliff_detected:
            time.sleep(1)    
        else:
            count(n)

with anki_vector.Robot(<ROBOT NAME HERE>) as robot:
    robot.conn.release_control()
    count(n)
