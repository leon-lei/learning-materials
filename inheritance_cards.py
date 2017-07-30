class Card(object):
	"""Represents a standard playing card
	spades 3, hearts 2, diamonds 1, clubs 0
	jack 11, queen 12, king 13	
	"""
	def __init__(self, suit=0, rank=2):
		self.suit = suit
		self.rank = rank
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
	def __str__(self):
		return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])
	def __cmp__(self, other):
		# check the suits
		if self.suit > other.suit: return 1
		if self.suit < other.suit: return -1
		
		#suits are the same...check ranks
		if self.rank > other.rank: return 1
		if self.rank < other.rank: return -1
		
		#rank are the same...so it's a tie
		return 0
		# t1 = self.suit, self.rank
		# t2 = other.suit, other.rank
		# return cmp(t1, t2)
		
class Deck(object):
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range (1,14):
				card = Card(suit, rank)
				self.cards.append(card)
	def __str__(self):
		res = []
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)
	def pop_card(self):
		return self.cards.pop()
	def add_card(self, card):
		self.cards.append(card)
	def shuffle(self):
		random.shuffle(self.cards)
		
class Hand(Deck):
	"""Represents a hand of playing cards."""
	def __init__(self, label=''):
		self.cards = []
		self.label = label

import random
		
hand = Hand('new hand')
print hand.cards
print hand.label

deck = Deck()
card = deck.pop_card()
hand.add_card(card)
print hand