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

# Drive for 30 cm
while drivetrain.get_left_encoder_position() < 30:
    # Set Speed (Right Wheel is Slower)
    drivetrain.set_speed(10,20)

# Stop Driving
drivetrain.stop()

