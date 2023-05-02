from autoroutine import AutoRoutine
from wpimath.controller import PIDController

from drivetrain import Drivetrain


class DriveStraight(AutoRoutine):
    def __init__(self, drivetrain: Drivetrain, goal_in_meters: int):
        self.drivetrain = drivetrain
        self.goal = goal_in_meters
        self.turn_pid_controller = PIDController(-20, 0, 0)
        self.turn_pid_controller.setSetpoint(0)
        self.turn_pid_controller.setTolerance(0.05)

        self.straight_pid_controller = PIDController(0.5, 0, 0)
        self.straight_pid_controller.setSetpoint(self.goal)
        self.straight_pid_controller.setTolerance(0.05)

    def run(self):
        difference = self.drivetrain.get_left_distance() - self.drivetrain.get_right_distance()
        rotate = self.turn_pid_controller.calculate(difference)
        power = self.straight_pid_controller.calculate(self.drivetrain.get_average_distance())

        if self.turn_pid_controller.atSetpoint():
            rotate = 0

        if self.straight_pid_controller.atSetpoint():
            forward = 0
        else:
            forward = power

        self.drivetrain.arcadeDrive(rotate, forward)



# Use gyro to get romi to drive up to box and stop on top of the box

