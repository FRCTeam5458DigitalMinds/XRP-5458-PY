from XRPLib.defaults import *

# available variables from defaults: left_motor, right_motor, drivetrain,
#      imu, rangefinder, reflectance, servo_one, board, webserver
# Write your code Here

############ 5458 Basics ########

# Reset Encoder
drivetrain.reset_encoder_position()

# Reset IMU
imu.reset()

#################################

# Go Straight Forward Specific Distance (Example 35 cm)
drivetrain.straight(40.00,0.8)

# Turn Right 90 Degrees 
drivetrain.turn(90.00,-0.50)

# Go Straight Forward 25 cm
drivetrain.straight(25.00,0.8)

# Turn Left 45 Degrees
drivetrain.turn(45.00, 0.50)

# Stop Driving
drivetrain.stop()

print("Mission complete :)")

