# Include the library filese
import I2C_LCD_driver
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep
import json

#Include the buzzer pin
buzzer = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(buzzer,GPIO.OUT)

# Create a object for the LCD
lcd = I2C_LCD_driver.lcd()

def write():
        reader = SimpleMFRC522()

        try:
                text = input('New data: ')
                print("Now place your tag to write")    
                lcd.lcd_display_string("Place your Tag",1,1)    
                lcd.lcd_display_string("Type new data",2,1)                                            
                reader.write(text)
                print("Written")                    
                
        
                GPIO.output(buzzer,GPIO.HIGH)
                sleep(0.5)
                GPIO.output(buzzer,GPIO.LOW)

        finally:
                GPIO.cleanup()
        
        
def read():
        scan = SimpleMFRC522()
        try:
                print("Now place your Tag to scan")      
                lcd.lcd_display_string("Place your Tag",1,1)                                               
                scan.write("Tag ID")
                id,Tag = scan.read()                    
                print("Your Tag ID is : " + str(id))
                lcd.lcd_clear()
                lcd.lcd_display_string("Tag ID",1,5)
                lcd.lcd_display_string(str(id),2,1)
        
                GPIO.output(buzzer,GPIO.HIGH)
                sleep(0.5)
                GPIO.output(buzzer,GPIO.LOW)

        finally:
                GPIO.cleanup()
        
        
def rfiddump():
        print("Now place your tag ")    
        lcd.lcd_display_string("Place your Tag",1,1)   
        scan.write("Tag ID") 
        id,Tag = scan.read()
        lcd.lcd_display_string("Data stored",2,1)
        scan = SimpleMFRC522()
        auth = {}
        with open("auth.json") as file: 
                auth = json.load(file)
        auth.update({id:Tag})
        with open("auth.json", "w") as file:
                json.dump(auth,file) 
