import asyncio, time, logging, time
import steppyr
from steppyr.profiles import max
from steppyr.drivers.stepdir import StepDirDriver
from contextlib import suppress

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

# def __init__(self, profile, dir_pin, step_pin, enable_pin=None, pin_mode=GPIO.BCM):
stepperA = steppyr.StepperController(
    driver=StepDirDriver(20, 21, 16),
    #def __init__(self, acceleration_steps=0, max_start_speed=0.0, deceleration_steps=0, name=None):
    profile=max.MaxProfile(1, 1, 1,"A")
)
stepperB = steppyr.StepperController(
    driver=StepDirDriver(19, 13, 26),
    #def __init__(self, acceleration_steps=0, max_start_speed=0.0, deceleration_steps=0, name=None):
    profile=max.MaxProfile(1, 1, 1,"B")
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
    log.debug('stepperA.move_to(1000)')
    stepperA.move_to(2000)
    await stepperA.wait_on_move()
async def stepperB_move():
    log.debug('stepperA.move_to(1000)')
    stepperB.move_to(1000)
    await stepperB.wait_on_move()
	
	
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