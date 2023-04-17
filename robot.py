from wpilib import TimedRobot
from drivetrain import Drivetrain
from wpilib import Spark, Encoder, Joystick
from drivestraight import DriveStraight
import wpilib
import os

class MyRobot(TimedRobot):
    def robotInit(self):
        self.controller = Joystick(0)
        self.drivetrain = Drivetrain(Spark(0), Spark(1), Encoder(4, 5), Encoder(6, 7))
        self.drivetrain.encoder_right.setDistancePerPulse(0.0183)
        self.drivetrain.encoder_left.setDistancePerPulse(0.0183)

        self.drivetrain.encoder_right.reset()
        self.drivetrain.encoder_left.reset()

        self.drive_straight = DriveStraight(self.drivetrain)

    def robotPeriodic(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        self.drive_straight.run()

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        forward = self.controller.getRawAxis(0)
        turn = self.controller.getRawAxis(1)
        self.drivetrain.arcadeDrive(forward, turn)


if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"
    wpilib.run(MyRobot)
