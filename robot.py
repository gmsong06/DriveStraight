from wpilib import TimedRobot
from drivetrain import Drivetrain
from wpilib import Spark, Encoder

class MyRobot(TimedRobot):
    def robotInit(self):
        self.drivetrain = Drivetrain(Spark(0), Spark(1), Encoder(4, 5), Encoder(6, 7))
        self.drivetrain.encoder_right.setDistancePerPulse(0.0183)
        self.drivetrain.encoder_left.setDistancePerPulse(0.0183)

        self.drivetrain.encoder_right.reset()
        self.drivetrain.encoder_left.reset()

    def robotPeriodic(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        pass