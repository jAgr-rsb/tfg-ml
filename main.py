import card as c
import deck as d
import random

shoe = d.Deck()
dealer_hand = d.Deck()
player_hand = d.Deck()

for _ in range (6):
	shoe.set_cards()

random.shuffle(shoe.cards)

play = True

wins, losses, draws = 0,0,0
balance = 1000

while play:
	
	bet = 10
	balance -= bet

	playing_hand = True
	busted = False
	
	dealer_hand.deal(shoe, 2)
	player_hand.deal(shoe, 2)
	player_hand.set_hand_value()
	
	print("Dealers hand:")
	print(dealer_hand.cards[0])
	print("HIDDEN CARD")
	print("------------------------")
	player_hand.show_hand(False)

	while playing_hand:
		user_input = input("Hit 1) / Stand 2)\n")
		if user_input == "1":
			player_hand.deal(shoe,1)
			if player_hand.value <= 21:
				player_hand.show_hand(False)
			else:
				player_hand.show_hand(False)
				print("BUST!")
				busted = True
				playing_hand = False
				losses += 1
		elif user_input == "2":
			playing_hand = False

	if not busted:
		while dealer_hand.value < 17:
			dealer_hand.deal(shoe,1)
		dealer_hand.show_hand(True)
		print("Player hand value:",player_hand.value)
		print("\n")
		if dealer_hand.value < player_hand.value or dealer_hand.value > 21:
			print("Player wins!")
			wins += 1
			if player_hand.value == 21 and player_hand.check_blackjack():
				balance += bet+bet*3/2
				print("BLACKJACK!")
			else:
				balance += bet*2
		elif dealer_hand.value > player_hand.value:
			print("House wins!")
			losses += 1
		elif dealer_hand.value == player_hand.value:
			print("Draw")
			draws += 1
			balance += bet

	dealer_hand.reset()
	player_hand.reset()


	print("\n")
	print("////////////////////////")
	print("\n")
	print("Wins:",wins)
	print("Losses:",losses)
	print("Draws:",draws)
	print("Balance:",balance)
	print("\n")
	print("////////////////////////")
	print("\n")