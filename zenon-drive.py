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

# Drive
#drivetrain.straight(20, 0.6)

#drivetrain.turn(-45, 0.3)


distance = 10

while rangefinder.distance() > distance:
    drivetrain.set_speed(20, 20)
  
    

drivetrain.stop()
        
# Print Heading 
print("Current distance: ", rangefinder.distance())       







