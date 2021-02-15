
# **********************************************************
#
# Autor: Pedro Henrique de Jesus 
# Classe para manipular objetos no VREP de maneira simples.
# Data: 21/12/2020
# 
# Se for utilizar no youtube, 
# mencione o link do canal, por favor.
# **********************************************************

import time
import vrep

class objeto:

    def __init__(self):
        self.tempo=10
        print('Programa VREP iniciou a simulação')
        #vrep.simxFinish(-1)
        self.cliente = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)  # Connect to V-REP

        vrep.simxSynchronous(self.cliente, True)
        vrep.simxStartSimulation(self.cliente, vrep.simx_opmode_blocking)

    def rodar(self):
        vrep.simxSynchronousTrigger(self.cliente)

    def obter(self,nome):
        errorCode, obj = vrep.simxGetObjectHandle(self.cliente, str(nome), vrep.simx_opmode_oneshot_wait)
        return obj

    def velocidade(self,objeto,valor):
        vrep.simxSetJointTargetVelocity(self.cliente, objeto, float(valor/57.2958), vrep.simx_opmode_streaming)

    def Off(self, objeto1, objeto2):
        vrep.simxSetJointTargetVelocity(self.cliente, objeto1, 0, vrep.simx_opmode_streaming)
        vrep.simxSetJointTargetVelocity(self.cliente, objeto2, 0, vrep.simx_opmode_streaming)

    def RotateMotorEx(self,objeto1,objeto2,valor,dist,dir,nop1,nop2):
        # RotateMotorEx('OUT_BC', MIN(MAX(30, -100), 100), (20 * 360 / (PI * WHEELDIAMETER)), 0, true, true)

        # Dir=0 é pra ir pra frente
        if dir==0:
            vrep.simxSetJointTargetVelocity(self.cliente, objeto1, 14*float(valor/57.2958)/2, vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetVelocity(self.cliente, objeto2, 14*float(valor / 57.2958)/2, vrep.simx_opmode_streaming)
            self.delay(  2*abs((1000*dist/409.4631483166515)/(valor/30)) )

        if dir==100:
            vrep.simxSetJointTargetVelocity(self.cliente, objeto1, -14*float(valor / 57.2958)/2, vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetVelocity(self.cliente, objeto2, 14*float(valor / 57.2958)/2, vrep.simx_opmode_streaming)
            self.delay(  2*abs((1000*dist/409.4631483166515)/(valor/30)) )
            
        if dir==-100:
            
            vrep.simxSetJointTargetVelocity(self.cliente, objeto1, 14*float(valor/57.2958)/2, vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetVelocity(self.cliente, objeto2, -14*float(valor / 57.2958)/2, vrep.simx_opmode_streaming)
            self.delay(  2*abs((1000*dist/409.4631483166515)/(valor/30)) )

    def SteerDriveEx(self, objeto1, objeto2, valor1, valor2, dirFrente, dist):
        # SteerDriveEx(OUT_C, OUT_B, MIN(MAX(10, -100), 100), MIN(MAX(30, -100), 100), true, 20)
        if dirFrente == True:
            vrep.simxSetJointTargetVelocity(self.cliente, objeto1, 14 * float(valor1 / 57.2958) / 2,
                                            vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetVelocity(self.cliente, objeto2, 14 * float(valor2 / 57.2958) / 2,
                                            vrep.simx_opmode_streaming)
            self.delay(10 * abs((1000 * dist / 409.4631483166515) / 1))
        if dirFrente == False:
            vrep.simxSetJointTargetVelocity(self.cliente, objeto1, -14 * float(valor1 / 57.2958) / 2,
                                            vrep.simx_opmode_streaming)
            vrep.simxSetJointTargetVelocity(self.cliente, objeto2, -14 * float(valor2 / 57.2958) / 2,
                                            vrep.simx_opmode_streaming)
            self.delay(10 * abs((1000 * dist / 409.4631483166515) / 1))

    def analogWrite(self,objeto,valor):
        vrep.simxSetJointTargetVelocity(self.cliente, objeto, float(valor/57.2958), vrep.simx_opmode_streaming)



    def setPos(self,objeto,valor):
        vrep.simxSetJointTargetPosition(self.cliente, objeto, float(valor/57.2958), vrep.simx_opmode_oneshot_wait)


    def obterPosX(self,c):
        pos = vrep.simxGetObjectPosition(self.cliente, c, -1, vrep.simx_opmode_streaming)
        return pos[1][0]
        #print(pos[1][0])

    def obterPosY(self,c):
        pos = vrep.simxGetObjectPosition(self.cliente, c, -1, vrep.simx_opmode_streaming)
        return pos[1][1]
        #print(pos[1][1])

    def obterPosZ(self,c):
        pos = vrep.simxGetObjectPosition(self.cliente, c, -1, vrep.simx_opmode_streaming)
        return pos[1][2]
        #print(pos[1][2])


    def obterVelocidade(self,corpo):
        angVel = vrep.simxGetObjectVelocity(self.cliente, corpo, vrep.simx_opmode_streaming)
        print(angVel)
        return angVel[1]

    def digitalRead(self,corpo):
        x=vrep.simxReadVisionSensor(self.cliente, corpo, vrep.simx_opmode_streaming)
        return x[1]

    def lerSensor(self,corpo):
        x=vrep.simxReadVisionSensor(self.cliente, corpo, vrep.simx_opmode_streaming)
        return x[1]
    def lerUltrassonico(self,nome):
        a,b,c,d,e=vrep.simxReadProximitySensor(self.cliente, nome, vrep.simx_opmode_streaming)
        if c[2]<0:
            return 10000
        return float(c[2]*100)

    def delay(self,t):
        tempo=int(t/self.tempo)
        for i in range(tempo):
            vrep.simxSynchronousTrigger(self.cliente)
    def parar(self):
        vrep.simxPauseSimulation(self.cliente, vrep.simx_opmode_oneshot)

    def TextOut(self,nop1,nop2,texto):
        print(  str(texto) )

