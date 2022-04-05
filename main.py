import card as c
import deck as d
import random

shoe = d.Deck()
dealer_hand = d.Deck()
player_hand = d.Deck()

def main():
	for _ in range (6):
		shoe.set_cards()

	random.shuffle(shoe.cards)
	
	play = True
	
	wins, losses, draws = 0,0,0
	balance = 1000
	
	count = 0

	while play:
		bet = 10
		balance -= bet
		
		playing_hand = True
		busted = False
		
		dealer_hand.deal(shoe, 2)
		count = count + count_card(dealer_hand.cards[0]) #cuenta solo la carta expuesta del dealer
	
		player_hand.deal(shoe, 2)
		count = count + count_card(player_hand.cards[0])
		count = count + count_card(player_hand.cards[1])
		player_hand.set_hand_value()
		
		print("Dealers hand:")
		print("HIDDEN CARD")
		print(dealer_hand.cards[0])
		print("------------------------")
		player_hand.show_hand(False)
	
		while playing_hand:
			print("Count:",count)
			user_input = input("Hit 1) / Stand 2)\n")
			if user_input == "1":
				player_hand.deal(shoe,1)
				count = count + count_card(player_hand.cards[-1]) #cuenta la ultima carta del jugador
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
				count = count + count_card(dealer_hand.cards[-1])
			#for card in range(1,len(dealer_hand.cards)):
				#count = count + count_card(dealer_hand.cards[card]) #cuenta las cartas restantes del dealer
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



def count_card(card):
	score = 0
	low_cards = ["TWO", "THREE", "FOUR", "FIVE", "SIX"]
	high_cards = ["TEN", "JACK", "QUEEN", "KING", "ACE"]
	if card.value in low_cards:
		score+=1
	elif card.value in high_cards:
		score-=1
	return score

main()