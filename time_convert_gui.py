#This is a time converter GUI application.
#A user can input seconds (as an integer) and the application
#outputs the corresponding conversion in hours, minutes and seconds

from tkinter import *

# Create a GUI window 
window = Tk() 
   
# Function to convert user inputted seconds into seconds, minutes, hours

def convert_from_seconds():

    seconds = int(e2_value.get())
      
    # 
    seconds = seconds%(24*3600)
      
    # 
    hour = seconds//3600
      
    #  
    seconds %= 3600

    #
    minutes = seconds//60

    #
    seconds %=60
      
    # Enters the converted time to  
    # the relevant text widget 
    t1.delete("1.0", END) 
    t1.insert(END,hour) 
      
    t2.delete("1.0", END) 
    t2.insert(END,minutes) 
      
    t3.delete("1.0", END) 
    t3.insert(END,seconds) 
  
# Label Widgets 
e1 = Label(window, text = "Enter the time in seconds") 
e2_value = StringVar() 
e2 = Entry(window, textvariable = e2_value) 
e3 = Label(window, text = 'Hours') 
e4 = Label(window, text = 'Minutes') 
e5 = Label(window, text = 'Seconds') 
  
# Text Widgets
t1 = Text(window, height = 1, width = 20) 
t2 = Text(window, height = 1, width = 20) 
t3 = Text(window, height = 1, width = 20) 
  
# Button Widgets
b1 = Button(window, text = "Convert", command = convert_from_seconds) 
  
# Placing widgets in rows and columns 

e1.grid(row = 0, column = 0) 
e2.grid(row = 0, column = 1) 
e3.grid(row = 1, column = 0) 
e4.grid(row = 1, column = 1) 
e5.grid(row = 1, column = 2) 
t1.grid(row = 2, column = 0) 
t2.grid(row = 2, column = 1) 
t3.grid(row = 2, column = 2) 
b1.grid(row = 0, column = 2) 
  
# GUI start-up 
window.mainloop() 
