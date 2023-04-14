class DriveStraight:
    def __init__(self, drivetrain):
        self.drivetrain = drivetrain

    def run(self):
        difference = self.drivetrain.encoder_left.getDistance() - self.drivetrain.encoder_right.getDistance()
        self.drivetrain.arcadeDrive(difference, 0.5)  # TODO: turn left if difference is positive, turn right if difference is negative