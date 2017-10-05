from ev3dev.ev3 import *

a = LargeMotor('outA')
b = LargeMotor('outB')

a.run_timed(time_sp = 60, speed_sp = 100),b.run_timed(time_sp = 60, speed_sp = 100)

while a.is_running:
    pass

