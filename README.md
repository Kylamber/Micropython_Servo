# Micropython Servo 

This is a library for controlling servo using Micropython. Tested working on ESP32 with Micropython v1.19 (Micropython 1.18 can't use PWM with frequencies lower than 611 Hz, be mindful of that).

## Usage

```python
from machine import Pin, PWM
from Servo import Servo

# Create the Servo object
servo = Servo(PWM(Pin(13), freq=50)) # the frequency of 50 Hz is the default for servos.

# Optionally calibrate the servo
servo.calibrate(min_duty=51, max_duty=102, min_angle=-90, max_angle=90)

# Set the duty manually
servo.set_duty(51)

# Set the angle
servo.set_angle(90)
```

## Explanations
### calibrate
The servo is controlled using PWM and it is said that the PWM is using a 20 ms period or 50 Hz frequency (T = 1/f). (read more: https://en.wikipedia.org/wiki/Servo_control)

Pulse widths and its corresponding angles:
- 1 ms   = -90 deg
- 1.5 ms = 0 deg
- 2 ms   = 90 deg

The duty method in PWM sets the ratio of the argument to 1023, e.g. PWM.duty(512) is 512/1023 which is roughly 50%. Since 1 ms in 20 ms period is 1/20 or 5% of the period, the duty is (1023 * 1/20). For 2 ms in 20 ms period is 2/20 or 10% of the period, the duty is (1023 * 2/20). (read more: https://docs.micropython.org/en/latest/esp32/quickref.html#pwm-pulse-width-modulation)

Assuming it's linear, the line equation given that -90 corresponds with a duty of 1023/20 and 90 degrees corresponds with a duty of 1023*2/20 is

`duty = 341/1200 * angle + 3069/40`
