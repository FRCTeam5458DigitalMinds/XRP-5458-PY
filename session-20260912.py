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

# Set both distances (one is for distance from box, two is for distance from glasses)
distanceOne = 15
distanceTwo = 10
distanceThree = 8
distanceFour = 7

# While distance is greater than 15cm keep going forward
while rangefinder.distance() > distanceOne:
    drivetrain.set_speed(10, 10)
 
# Stop moving
drivetrain.stop()

# Turn clockwise 
drivetrain.turn(-90,0.25)

sleep(1)

while rangefinder.distance() > distanceTwo:
    drivetrain.set_speed(10, 10)

drivetrain.stop()

drivetrain.turn(90, 0.25)

sleep(1)

while rangefinder.distance() > distanceThree:
    drivetrain.set_speed(10, 10)

drivetrain.stop()

drivetrain.turn(90, 0.25)


sleep(1)

while rangefinder.distance() > distanceFour:
    drivetrain.set_speed(10, 10)

# Go until within 10 cm
# Turn to right 90 degrees
# Go straight certain amount
# Turn to the left 90 degrees
# Go straight until it comes within 5cm of object

    