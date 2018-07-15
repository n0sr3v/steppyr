import asyncio, time, logging, time
import steppyr
from steppyr.profiles import accel
from steppyr.drivers.stepdir import StepDirDriver
from contextlib import suppress

logging.basicConfig(level=logging.DEBUG)

# def __init__(self, profile, dir_pin, step_pin, enable_pin=None, pin_mode=GPIO.BCM):
stepperA = steppyr.StepperController(
	driver=StepDirDriver(20, 21, 16),
	profile=accel.AccelProfile("A")
)
stepperB = steppyr.StepperController(
	driver=StepDirDriver(19, 13, 26),
	profile=accel.AccelProfile("B")
)
stepperA.activate()
stepperB.activate()

motorA_steps_per_rev = 6400
motorB_steps_per_rev = 6400

motorA_max_rpm = 50
motorB_max_rpm = 50

# steps per second
stepperA.set_target_speed(motorA_steps_per_rev * ( motorA_max_rpm / 60 ) )
stepperB.set_target_speed(motorB_steps_per_rev * ( motorB_max_rpm / 60 ) )

# steps per second per second
stepperA.set_target_acceleration(1000)
stepperB.set_target_acceleration(1000)

# Pulse width is defined by the stepper driver. 1.9us for the TB6560
stepperA.set_pulse_width(2)
stepperB.set_pulse_width(2)

async def stepperA_move():
	stepperA.move_to(1000)
	await stepperA.wait_on_move()
	print ('a1000')
	stepperA.move_to(-500)
	await stepperA.wait_on_move()
	print ('a-500')
	await stepperB.wait_on_move()
	print ('waited for b') #sync
	stepperA.move_to(0)
	await stepperA.wait_on_move()
	print ('a0')
	stepperA.move_to(1000)
	await stepperA.wait_on_move()
	print ('a1000')
	stepperA.move_to(0)
	await stepperA.wait_on_move()
	print ('a0')
async def stepperB_move():
	stepperB.move_to(500)
	await stepperB.wait_on_move()
	print ('b500')
	stepperB.move_to(-500)
	await stepperB.wait_on_move()
	print ('b-500')
	stepperB.move_to(1000)
	await stepperB.wait_on_move()
	print ('b1000') #sync
	stepperB.move_to(0)
	await stepperB.wait_on_move()
	print ('b0')
	
	
loop = asyncio.get_event_loop()
asyncio.ensure_future(stepperA.run_forever())
asyncio.ensure_future(stepperB.run_forever())
try:
	loop.run_until_complete(
		asyncio.gather(
			stepperA_move(),
			stepperB_move()
		)
	)
finally:
	stepperA.shutdown()
	stepperB.shutdown()
	# Let's also cancel all running tasks:
	pending = asyncio.Task.all_tasks()
	for task in pending:
		task.cancel()
		# Now we should await task to execute it's cancellation.
		# Cancelled task raises asyncio.CancelledError that we can suppress:
		with suppress(asyncio.CancelledError):
			loop.run_until_complete(task)
			loop.close()