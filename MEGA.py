class MEGA:
    def __init__(self) -> None:
        self.arduino_mega_uart = Serial(
                "/dev/ttyS0",
                baudrate=115200,
                stopbits=STOPBITS_ONE
        )


                
    

        

        
