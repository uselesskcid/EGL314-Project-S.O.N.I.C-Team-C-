import tkinter as tk
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(2,GPIO.OUT)

GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)

GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
            
def laseron():
    GPIO.output(3,GPIO.LOW)
    GPIO.output(2,GPIO.LOW)
    
    GPIO.output(20,GPIO.LOW)
    GPIO.output(21,GPIO.LOW)
    
    GPIO.output(19,GPIO.LOW)
    GPIO.output(26,GPIO.LOW)
    
    
    
        
def laseroff():
    GPIO.output(3,GPIO.HIGH)
    GPIO.output(2,GPIO.HIGH)
    
    GPIO.output(20,GPIO.HIGH)
    GPIO.output(21,GPIO.HIGH)
    
    GPIO.output(19,GPIO.HIGH)
    GPIO.output(26,GPIO.HIGH)

main = tk.Tk()
main.title("Laser Control")

laseron_label = tk.Label(main, text = "Laser", foreground = "purple", font=("Helvetica",20))
laseron_button = tk.Button(main, text = "Laser On",command = laseron, background = "green", foreground = "white", font= ("Helvetica", 20))
laserdown_button = tk.Button(main, text = "Laser Off", command = laseroff, background = "red",foreground = "white", font=("Helvetica",20))

laseron_label.grid(row = 0, column = 2)
laseron_button.grid(row = 1, column = 1)
laserdown_button.grid(row = 1, column = 3)

main.mainloop()

