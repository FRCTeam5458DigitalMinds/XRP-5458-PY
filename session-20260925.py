from XRPLib.defaults import *

# available variables from defaults: left_motor, right_motor, drivetrain,
#      imu, rangefinder, reflectance, servo_one, board, webserver
# Write your code Here


############ 5458 Basics ########

# Import Required Sleep Function from the Time Module
from time import sleep

# Wait for User Button Press
board.wait_for_button()

# Time to Get Away Before Movement
sleep(1)

# Reset Encoder
drivetrain.reset_encoder_position()

# Reset IMU
imu.reset()

#################################

# Go Straight Forward Specific Distance (Example 35 cm)
drivetrain.straight(35.00,0.8)

# Turn Right 90 Degrees 
drivetrain.turn(90.00,-0.50)

while reflectance.get_right() <= 0.40:
    drivetrain.set_speed(5,5)
    print(reflectance.get_right())

drivetrain.stop()



