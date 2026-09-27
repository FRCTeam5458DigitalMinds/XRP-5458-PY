from XRPLib.board import Board
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.gamepad import Gamepad

board = Board.get_default_board()
drive = DifferentialDrive.get_default_differential_drive()
gp = Gamepad.get_default_gamepad()

while not board.is_button_pressed():

    # Left stick Y = forward/reverse
    forward = gp.get_value(gp.Y1)

    # Right stick X = turning
    turn = -gp.get_value(gp.X2)

    # Arcade drive
    left = forward + turn
    right = forward - turn

    # Keep values between -1 and 1
    left = max(-1, min(1, left))
    right = max(-1, min(1, right))

    drive.set_effort(left, right)
    
    
    
    