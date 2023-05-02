from wpilib.drive import DifferentialDrive
import wpilib
import romi

class Drivetrain(DifferentialDrive):
    def __init__(self, left_motor, right_motor, encoder_left, encoder_right):
        super().__init__(left_motor, right_motor)
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.encoder_left = encoder_left
        self.encoder_right = encoder_right
        self.gyro = romi.RomiGyro()
        self.accelerometer = wpilib.BuiltInAccelerometer()

    def move_forward(self, speed):
        self.arcadeDrive(0, speed)

    def get_left_distance(self):
        return self.encoder_left.getDistance()

    def get_right_distance(self):
        return self.encoder_right.getDistance()

    def get_average_distance(self):
        return (self.get_left_distance() + self.get_right_distance())/2

    def reset_encoders(self):
        self.encoder_left.reset()
        self.encoder_right.reset()

    def get_gyro_angle(self):
        """
        Give the twist of the robot in degrees
        :return: current twist in degrees
        """

        return self.gyro.getAngle()
        # get y axis rotation
        # return self.gyro.getAngleY()

    def reset_gyro(self):
        """
        Reset the gyro to 0 degrees
        """
        self.gyro.reset()
