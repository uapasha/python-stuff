from sys import exit
from random import randint

class Scene(object):
	
	def enter(self):
		print "This scene is not yet configured"
		exit(1)

class Engine(object):
	
	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.oppening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
		
		# be sure to print out the last scene
		current_scene.enter()
		
		
class Death(Scene):

	quips = [
		"You died. You kinda suck at this.",
		"Your mam woulf be proud...if she were smartet.",
		"Such a luser.",
		"I have a small puppy that's better at this."
	]
	
	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)
		
class CentralCorridor(Scene):

	def enter(self):
		print "The Gothons of Planet Percal #25 have invaded your ship and..."
		
		action = raw_input("> ")
		
		if action == "shoot!":
			print "Quick on the draw you yank out blaster and fire it at the Gothon.."
			print "he kills you"
			return 'death'
		
		elif action == "dodge!":
			print "Like a world class boxer you dodge, weawe, slip and slide.."
			print "He eats you"
			return 'death'
		
		elif action == "tell a joke":
			print "Luckly for you they made you learn Gothon insults in the academy."
			print "You shot him"
			return 'laser_weapon_armory'
		
		else: 
			print "DOES NOT COMPUTE!"
			return 'central_coridor'
			
class LaserWeaponArmory(Scene):

	def enter(self):
		print "You do a dive into the Weapon Armory, crouch and scan the room..."
		print "you need the code to get the bomb out. if you get the code"
		print "wrong 10 times then the lock closes forever and you can't"
		print "get to the bomb. The code is 3 digits."
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[keypad]> ")
		guesses = 0
		
		while guess != code and guesses <9:

			print "BZZZZEDDD!"
			guesses += 1
			guesss = raw_input("[keypad]> ")
		
		if guess == code:
			print "The container opens and you ran to the bridge"
			return "the_bridge"
		
		else: 
			print "locked. You loose"
			return 'death'

class TheBridge(Scene):
	
	def enter(self):
		print "you burst into the bridge with the netron destruct bomb.."
		
		action = raw_input("> ")
		
		if action == "throw the bomb":
			print "in a panic you throw the bomb at the group of the Gothons"
			print "they kill you and blow up themselves"
			return 'death'
			
		elif action == "slowly place the bomb":
			print "You point your blaster at the bomb under your arm"
			print "you ran to the escape pod"
			return 'escape_pod'
		
		else:
			print "DOES NOT COMPUTE"
			return 'the_bridge'

class	EscapePod(Scene):

	def enter(self):
		print "You rush through the ship desperately trying to make it to"
		print "the escape pod before the whole ship explodes.  It seems like"
		print "hardly any Gothons are on the ship, so your run is clear of"
		print "interference.  You get to the chamber with the escape pods, and"
		print "now need to pick one to take.  Some of them could be damaged"
		print "but you don't have time to look.  There's 5 pods, which one"
		print "do you take?"
		
		good_pod = randint(1,5)
		guess = raw_input("[pod #]> ")
			
		if int(guess) != good_pod:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod escapes out into the void of space, then"
			print "implodes as the hull ruptures, crushing your body"
			print "into jam jelly."
			return 'death'
		else:
			print "You jump into pod %s and hit the eject button." % guess
			print "The pod easily slides out into space heading to"
			print "the planet below.  As it flies to the planet, you look"
			print "back and see your ship implode then explode like a"
			print "bright star, taking out the Gothon ship at the same"
			print "time.  You won!"

			return 'finished'

class Finished(Scene):
	
	def enter(self):
		print "You won! Good job!"
		return 'finished'
		
class Map(object):
	
	scenes = {
		'central_coridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death' : Death(),
		'finished': Finished()
	}
	def __init__(self, start_scene):
		self.start_scene = start_scene
	
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
	
	def oppening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('central_coridor')
a_game = Engine(a_map)
a_game.play()