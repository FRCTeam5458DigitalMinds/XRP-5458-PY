from XRPLib.defaults import *
from time import sleep

# available variables from defaults: left_motor, right_motor, drivetrain,
#      imu, rangefinder, reflectance, servo_one, board, webserver
# Write your code Here

# Wait for User Button Press
board.wait_for_button()

# Time to Get Away Before Movement
sleep(1)

# Reset Encoder
drivetrain.reset_encoder_position()

# Reset IMU
imu.reset()

# Set both distances (one is for distance from block)
distanceOne = 80

# Turn clockwise 
drivetrain.turn(-45,0.25)

# While distance is greater than 15cm keep going forward
drivetrain.straight(80, 0.5)
    
drivetrain.stop()

# Turn clockwise 
drivetrain.turn(35,0.25)

# set both distances (one is for distance from block)
distanceTwo = 27

drivetrain.straight(27, 0.5)

drivetrain.turn(92, 0.25)

distanceThree = 10

while rangefinder.distance() > distanceThree:
    drivetrain.set_speed(10, 10)
