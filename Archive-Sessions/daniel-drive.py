from XRPLib.defaults import *
from time import sleep

# available variables from defaults: left_motor, right_motor, drivetrain,
#      imu, rangefinder, reflectance, servo_one, board, webserver
# Write your code Here

board.wait_for_button()

sleep(1)

drivetrain.reset_encoder_position()

while rangefinder.distance() > 20:
    drivetrain.set_speed(15,15)
    
drivetrain.turn(-90)