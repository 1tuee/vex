from vex import * 

con = Controller() 

brain = Brain()
lm = Motor(ports.PORT1, GearSetting.RATIO_18_1, False)
rm = Motor(Ports.PORT6, GearSetting.RATIO_18_1,True)


def main():
	brain.screen.print("code init, working probably, leave the space inside the quotes blank to remove this")	


def avoidstuff():
	while True:
		diste = distance_sensor.distance(MM)
		if distance_sensor.is_object_deteched() and diste < 200:
			# bac kup and turn 
			drivetrain.stop()
			drivetrain.drive_for(REVERSE, 100, MM)
			drivetrain.turn_for(RIGHT, 90, DEGREES)
	 	else:
			drivetrain.drive(FORWARD)

		wait(20, MSEC)



main() 
