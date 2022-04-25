#Importtación librerias 
import pyfirmata, time
#Variables de LED
led1 = 13
led2 = 11
led3 = 9
led4 = 7
led5 = 5
led6 = 3

#comunicación tarjeta y Python
tarjeta = pyfirmata.Arduino("COM3")
time.sleep(2)
print("comunicacion con Arduino realizada")  #Estado en el que estan los dispositivos conectados a Arduino 
tarjeta.analog[0].mode = pyfirmata.INPUT
tarjeta.digital[led1].mode = pyfirmata.OUTPUT  
tarjeta.digital[led2].mode = pyfirmata.OUTPUT
tarjeta.digital[led3].mode = pyfirmata.OUTPUT
tarjeta.digital[led4].mode = pyfirmata.OUTPUT
tarjeta.digital[led5].mode = pyfirmata.OUTPUT
tarjeta.digital[led6].mode = pyfirmata.OUTPUT


#Comienzo de las iteraciones 
iterator = pyfirmata.util.Iterator(tarjeta)
iterator.start()

while True:
        if tarjeta.analog[0].read() == None:
            pass                #Ignora el error cuando no reconoce el Pin
            
        else:        
            ptmt = tarjeta.analog[0].read()
            print(f"visualizacion de los datos del  {ptmt} ")  #ptmt variable para leer los datos del potenciometro 
            
            if ptmt >= 0 and ptmt <=0.16:
                print(f"Se encendió led verde ")  
                tarjeta.digital[led1].write(1) 
                tarjeta.digital[led2].write(0)
                tarjeta.digital[led3].write(0)
                tarjeta.digital[led4].write(0)
                tarjeta.digital[led5].write(0)
                tarjeta.digital[led6].write(0)
                                   
            if ptmt >= 0.161 and ptmt <=0.32:
                print(f"Se encendió led amarillo ") 
                tarjeta.digital[led1].write(0)
                tarjeta.digital[led2].write(1)
                tarjeta.digital[led3].write(0)
                tarjeta.digital[led4].write(0)
                tarjeta.digital[led5].write(0)
                tarjeta.digital[led6].write(0)
               
                           
            if ptmt >= 0.321 and ptmt <=0.48:
                print(f"Se encendió led rojo ") 
                tarjeta.digital[led1].write(0)
                tarjeta.digital[led2].write(0)
                tarjeta.digital[led3].write(1)
                tarjeta.digital[led4].write(0)
                tarjeta.digital[led5].write(0)
                tarjeta.digital[led6].write(0)
                
                            
            if ptmt >= 0.481 and ptmt <=0.64:
                print(f"Se encendió led verde ")     
                tarjeta.digital[led1].write(0)
                tarjeta.digital[led2].write(0)
                tarjeta.digital[led3].write(0)
                tarjeta.digital[led4].write(1)
                tarjeta.digital[led5].write(0)
                tarjeta.digital[led6].write(0)
                
            if ptmt >= 0.641 and ptmt <=0.80:
                print(f"Se encendió led amarillo ")    
                tarjeta.digital[led1].write(0)
                tarjeta.digital[led2].write(0)
                tarjeta.digital[led3].write(0)
                tarjeta.digital[led4].write(0)
                tarjeta.digital[led5].write(1)
                tarjeta.digital[led6].write(0)
                
            if ptmt >= 0.810 and ptmt <=1.00:
                print(f"Se encendió led rojo ")     
                tarjeta.digital[led1].write(0)
                tarjeta.digital[led2].write(0)
                tarjeta.digital[led3].write(0)
                tarjeta.digital[led4].write(0)
                tarjeta.digital[led5].write(0)
                tarjeta.digital[led6].write(1)

        tarjeta.pass_time(1)
                
        
                
            