from XRPLib.defaults import *
from time import sleep

# available variables from defaults: left_motor, right_motor, drivetrain,
#      imu, rangefinder, reflectance, servo_one, board, webserver
# Write your code Here

board.wait_for_button()

sleep(1)

drivetrain.reset_encoder_position()

while drivetrain.get_left_encoder_position() < 20:
    drivetrain.set_speed(30,30)
    
drivetrain.reset_encoder_position()

while drivetrain.get_left_encoder_position() > -10:
     drivetrain.set_speed(-30,-30)
     
