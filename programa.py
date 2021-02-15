import webbrowser
import os
import tkinter.filedialog as tkFileDialog
import tkinter.messagebox as tkMessageBox
import time

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import programa_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    programa_support.set_Tk_var()
    top = Toplevel1 (root)
    programa_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    programa_support.set_Tk_var()
    top = Toplevel1 (w)
    programa_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family {Segoe UI} -size 24 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 12 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 14 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("600x450+345+68")
        top.minsize(116, 1)
        top.maxsize(1284, 702)
        top.resizable(1, 1)
        top.title("Interface Simulação 3D")
        top.configure(background="#f3f3f3")

        self.btnAjuda = tk.Button(top)
        self.btnAjuda.place(relx=0.133, rely=0.511, height=94, width=127)
        self.btnAjuda.configure(activebackground="#ececec")
        self.btnAjuda.configure(activeforeground="#000000")
        self.btnAjuda.configure(background="#2452f0")
        self.btnAjuda.configure(disabledforeground="#a3a3a3")
        self.btnAjuda.configure(font=font13)
        self.btnAjuda.configure(foreground="#ffffff")
        self.btnAjuda.configure(highlightbackground="#d9d9d9")
        self.btnAjuda.configure(highlightcolor="black")
        self.btnAjuda.configure(pady="0")
        self.btnAjuda.configure(text='''Ajuda''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.133, rely=0.311,height=30, relwidth=0.64)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Courier New} -size 10")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(textvariable=programa_support.diretorio)

        self.btnSimular = tk.Button(top)
        self.btnSimular.place(relx=0.35, rely=0.511, height=94, width=127)
        self.btnSimular.configure(activebackground="#ececec")
        self.btnSimular.configure(activeforeground="#000000")
        self.btnSimular.configure(background="#18a005")
        self.btnSimular.configure(disabledforeground="#a3a3a3")
        self.btnSimular.configure(font=font13)
        self.btnSimular.configure(foreground="#ffffff")
        self.btnSimular.configure(highlightbackground="#d9d9d9")
        self.btnSimular.configure(highlightcolor="black")
        self.btnSimular.configure(pady="0")
        self.btnSimular.configure(text='''Gerar''')

        self.btnYoutube = tk.Button(top)
        self.btnYoutube.place(relx=0.567, rely=0.511, height=94, width=127)
        self.btnYoutube.configure(activebackground="#ececec")
        self.btnYoutube.configure(activeforeground="#000000")
        self.btnYoutube.configure(background="#d70005")
        self.btnYoutube.configure(disabledforeground="#a3a3a3")
        self.btnYoutube.configure(font=font13)
        self.btnYoutube.configure(foreground="#ffffff")
        self.btnYoutube.configure(highlightbackground="#d9d9d9")
        self.btnYoutube.configure(highlightcolor="black")
        self.btnYoutube.configure(pady="0")
        self.btnYoutube.configure(text='''Youtube''')

        self.btnBuscar = tk.Button(top)
        self.btnBuscar.place(relx=0.817, rely=0.267, height=64, width=67)
        self.btnBuscar.configure(activebackground="#ececec")
        self.btnBuscar.configure(activeforeground="#000000")
        self.btnBuscar.configure(background="#f2f746")
        self.btnBuscar.configure(disabledforeground="#a3a3a3")
        self.btnBuscar.configure(font=font12)
        self.btnBuscar.configure(foreground="#000000")
        self.btnBuscar.configure(highlightbackground="#d9d9d9")
        self.btnBuscar.configure(highlightcolor="black")
        self.btnBuscar.configure(pady="0")
        self.btnBuscar.configure(text='''Buscar''')

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.0, rely=0.067, height=61, width=604)
        self.Label1.configure(background="#2c2c2c")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Interface de Simulação 3D''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.15, rely=0.911, height=21, width=414)
        self.Label2.configure(background="#f3f3f3")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font13)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Desenvolvido por Pedro Henrique de Jesus''')

        self.Label2_6 = tk.Label(top)
        self.Label2_6.place(relx=0.367, rely=0.244, height=21, width=94)
        self.Label2_6.configure(activebackground="#f9f9f9")
        self.Label2_6.configure(activeforeground="black")
        self.Label2_6.configure(background="#f3f3f3")
        self.Label2_6.configure(disabledforeground="#a3a3a3")
        self.Label2_6.configure(font="-family {Segoe UI} -size 12")
        self.Label2_6.configure(foreground="#000000")
        self.Label2_6.configure(highlightbackground="#d9d9d9")
        self.Label2_6.configure(highlightcolor="black")
        self.Label2_6.configure(text='''Arquivo NXC''')
        self.iniciar()

    def iniciar(self):
        self.dir=""
        self.btnBuscar.configure(command=self.buscarDiretorio)
        self.btnSimular.configure(command=self.simular)
        self.btnAjuda.configure(command=self.ajuda)
        self.btnYoutube.configure(command=self.youtube)
    def ajuda(self):
        webbrowser.open('https://www.youtube.com/channel/UCDsIP5sZpB0q28TYk3m-V-w')
    def youtube(self):
        webbrowser.open('https://www.youtube.com/channel/UCDsIP5sZpB0q28TYk3m-V-w')

    def simular(self):
        f = open(self.dir, "r")
        d = "import vrep\nfrom pedrohj import *\narduino = objeto()\nmotor1 = arduino.obter('DynamicLeftJoint')\nmotor2 = arduino.obter('DynamicRightJoint')\nS4 = arduino.obter('sensorUS')\n"
        i = 0  # Contador de linhas
        loopAqui = 0
        # Ler
        for x in f:

            if x.find("task main") != -1:
                loopAqui = 1

            if loopAqui == 1:
                if x.find("if") != -1:
                    x = x.replace(")", "):")

                if x.find("for") != -1:
                    g = x.split(";")  # Achar os três trechos do FOR
                    g = g[1].split("<")  # achar o numero  do contador FOR
                    x = x.replace(x[x.find("for"):len(x)], "for i in range(" + str(g[1]) + "):\n")

                d = d + x
            i = i + 1


        d = d.replace("SetSensor(S4, SENSOR_LOWSPEED)", " ")
        d = d.replace("SensorUS(S4)", "arduino.lerUltrassonico(S4)")
        d = d.replace("arduino.lerUltrassonico(S4):", "arduino.lerUltrassonico(S4)")
        d = d.replace("task main()", "if True:")
        d = d.replace("} else {", "else:")
        d = d.replace("{", " ")
        d = d.replace("}", " ")
        d = d.replace(";", " ")
        d = d.replace("Wait", "arduino.delay")
        d = d.replace("while ( true )", "while True:\n        arduino.rodar()")
        d = d.replace("RotateMotorEx", "arduino.RotateMotorEx")
        d = d.replace("SteerDriveEx", "arduino.SteerDriveEx")
        # d=d.replace("___", "   ")
        d = d.replace("OUT_BC", "motor1,motor2")
        d = d.replace("OUT_B", "motor1")
        d = d.replace("OUT_C", "motor2")
        d = d.replace("MAX", "max")
        d = d.replace("MIN", "min")
        d = d.replace("WHEELDIAMETER", "5.6")
        d = d.replace("TRACKWIDTH", "12")
        d = d.replace("PI", "3.14")
        d = d.replace("true", "True")
        d = d.replace("false", "False")
        d = d.replace("Off", "arduino.Off")
        d = d.replace("TextOut", "arduino.TextOut")
        d = d.replace("NumOut",  "arduino.TextOut")
        d = d.replace("maxLINES", "8")
        d = d.replace("&&", " and ")
        d = d.replace("||", " or ")








        d=d+"\narduino.velocidade(motor1,0)\narduino.velocidade(motor2,0)\narduino.parar()\n#Gerado por Pedro H.J visite o canal Teoria na Pratica com Pedro\n"
        print(d)
        # Python file
        p = open("main.py", "w")
        p.write(d)
        p.close()
        tkMessageBox.showinfo('Mensagem', "Gerado com sucesso")


    def buscarDiretorio(self):
        file_path = tkFileDialog.askopenfilename()  # Diretório e arquivo
        programa_support.diretorio.set(file_path)
        self.dir=file_path
if __name__ == '__main__':
    vp_start_gui()





