import wpilib
from wpilib import Spark, Encoder
from gyroturn import GyroTurn
from drivestraight import DriveStraight
from drivetrain import Drivetrain
class RobotContainer:

    def __init__(self):
        self.controller = wpilib.Joystick(0)
        self.drivetrain = Drivetrain(Spark(0), Spark(1), Encoder(4, 5), Encoder(6, 7))
        self.drivetrain.encoder_right.setDistancePerPulse(0.0183)
        self.drivetrain.encoder_left.setDistancePerPulse(0.0183)

        self.drivetrain.encoder_right.reset()
        self.drivetrain.encoder_left.reset()
        self.chooser = wpilib.SendableChooser()
        self._configure()

    def _configure(self):
        self.chooser.setDefaultOption("Drive Straight", DriveStraight(self.drivetrain, 2))
        self.chooser.addOption("Turn 90", GyroTurn(self.drivetrain, 90))
        wpilib.SmartDashboard.putData("Auto Chooser", self.chooser)

    def get_autonomous_routine(self):
        return self.chooser.getSelected()