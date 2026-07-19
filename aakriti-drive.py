from XRPLib.defaults import *

# available variables from defaults: left_motor, right_motor, drivetrain,
#      imu, rangefinder, reflectance, servo_one, board, webserver
# Write your code Here

# Wait for User Button Press
board.wait_for_button()

# Reset Encoder
drivetrain.reset_encoder_position()

# Reset IMU
imu.reset()

drivetrain.turn(-60, 0.5)
drivetrain.straight(40, 0.5)
drivetrain.turn(-60, 0.5)
drivetrain.straight(40, 0.5)
drivetrain.turn(-130, 0.5)
drivetrain.straight(40, 0.5)



