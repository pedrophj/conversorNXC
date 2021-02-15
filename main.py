import vrep
from pedrohj import *
arduino = objeto()
motor1 = arduino.obter('DynamicLeftJoint')
motor2 = arduino.obter('DynamicRightJoint')
S4 = arduino.obter('sensorUS')
if True:  
    arduino.RotateMotorEx(motor1,motor2, min(max(30, -100), 100), (20 * 360 / (3.14 * 5.6)), 0, True, True) 
    arduino.delay(1) 
    arduino.RotateMotorEx(motor1,motor2, min(max(30, -100), 100), (90 * 12 / 5.6), 100, True, True) 
    arduino.delay(1) 
    arduino.RotateMotorEx(motor1,motor2, min(max(30, -100), 100), (20 * 360 / (3.14 * 5.6)), 0, True, True) 
    arduino.delay(1) 
    arduino.RotateMotorEx(motor1,motor2, min(max(30, -100), 100), (90 * 12 / 5.6), -100, True, True) 
    arduino.delay(1) 
    arduino.RotateMotorEx(motor1,motor2, min(max(30, -100), 100), (20 * 360 / (3.14 * 5.6)), 0, True, True) 
    arduino.delay(1) 
 

arduino.velocidade(motor1,0)
arduino.velocidade(motor2,0)
arduino.parar()
#Gerado por Pedro H.J visite o canal Teoria na Pratica com Pedro
