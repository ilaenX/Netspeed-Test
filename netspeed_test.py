'''
 FILE:     netspeed_test_ui.py
 AUTHOR:   Daniel Adeyelu
 CREATED:  December 24, 2022
 UPDATED:  December 25, 2022
 DESCRIPTION:
   This python script will outputs the network speed
'''

# Import modules and packages 
from tkinter import *
from speedtest import Speedtest, SpeedtestResults
import sys
import math


# Creation OF Function
# def get_ping(value):
#     dictionary = SpeedtestResults().dict()
#     for key in dictionary.items():
#         if key == value:
#             return key

def update_text(_event=None):
    Kbps_to_Mbps = math.pow(10,6)
    speed_test = Speedtest()
    downloadload = speed_test.download()
    upload = speed_test.upload()
    downloadload_speed = round(downloadload / Kbps_to_Mbps, 2)
    upload_speed = round(upload / Kbps_to_Mbps, 2)
    download_output.config(text= "{} Mbps".format(downloadload_speed))
    upload_output.config(text= "{} Mbps".format(upload_speed))

def exit_button(_event=None):
    sys.exit()

def clear_button(_event=None):
    download_output.config(text="")
    upload_output.config(text="")

# Window properties
window = Tk()
window.title("Network Speed Test")
window.geometry('420x250+250+150')

# Row 0 Widget
download_label = Label(window, text="Download Speed: ")
download_label.grid(row=0,column=0)
download_output = Label(window, relief=SUNKEN, width=20)
download_output.grid(row=0,column=1)

# Row 1 Widget
upload_label = Label(window, text="Upload Speed: ")
upload_label.grid(row=1,column=0)
upload_output = Label(window, relief=SUNKEN, width=20)
upload_output.grid(row=1,column=1)

# Row 2 Widget
# ping = get_ping('ping')
# pings_label = Label(window, text="Ping: {} ms".format(ping))
# pings_label.grid(row=2, column=0)
# # server_label = Label(window, text="Server: {}".format(Speedtest.server()))

# Row 3 Widget
clear_button = Button(window, text="Clear", command=clear_button)
clear_button.grid(row=3, column=0)

button = Button(window, text="Check Speed", command=update_text, background = '#49A')
button.grid(row=3, column=1)

exit_button = Button(window, command=exit_button, text="Exit")
exit_button.grid(row=3, column=2)

# Assign weight values to each row in the grid so that they evenly distribute through the application.
for row_index in range(4):
    window.rowconfigure(row_index, weight = 1)
# Assign weight values for each column for the same reason.
for column_index in range(2):
    window.columnconfigure(column_index, weight = 1)

# Add hotkey support for the three main buttons.
window.bind("<Alt-c>", clear_button)
window.bind("<Return>", update_text)
window.bind("<Enter>", update_text)
window.bind("<Escape>", exit_button)

# Closing of GUI
window.mainloop()