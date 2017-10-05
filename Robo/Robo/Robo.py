from ev3dev.ev3 import *

a = LargeMotor('outA')
b = LargeMotor('outB')

a.run_timed(time_sp = 3000, speed_sp = 360),b.run_timed(time_sp = 3000, speed_sp = 360)

while a.is_running:
    pass

