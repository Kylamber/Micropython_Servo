class Servo:
    def __init__(self, servo):
        """
        Initialize the servo.

        Args:
        -> servo: PWM object of the servo.
        """
        
        # Setting up the servo
        self._servo = servo
        self._servo.freq(50) # setting the frequency to 50 Hz to match the servo
        
        # Calibrate the servo 
        self._line_eq = self.calibrate(min_duty = 51, max_duty = 102)
        self.set_angle(0)

    def set_angle(self, angle):
        """
        Set the angle of the servo.
        
        Args:
        -> angle: desired angle.
        """

        duty = int(self._line_eq(angle)) # since the duty can only be integers, int is used.
        self._servo.duty(duty)
    
    def set_duty(self, duty):
        """
        Set the duty of the servo.
        
        Args:
        -> duty: desired duty.
        """
        self._servo.duty(duty)
        
    def calibrate(self, min_duty, max_duty, min_angle = -90, max_angle = 90):
        """
        Create line equation based on if:
        -> min_duty = -90 degrees
        -> max_duty = 90 degrees
        
        Args:
        -> min_duty: minimum duty of the servo.
        -> max_duty: maximum duty of the servo.
        -> min_angle: arbitrary minimum, for readibility sake, 0 or -90 is preferred.
        -> min_angle: arbitrary maximum, for readibility sake, 180 or 90 is preferred.
        """
        
        gradient = (min_duty-max_duty)/(-90 - 90)
        constant = min_duty - gradient * (-90)
        line_eq = lambda x: gradient * x + constant
        
        return line_eq
