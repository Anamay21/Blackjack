import random
import os
import art_blackjack

points_dic = {
	"A" : 1,
	"2" : 2,
	"3" : 3,
	"4" : 4,
	"5" : 5,
	"6" : 6,
	"7" : 7,
	"8" : 8,
	"9" : 9,
	"10": 10,
	"J" : 10,
	"Q" : 10,
	"K" : 10,
}

user = {}
cpu = {}

points = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
suits = ['diamonds', 'clubs', 'spades', 'hearts']

# User's Total.
def user_total():
	ut = 0
	for key in user:
		ut += points_dic[key]
	#print(f"Your Total: {ut}")
	return ut

# Dealer's Total.
def cpu_total():
	ct = 0
	for key in cpu:
		ct += points_dic[key]
	#print(f"Dealer's Total: {ct}")
	return ct

# Decision Function to conclude the result.
def decision():
	user_final_total = user_total()
	cpu_final_total = cpu_total()

	if cpu_final_total > 21 or (user_final_total > cpu_final_total and user_final_total <= 21):
		os.system('clear')
		
		print("Yor Cards: ")
		art_blackjack.card_print(user, False)
		print(f"Your Total: {user_total()}")
		print("")

		print("Dealer's Cards: ")
		art_blackjack.card_print(cpu, False)
		print(f"Dealer's Total: {cpu_total()}")
		print("")

		print(f"Yuhoooo! You Won!")

	elif user_final_total > 21 or (user_final_total < cpu_final_total and cpu_final_total <= 21):
		os.system('clear')
		print("Your Cards: ")
		art_blackjack.card_print(user, False)
		print(f"Your Total: {user_total()}")
		print("")
		
		print("Dealer's Cards: ")
		art_blackjack.card_print(cpu, False)
		print(f"Dealer's Total: {cpu_total()}")
		print("")

		print("You lose!, Try again.")

	else:
		os.system('clear')
		print("Your Cards: ")
		art_blackjack.card_print(user, False)
		print(f"Your Total: {user_total()}")
		print("")
		
		print("Dealer's Cards: ")
		art_blackjack.card_print(cpu, False)
		print(f"Dealer's Total: {cpu_total()}")
		print("")

		print("Error occured while printing the result")

os.system('clear')

for deal in range(2):
	# User's First Two Cards.
	key = random.choice(points)
	value = random.choice(suits)
	user[key] = value
	
	# Dealer's First Two Cards.
	key = random.choice(points)
	value = random.choice(suits)
	cpu[key] = value

# Printing User's Cards.
print("Your Cards: ")
art_blackjack.card_print(user, False)
print(f"Your Total: {user_total()}")
print("")

# Printing Dealer's Cards.
print("Dealer's Cards: ")
art_blackjack.card_print(cpu, True)
print("")

hit = True
while hit:
	hit_or_not = input("Type 'Hit' to draw a card or 'Stand' to pass: ").lower()
	if hit_or_not == 'hit':
		os.system('clear')
		key = random.choice(points)
		
		# To check if card is repeated or not
		if key in user:
			key_found = True
			while key_found:
				key = random.choice(points)
				if key not in user:
					key_found = False

		value = random.choice(suits)
		user[key] = value
	elif hit_or_not == 'stand':
		os.system('clear')
		hit = False
	else:
		os.system('clear')
		print("Enter valid input")

	print("Your Cards: ")
	art_blackjack.card_print(user, False)
	print(f"Your Total: {user_total()}")
	print("")

	print("Dealer's Cards: ")
	art_blackjack.card_print(cpu, True)
	print("")

	if hit == False:
		decision()

