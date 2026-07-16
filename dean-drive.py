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

# Print Heading 
print("Current YAW:", imu.get_yaw())

# Drive for Under 42 cm
while drivetrain.get_left_encoder_position() < 42:
    drivetrain.straight(30,0.5)

# Stop Driving
drivetrain.stop()

# Print Heading Again
print("Current YAW:", imu.get_yaw())



