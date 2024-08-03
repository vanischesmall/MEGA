from serial import Serial, STOPBITS_ONE
from RobotAPI import RobotAPI

class Package:
    @staticmethod
    def encode(self, ...) -> ...:
        ...

class MEGA:
    def __init__(self) -> None:
        self.arduino_mega_uart = Serial(
                "/dev/ttyS0",
                baudrate=115200,
                stopbits=STOPBITS_ONE
        )


                
    

        

        
