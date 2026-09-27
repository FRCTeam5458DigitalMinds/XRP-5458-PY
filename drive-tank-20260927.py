from XRPLib.board import Board
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.gamepad import Gamepad

board = Board.get_default_board()
drive = DifferentialDrive.get_default_differential_drive()
gp = Gamepad.get_default_gamepad()

while not board.is_button_pressed():

    left = gp.get_value(gp.Y1)
    right = gp.get_value(gp.Y2)

    drive.set_effort(left, right)