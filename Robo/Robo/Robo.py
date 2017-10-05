from ev3dev.ev3 import *

B = LargeMotor('outB')
C = LargeMotor('outC')

B.run_timed(time_sp = 3000, speed_sp = 360),C.run_timed(time_sp = 3000, speed_sp = 360)

while B.is_running:
    pass

