import RPi.GPIO as GPIO

def move_forward():
	GPIO.output(16, False)
	GPIO.output(18, False)

	GPIO.output(38, True)	#rigth backward
	GPIO.output(40, True)	#left forward
	return

def move_backward():
	GPIO.output(38, False)
	GPIO.output(40, False)

	GPIO.output(16, True)	#left backward
	GPIO.output(18, True)	#right backward
	return

def move_forward_left():
	GPIO.output(16, False)
	GPIO.output(18, False)
	GPIO.output(40, False)

	GPIO.output(38, True)	#right forward
	return

def move_forward_right():
	GPIO.output(16, False)
	GPIO.output(18, False)
	GPIO.output(38, False)

	GPIO.output(40, True)	#left forward
	return

def move_backward_left():
	GPIO.output(16, False)
	GPIO.output(38, False)
	GPIO.output(40, False)

	GPIO.output(18, True)	#right backward
	return

def move_backward_right():
	GPIO.output(18, False)
	GPIO.output(38, False)
	GPIO.output(40, False)

	GPIO.output(16, True)	#left backward	
	return

def turn_left():
	GPIO.output(18, False)
	GPIO.output(40, False)

	GPIO.output(16, True)	#left backward
	GPIO.output(38, True)	#right forward
	return

def turn_right():
	GPIO.output(16, False)
	GPIO.output(38, False)

	GPIO.output(18, True)	#right backward
	GPIO.output(40, True)	#left forward
	return

def stop():
	GPIO.output(16, False)
	GPIO.output(18, False)
	GPIO.output(38, False)
	GPIO.output(40, False)
	return

def cleanup():
	print("cleaning GPIOs")
	GPIO.cleanup()
	return
	
# Use physical pin numbers
GPIO.setmode(GPIO.BOARD)

# Set up header pin 16 (GPIO4) as an output (left wheel backward)
print("Setup Pin 16")
GPIO.setup(16, GPIO.OUT)

# Set up header pin 18 (GPIO5) as an output (right wheel backward)
print("Setup Pin 18")
GPIO.setup(18, GPIO.OUT)

# Set up header pin 38 (GPIO20) as an output (right wheel forward)
print("Setup Pin 38")
GPIO.setup(38, GPIO.OUT)

# Set up header pin 40 (GPIO21) as an output (left wheel forward)
print("Setup Pin 40")
GPIO.setup(40, GPIO.OUT)
