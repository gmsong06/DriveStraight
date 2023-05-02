from autoroutine import AutoRoutine
from wpimath.controller import PIDController

from drivetrain import Drivetrain


class DriveStraight(AutoRoutine):
    def __init__(self, drivetrain: Drivetrain, goal_in_meters: int):
        self.drivetrain = drivetrain
        self.goal = goal_in_meters
        self.rotation_pid_controller = PIDController(-20, 0, 0)
        self.rotation_pid_controller.setSetpoint(0)
        self.rotation_pid_controller.setTolerance(0.05)

        self.distance_pid_controller = PIDController(0.5, 0, 0)  # need to tune
        self.distance_pid_controller.setSetpoint(self.goal)
        self.distance_pid_controller.setTolerance(0.05)  # need to tune

    def run(self):
        encoder_error = self.drivetrain.get_left_distance() - self.drivetrain.get_right_distance()
        distance_error = self.goal - self.drivetrain.get_average_distance()

        rotate = self.rotation_pid_controller.calculate(encoder_error)
        power = self.distance_pid_controller.calculate(distance_error)

        if self.rotation_pid_controller.atSetpoint():
            rotate = 0

        if self.distance_pid_controller.atSetpoint():
            power = 0

        self.drivetrain.arcadeDrive(rotate, power)
