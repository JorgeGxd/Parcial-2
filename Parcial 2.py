import pyfirmata, time

led1 = 13
led2 = 11
led3 = 9
led4 = 7
led5 = 5
led6 = 3

tarjeta = pyfirmata.Arduino("COM3")
time.sleep(2)
print("comunicacion con Arduino realizada")
tarjeta.analog[0].mode = pyfirmata.INPUT
tarjeta.digital[led1].mode = pyfirmata.OUTPUT
tarjeta.digital[led2].mode = pyfirmata.OUTPUT
tarjeta.digital[led3].mode = pyfirmata.OUTPUT
tarjeta.digital[led4].mode = pyfirmata.OUTPUT
tarjeta.digital[led5].mode = pyfirmata.OUTPUT
tarjeta.digital[led6].mode = pyfirmata.OUTPUT



iterator = pyfirmata.util.Iterator(tarjeta)
iterator.start()

while True:
        if tarjeta.analog[0].read() == None:
            pass
            
        else:
            ptmt = tarjeta.analog[0].read()
            print(f"visualizacion de los datos del  {ptmt} ")
            
            if ptmt >= 0 and ptmt <=1.00:
                
                tarjeta.digital[led1].write(1)
                tarjeta.digital[led2].write(1)
                tarjeta.digital[led3].write(1)
                tarjeta.pass_time(1)
                tarjeta.digital[led4].write(1)
                tarjeta.digital[led5].write(1)
                tarjeta.digital[led6].write(1)
                tarjeta.pass_time(2)
                tarjeta.digital[led1].write(0)
                tarjeta.digital[led2].write(0)
                tarjeta.digital[led3].write(0)
                tarjeta.pass_time(1)
                tarjeta.digital[led4].write(0)
                tarjeta.digital[led5].write(0)
                tarjeta.digital[led6].write(0)
                tarjeta.pass_time(2)
                  
            