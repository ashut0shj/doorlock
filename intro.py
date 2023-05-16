import rw
import I2C_LCD_driver
lcd = I2C_LCD_driver.lcd()
lcd.lcd_display_string("Welcome to Braims",1,0)
def mainscreen():
    a='''Welcome to BRAIMS' DNP project

    1> Deploy Door_Lock_System
    2>Add RFID Tag in database
    3>Read Data in RFID
    4>Write Data in RFID'''
    print(a)


    c=int(input("enter your choice : "))
    if c==1:
        import Door_lock_system
    elif c==2:
        rw.rfiddump()
    elif c==3:
        rw.read()
    elif c==4:
        rw.write()
x='y'
while(x=='y' or x=='Y' or x==1):
    mainscreen()
    x= input("Do you want move further with the words and generate hints? (y/n)")
    
    