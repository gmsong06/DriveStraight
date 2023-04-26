from wpilib import TimedRobot
from robotcontainer import RobotContainer
import wpilib
import os

class MyRobot(TimedRobot):
    def robotInit(self):
        self.container = RobotContainer()
    def robotPeriodic(self):
        pass

    def autonomousInit(self):
        self.auto = self.container.get_autonomous_routine()

    def autonomousPeriodic(self):
        self.auto.run()

    def autonomousExit(self):
        self.container.drivetrain.reset_gyro()
        self.container.drivetrain.reset_encoders()

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        forward = self.container.controller.getRawAxis(0)
        rotate = self.container.controller.getRawAxis(1)
        self.container.drivetrain.arcadeDrive(forward, rotate)


if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"
    wpilib.run(MyRobot)
