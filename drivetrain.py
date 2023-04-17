from wpilib.drive import DifferentialDrive


class Drivetrain(DifferentialDrive):
    def __init__(self, left_motor, right_motor, encoder_left, encoder_right):
        super().__init__(left_motor, right_motor)
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.encoder_left = encoder_left
        self.encoder_right = encoder_right

    def move_forward(self, speed):
        self.arcadeDrive(0, speed)
