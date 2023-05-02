from autoroutine import AutoRoutine
from drivetrain import Drivetrain
from wpimath.controller import PIDController

class GyroTurn(AutoRoutine):

    # P - proportional - how much to turn based on how far off we are
    # I - integral - how much to turn based on how long we've been off
    # D - derivative - how much to turn based on how fast we're approaching the goal
    # F - feedforward - how much to turn based on how fast we want to turn
    def __init__(self, drivetrain: Drivetrain, goal_in_degrees: float):
        self.drivetrain = drivetrain
        self.goal = goal_in_degrees
        self.pid_controller = PIDController(1/200, 1/1000, 0)
        self.pid_controller.setSetpoint(self.goal)
        self.pid_controller.setIntegratorRange(-0.2, 0.2)
        self.pid_controller.setTolerance(3)


    def run(self):
        current_angle = self.drivetrain.get_gyro_angle()
        power = self.pid_controller.calculate(current_angle)
        if self.pid_controller.atSetpoint():
            self.drivetrain.arcadeDrive(0, 0)
        else:
            self.drivetrain.arcadeDrive(0, power)
