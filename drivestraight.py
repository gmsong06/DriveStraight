class DriveStraight:
    def __init__(self, drivetrain):
        self.drivetrain = drivetrain

    def run(self):
        self.drivetrain.move_forward(0.5)
        print(f"RIGHT: {self.drivetrain.encoder_right.getDistance()}, LEFT: {self.drivetrain.encoder_left.getDistance()}")
        difference = self.drivetrain.encoder_right.getDistance() - self.drivetrain.encoder_left.getDistance()
        if difference > 0.1:
            print("TURNING RIGHT")
            self.drivetrain.arcadeDrive(0.3, 0.5)
        elif difference < -0.1:
            print("TURNING LEFT")
            self.drivetrain.arcadeDrive(-0.4, 0.5)
        else:
            self.drivetrain.arcadeDrive(0, 0.5)

        # self.drivetrain.arcadeDrive(difference, 0.5)  # TODO: turn left if difference is positive, turn right if difference is negative