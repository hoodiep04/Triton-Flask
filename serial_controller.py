import serial
import serial.tools.list_ports 

class Controller():
    def __init__(self, typeof_mc):
        if typeof_mc.lower() == 'pressure':
            self.typeof_mc = 'P'
        
        else:
            self.typeof_mc = 'V'
            self.valve1state = False
            self.valve2state = False
            self.valve3state = False
            self.valve4state = False
            self.valve5state = False
            self.valve6state = False
        
        self.ser = None

    def connect(self):
        ports = list(serial.tools.list_ports.comports())

        maple_ports = []

        for x in ports:
            if 'Maple' in x.description:
                maple_ports.append(x)

        port = ''

        for x in maple_ports:
            tmp = serial.Serial(x.device)
            tmp.reset_input_buffer()
            mode = ''
            while len(mode) != 1:
                mode = tmp.readline().decode().split(',')[0]
                print(mode)
            if mode == self.typeof_mc:
                port = x.device 
            tmp.close()
        
        self.ser = serial.Serial(port)

    def get_p(self):
        if self.typeof_mc != 'P':
            return 'Error'

        pressures = self.ser.readline().decode().strip().split(',')

        return pressures
    
    def change_valve(self, valve):

        if valve == 'valve1':
            self.ser.write('A'.encode())
            print('Sent A')
        elif valve == 'valve2':
            self.ser.write('B'.encode())
        elif valve == 'valve3':  
            self.ser.write('C'.encode())
        elif valve == 'valve4':
            self.ser.write('D'.encode())
        elif valve == 'valve5':
            self.ser.write('E'.encode())
        elif valve == 'valve6':
            self.ser.write('F'.encode())