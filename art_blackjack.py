def card_print(card, hidden):
	if hidden:
		hidden_card = list(card)[0]
	else:
		hidden_card = "None"
	# --- 1 ---
	for key in card:
		print(f".--------------.", end = '  ')
	print("")

	#--- 2 ---
	for key in card:
		if key == hidden_card:
			print(f"|::::::::::::::|", end = '  ')
		else:
			print(f"| {key}            |", end = '  ')
	print("")

	#--- 3 ---
	for key in card:
		print(f"|              |", end = '  ')
	print("")

	#--- 4 ---
	for key in card:
		if key == hidden_card:
			print(f"|::::::::::::::|", end = '  ')
		else:
			print(f"|              |", end = '  ')
	print("")

	#--- 5 ---
	for key in card:
		if key == hidden_card:
			print(f"|              |", end = '  ')
		else:
			if card[key] == 'diamonds':
				print(f"|      /\      |", end = '  ')
			elif card[key] == 'clubs':
				print(f"|      __      |", end = '  ')
			elif card[key] == 'spades':
				print(f"|              |", end = '  ')
			else:
				print(f"|     _  _     |", end = '  ')
	print("")

	#--- 6 ---
	for key in card:
		if key == hidden_card:
			print(f"|,,,,,,,,,,,,,,|", end = '  ')
		else:
			if card[key] == 'diamonds':
				print(f"|     /  \     |", end = '  ')
			elif card[key] == 'clubs':
				print(f"|    _(  )_    |", end = '  ')
			elif card[key] == 'spades':
				print(f"|      /\      |", end = '  ')
			else:
				print(f"|    ( \/ )    |", end = '  ')
	print("")

	#--- 7 ---
	for key in card:
		if key == hidden_card:
			print(f"|‘‘‘‘‘‘‘‘‘‘‘‘‘‘|", end = '  ')
		else:
			if card[key] == 'diamonds':
				print(f"|     \  /     |", end = '  ')
			elif card[key] == 'clubs':
				print(f"|   (__  __)   |", end = '  ')
			elif card[key] == 'spades':
				print(f"|     /  \     |", end = '  ')
			else:
				print(f"|     \  /     |", end = '  ')
	print("")
	
	#--- 8 ---
	for key in card:
		if key == hidden_card:
			print(f"|              |", end = '  ')
		else:
			if card[key] == 'diamonds':
				print(f"|      \/      |", end = '  ')
			elif card[key] == 'clubs':
				print(f"|     /__\     |", end = '  ')
			elif card[key] == 'spades':
				print(f"|    (_/\_)    |", end = '  ')
			else:
				print(f"|      \/      |", end = '  ')
	print("")

	#--- 9 ---
	for key in card:
		if key == hidden_card:
			print(f"|::::::::::::::|", end = '  ')
		else: 
			print(f"|              |", end = '  ')
	print("")

	#--- 10 ---
	for key in card:
		print(f"|              |", end = '  ')
	print("")

	#--- 11 ---
	for key in card:
		if key == hidden_card:
			print(f"|::::::::::::::|", end = '  ')
		else:
			print(f"|            {key} |", end = '  ')
	print("")

	#--- 12 ---
	for key in card:
		print(f"`--------------'", end = '  ')
	print("")
