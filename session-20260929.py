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

# # Go Straight Forward Specific Distance (Example 35 cm)
# drivetrain.straight(40.00,0.8)

# # Turn Right 90 Degrees 
# drivetrain.turn(90.00,-0.50)

# # Go Straight Forward 25 cm
# drivetrain.straight(25.00,0.8)

# # Turn Left 45 Degrees
# drivetrain.turn(45.00, 0.50)

# drivetrain.straight(15.00,0.8)

# # Turn Right 90 Degrees 
# drivetrain.turn(90.00,-0.50)

# # Go Straight Forward 25 cm
# drivetrain.straight(25.00,0.8)

# # Turn Left 45 Degrees
# drivetrain.turn(90.00, 0.50)

# drivetrain.straight(40.00,0.8)

# drivetrain.turn(90.00,-0.50)

# drivetrain.straight(20.00,0.8)

# Thingy 1
drivetrain.straight(35.00,0.8)
drivetrain.turn(90.00,-0.50)

# Thingy 2
drivetrain.straight(48.00,0.8)
drivetrain.turn(90.00,0.50)

# Thingy 3
drivetrain.straight(23.50,0.8)
drivetrain.turn(90.00,-0.50)

# Thingy 4
drivetrain.straight(30.0, 0.8)

drivetrain.turn(90.0,-0.5)

drivetrain.straight(18.50,0.8)

drivetrain.turn(90.0,0.5)

drivetrain.straight(22.0,0.8)

# Stop Driving
drivetrain.stop()

print("Mission complete :)") 


