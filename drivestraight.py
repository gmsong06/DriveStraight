class DriveStraight:
    def __init__(self, drivetrain, goal_in_meters):
        self.drivetrain = drivetrain
        self.goal = goal_in_meters
        self.kp = -20

    def run(self):
        # print(f"RIGHT: {self.drivetrain.encoder_right.getDistance()}, LEFT: {self.drivetrain.encoder_left.getDistance()}")
        # difference = self.drivetrain.encoder_right.getDistance() - self.drivetrain.encoder_left.getDistance()
        # if (self.drivetrain.encoder_right.getDistance() + self.drivetrain.encoder_left.getDistance())/2 >= 200:
        #     self.drivetrain.arcadeDrive(0, 0)
        # else:
        #     if difference > 0.1:
        #         print("TURNING LEFT")
        #         self.drivetrain.arcadeDrive(0.3**2, 0.5)
        #     elif difference < -0.1:
        #         print("TURNING RIGHT")
        #         self.drivetrain.arcadeDrive(-0.3**2, 0.5)
        #     else:
        #         self.drivetrain.arcadeDrive(0, 0.5)


        # BARDOE CODE
        difference = self.drivetrain.get_left_distance() - self.drivetrain.get_right_distance()
        if self.drivetrain.get_average_distance() > self.goal:
            self.drivetrain.arcadeDrive(0, 0)
        else:
            rotate = difference * self.kp
            forward = 0.5
            self.drivetrain.arcadeDrive(rotate, forward)

