from drivetrain import Drivetrain
class GyroTurn:

    def __init__(self, drivetrain: Drivetrain, goal_in_degrees: float):
        self.drivetrain = drivetrain
        self.goal = goal_in_degrees
        self.kp = -1/25

    def run(self):
        current_angle = self.drivetrain.get_gyro_angle()
        error = abs(current_angle - self.goal)
        if error < 1:
            self.drivetrain.arcadeDrive(0, 0)
        else:
            power = error * self.kp
            power = max(-0.5, min(.5, power))
            self.drivetrain.arcadeDrive(power, 0)
