#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pafy
import cv2
import numpy as np

# määritellään torikameran url
url = "https://www.youtube.com/watch?v=yA4aFD0AjDs"
video = pafy.new(url)
# haetaan paras laatu
best = video.getbest(preftype="mp4")
# napataan videokuva url-osoitteesta
capture = cv2.VideoCapture(best.url)
# videokoodekki
video_cod = cv2.VideoWriter_fourcc(*'XVID')
# määritellään ulostulo, johon video striimataan
video_output= cv2.VideoWriter('captured_video.avi',video_cod,10,(640,480))

# loopataan, kunnes keskeytetään tai videokuvaa ei löydy
while (True):
    _, frame = capture.read()
    # muutetaan brg rgb:ksi
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # määritellään oranssin värialue
    light_orange = np.array([(10, 100, 20)])
    dark_orange = np.array([(25, 255, 255)])
    # rajataan kuvaa näyttämään vain oranssit värialueet
    mask = cv2.inRange(hsv, light_orange, dark_orange)
    # lyödään maskaus alkuperäisen kuvan päälle
    output = cv2.bitwise_and(frame, frame, mask=mask)
    # kirjoitetaan kuva tiedostoon
    video_output.write(output)
    # näytetään kuva
    cv2.imshow('output', output)
    # paina Q lopettaaksesi videon
    if cv2.waitKey(1) & 0xFF == ord('Q'):
        break


# suljetaan capture ja video_output
capture.release()
video_output.release()
cv2.destroyAllWindows()

print("Video tallennettiin onnistuneesti")   


# In[3]:





# In[ ]:




