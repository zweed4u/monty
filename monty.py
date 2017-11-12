import random


class LetsMakeADeal():
	def __init__(self, switch, debug=False):
		"""
		:param switch: bool - True if choose to switch, after 1 reveal, False if choose to stay with original choice
		"""
		self.switch = switch
		self.debug = debug
		if self.debug:
			if self.switch:
				print('These games will always switch doors given the oppurtunity')
			else:
				print('These games will always remain with the original choice even after a door reveal')
		
	def _setup_game(self):
		self.doors = [1, 2, 3]
		self.zonk_doors = []
		self.prize_door = random.randint(1,3) # int
		if self.debug:
			print(f'Prize door: {self.prize_door}')
		for door in self.doors:
			if door == self.prize_door:
				continue
			else:
				self.zonk_doors.append(door)

	def play(self):
		self._setup_game()

		self.my_choice = random.randint(1,3) # int
		if self.debug:
			print(f'You chose door: {self.my_choice}')
		self.monty_reveal = random.choice(list(set(self.zonk_doors) - set([self.my_choice]))) # int
		if self.debug:
			print(f'Monty reveals zonk door: {self.monty_reveal}')
		if self.switch:
			self.my_choice = random.choice(list(set(self.doors) - set([self.monty_reveal]) - set([self.my_choice])))
			if self.debug:
				print(f'Switched to door: {self.my_choice}')
		if self.my_choice == self.prize_door:
			return 1
		else:
			return 0


wins = 0
num_of_games = 1000000
print(f'Simulating {num_of_games} games with switching')
game_with_switching = LetsMakeADeal(True)
for game in range(num_of_games):
	wins += game_with_switching.play()
print(f'{wins} correct doors guessed/switched to out of {num_of_games} games. ({(float(wins)/float(num_of_games))*100.0}%)')
print()

wins = 0
print(f'Simulating {num_of_games} games withOUT switching')
game_without_switching = LetsMakeADeal(False)
for game in range(num_of_games):
	wins += game_without_switching.play()
print(f'{wins} correct doors guessed to out of {num_of_games} games. ({(float(wins)/float(num_of_games))*100.0}%)')
print()