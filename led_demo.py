import RPi.GPIO
import time
#RPi.GPIO.cleanup()
RPi.GPIO.setmode(RPi.GPIO.BCM)
VCC=2
D1=3
D2=18
D3=23
D4=24
LED_A = 25
LED_B = 8
LED_C = 7
LED_D = 12
LED_E = 16
LED_F = 20
LED_G = 21
LED_DP = 26

RPi.GPIO.setup(VCC, RPi.GPIO.OUT)
RPi.GPIO.setup(D1, RPi.GPIO.OUT)
RPi.GPIO.setup(D2, RPi.GPIO.OUT)
RPi.GPIO.setup(D3, RPi.GPIO.OUT)
RPi.GPIO.setup(D4, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_A, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_B, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_C, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_D, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_E, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_F, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_G, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_DP, RPi.GPIO.OUT)

def select( ):
    RPi.GPIO.output(LED_A, True)
    RPi.GPIO.output(LED_B, True)
    RPi.GPIO.output(LED_C, True)
    RPi.GPIO.output(LED_D, True)
    RPi.GPIO.output(LED_E, True)
    RPi.GPIO.output(LED_F, True)
    RPi.GPIO.output(LED_G, True)
    RPi.GPIO.output(LED_DP, True)
    return 0


def c():
    #
    RPi.GPIO.output(VCC, True)
    RPi.GPIO.output(D1, True)
    RPi.GPIO.output(D2, True)
    RPi.GPIO.output(D3, True)
    RPi.GPIO.output(D4, True)
    
    for n in range(0,8000):
        #7
        RPi.GPIO.output(LED_A, False)
        RPi.GPIO.output(LED_B, False)
        RPi.GPIO.output(LED_C, False)
        #7
        RPi.GPIO.output(D1,False)
        time.sleep(0.0001)
        RPi.GPIO.output(D1,True)#OPEN D1
        time.sleep(0.0001)
        
        select()
        RPi.GPIO.output(LED_A, False)
        RPi.GPIO.output(LED_E, False)
        RPi.GPIO.output(LED_G, False)
        RPi.GPIO.output(LED_B, False)
        RPi.GPIO.output(LED_D, False)
        RPi.GPIO.output(LED_F, False)
        RPi.GPIO.output(LED_C, False)
        RPi.GPIO.output(D2,False)
        time.sleep(0.0001)
        RPi.GPIO.output(D2,True)#OPEN D1
        time.sleep(0.0001)
        
        select()
        RPi.GPIO.output(LED_C, False)
        RPi.GPIO.output(LED_B, False)
        RPi.GPIO.output(D3,False)
        time.sleep(0.0001)
        RPi.GPIO.output(D3,True)#OPEN D1
        time.sleep(0.0001)
        
        
        select()
        RPi.GPIO.output(LED_A, False)
        RPi.GPIO.output(LED_B, False)
        RPi.GPIO.output(LED_G, False)
        RPi.GPIO.output(LED_E, False)
        RPi.GPIO.output(LED_D, False)
        RPi.GPIO.output(D4,False)
        time.sleep(0.0001)
        RPi.GPIO.output(D4,True)#OPEN D4
        time.sleep(0.0001)
        select()
        RPi.GPIO.output(D1, True)
        RPi.GPIO.output(D2, True)
        RPi.GPIO.output(D3, True)
        RPi.GPIO.output(D4, True)
        
        
    return 0

select()
c()
RPi.GPIO.cleanup()
    



    

