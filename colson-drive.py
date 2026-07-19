from XRPLib.defaults import *

# available variables from defaults: left_motor, right_motor, drivetrain,
#      imu, rangefinder, reflectance, servo_one, board, webserver
# Write your code Here
#wait for button
board.wait_for_button()

#reset memory
drivetrain.reset_encoder_position()

imu.reset()

#make the robot move
drivetrain.turn(-90, 0.5)
drivetrain.straight(30,0.5)
drivetrain.turn(90, 0.5)
drivetrain.straight(30,0.5)
drivetrain.turn(90, 0.5)
drivetrain.straight(30,0.5)
drivetrain.turn(90, 0.5)
drivetrain.straight(30, 0.5)

