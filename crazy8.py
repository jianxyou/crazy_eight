# nom : Timothy Lee 20213311
# nom : Jianxin You 20134401

import math
import random
import copy


### LinkedList

class LinkedList:
    
#------------------------------------------------------------------------------------
    class _Node:
        def __init__(self, v, n):
            self.value = v
            self.next = n

    def __init__(self):
        self._head = None
        self._size = 0

        
#------------------------------------------------------------------------------------
    def __str__(self):
        res = '['
        cur = self._head
        while cur != None:
            res += str(cur.value) + ', '
            cur = cur.next
            
        
        if len(res) == 1:
            return '[]'
        else:
            return res[0:-2] + ']'
        
        
#------------------------------------------------------------------------------------        
    def __len__(self):
        return self._size
    

#------------------------------------------------------------------------------------
    def isEmpty(self):
        return self._size == 0

    
#------------------------------------------------------------------------------------
    # Adds a node of value v to the beginning of the list
    def add(self, v): 
        self._head = self._Node(v,self._head)
        self._size += 1

        
#------------------------------------------------------------------------------------
    # Adds a node of value v to the end of the list
    def append(self,v):
        if not self._head:
            self._head = self._Node(v,None)
               
        else:
            cur = self._head
            while(cur.next!= None):
                cur = cur.next
            cur.next = self._Node(v,None)
            
        self._size += 1


#------------------------------------------------------------------------------------
    # Removes and returns the first node of the list
    def pop(self):
        if self._size == 0:
            return None
        else:
            value= self._head.value
            self._head = self._head.next
            self._size -= 1
            return value

        
#------------------------------------------------------------------------------------
    # Returns the value of the first node of the list
    def peek(self):
        
        return self._head.value if self._head else None
        
    

        
#------------------------------------------------------------------------------------
    # Removes the first node of the list with value v and return v
    def remove(self, v):
        if self._size == 0:
            return None
        else: 
            current = self._head
            # if the value of the first node is v
            if current.value == v:
                Removed_Node = current
                self._head = self._head.next
                self._size -= 1  
                return Removed_Node.value
            
            else:
                for i in range(self._size-1):
                    if current.next.value == v:
                        Removed_Node = current.next
                        current.next = current.next.next
                        self._size -= 1       
                        return Removed_Node.value
                    else:
                        current = current.next
        return None
    

### CircularLinkedList

class CircularLinkedList(LinkedList):
    
#------------------------------------------------------------------------------------
    def __init__(self):
        super().__init__()
    
    
#------------------------------------------------------------------------------------
    def __str__(self):
        res = '['
        cur = self._head
        for _ in range(self._size):
            res += str(cur.value) + ', '
            cur = cur.next
    
        return res[0:-2] + ']'
        

#------------------------------------------------------------------------------------
    def __iter__(self):
        current = self._head
        for i in range(self._size):
            output = current.value
            if current != None:
                current = current.next
            yield output


#------------------------------------------------------------------------------------
    # Moves head pointer to next node in list
    def next(self):
        self._head = self._head.next

        
#------------------------------------------------------------------------------------
    # Adds a node of value v to the end of the list
    def append(self, v):
        if not self._head:
            self._head = self._Node(v,None)
        
        else:
            cur = self._head
            for _ in range(self._size - 1):
                cur = cur.next
            cur.next = self._Node(v,self._head)
        
        self._size += 1
        
        
#------------------------------------------------------------------------------------
    # Reverses the next pointers of all nodes to previous node
    def reverse(self):
        
        
        prev = self._head
        cur = self._head.next
        
        while(cur != self._head):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            
        # after the boucl, prev will be the last node
        self._head.next = prev

    
#------------------------------------------------------------------------------------
    # Removes head node and returns its value
    def pop(self):
        cur = self._head
        val = self._head.value
        
        # find the last node
        while(cur.next != self._head):
            cur = cur.next
            
        self._head = self._head.next
        
        # rebuild the cycle
        cur.next = self._head
        
        self._size -= 1
        return val


### Card

class Card:
    def __init__(self, r, s):
        self._rank = r
        self._suit = s

    suits = {'s': '\U00002660', 'h': '\U00002661', 'd': '\U00002662', 'c': '\U00002663'}

    def __str__(self):
        return self._rank + self.suits[self._suit]

    def __eq__(self, other):
        if other != None:
            if self._rank == other._rank and self._suit == other._suit:
                return True
            else:
                if (self._rank == 'A' and other._rank == '1' and self._suit == other._suit):
                    return True

                elif (self._rank == '1' and other._rank == 'A' and self._suit == other._suit):
                    return True
                return False       
        else:
            return False



### Hand

class Hand:
    
#------------------------------------------------------------------------------------
    def __init__(self):
        self.cards = {'s': LinkedList(), 'h': LinkedList(), 'd': LinkedList(), 'c': LinkedList()}

        
    
#------------------------------------------------------------------------------------
    def __str__(self):
        result = ''
        for suit in self.cards.values():
            result += str(suit)
        return result
    
    
#------------------------------------------------------------------------------------
    def __getitem__(self, item):
        return self.cards[item]

    
    
#------------------------------------------------------------------------------------
    def __len__(self):
        result = 0
        for suit in list(self.cards):
            result += len(self.cards[suit])

        return result

    
    
#------------------------------------------------------------------------------------
    def add(self, card):
        self.cards[card._suit].add(card)

        
    
#------------------------------------------------------------------------------------
    def get_most_common_suit(self):
        return max(list(self.cards), key = lambda x: len(self[x]))
    
    
    
#------------------------------------------------------------------------------------
    # Returns a card included in the hand according to
    # the criteria contained in *args and None if the card
    # isn't in the hand. The tests show how *args must be used.
    def play(self, *args):
        if len(args) != 1:
            if args[0] == 's':
                return self.cards['s'].remove(Card(args[1],'s'))
            elif args[0] == 'h':
                return self.cards['h'].remove(Card(args[1],'h'))
            elif args[0] == 'd':    
                return self.cards['d'].remove(Card(args[1],'d'))
            elif args[0] == 'c': 
                return self.cards['c'].remove(Card(args[1],'c'))                
            if args[1] == 's':
                return self.cards['s'].remove(Card(args[0],'s'))
            elif args[1] == 'h':
                return self.cards['h'].remove(Card(args[0],'h'))
            elif args[1] == 'd':    
                return self.cards['d'].remove(Card(args[0],'d'))
            elif args[1] == 'c': 
                return self.cards['c'].remove(Card(args[0],'c'))  
            
        else:
            if args[0] == 's':
                return self.cards['s'].pop()
            elif args[0] == 'h':
                return self.cards['h'].pop()
            elif args[0] == 'd': 
                return self.cards['d'].pop()
            elif args[0] == 'c':
                return self.cards['c'].pop()
            else:
                
                out = self.cards['s'].remove(Card(args[0],'s'))
                if out != None:
                    return out

                out = self.cards['h'].remove(Card(args[0],'h'))
                if out != None:
                    return out

                out = self.cards['d'].remove(Card(args[0],'d'))
                if out != None:
                    return out

                out = self.cards['c'].remove(Card(args[0],'c'))
                if out != None:
                    return out                
               
        return None

#------------------------------------------------------------------------------------


### Deck

class Deck(LinkedList):
    
#------------------------------------------------------------------------------------
    def __init__(self, custom=False):
        super().__init__()
        if not custom:
            # for all suits
            for i in range(4):
                # for all ranks
                for j in range(13):
                    s = list(Card.suits)[i]
                    r = ''
                    if j == 0:
                        r = 'A'
                    elif j > 0 and j < 10:
                        r = str(j+1)
                    elif j == 10:
                        r = 'J'
                    elif j== 11:
                        r = 'Q'
                    elif j == 12:
                        r = 'K'
                    self.add(Card(r,s))
                    

#------------------------------------------------------------------------------------
    def draw(self):
        return self.pop()
    
    
#------------------------------------------------------------------------------------
    def shuffle(self, cut_precision = 0.05):
         # Cutting the two decks in two
        center = len(self) / 2
        k = round(random.gauss(center, cut_precision*len(self)))

        # other_deck must point the kth node in self
        # (starting at 0 of course)
        # other_deck = #TO DO
        other_deck_head = self._head
        for _ in range(k):
            other_deck_head =  other_deck_head.next 

        #TO DO: seperate both lists
        # Merging the two decks together
        
        deck_1_curent = self._head
        for _ in range(k-1):
            deck_1_curent=deck_1_curent.next
        deck_1_curent.next = None
        
        
#------------------------------------------------------------------------------------
        if random.uniform(0,1) < 0.5:
            #switch self._head and other_deck pointers
            current = self._head
            self._head = other_deck_head
            other_deck_head = current
            
        deck_1_current = self._head
        deck_2_current = other_deck_head

        deck_1_End = False
        deck_2_End = False

        while deck_1_End == False or deck_2_End == False:
            if deck_1_current.next == None:
                deck_1_End = True
            else:
                deck_1_temp = deck_1_current.next
                
            if deck_2_current == None:
                deck_2_End = True  
            else:
                deck_2_temp = deck_2_current.next                
            
            if deck_1_End == False and deck_2_End == False: 
                
                # fusion the ndoes
                deck_1_current.next = deck_2_current
                deck_2_current.next = deck_1_temp
                
                # update the current nodes
                deck_1_current = deck_1_temp
                deck_2_current = deck_2_temp
                
            elif deck_1_End == True and deck_2_End == False:
                deck_1_current.next = deck_2_current
                deck_2_current = deck_2_current.next
                deck_1_current = deck_1_current.next
                
            elif deck_1_End == False and deck_2_End == True:
                deck_1_current = deck_1_current.next
            
        return None

    


### Player

class Player():
    def __init__(self, name, strategy='naive'):
        self.name = name
        self.score = 8
        self.hand = Hand()
        self.strategy = strategy

    def __str__(self):
        return self.name

    # This function must modify the player's hand,
    # the discard pile, and the game's declared_suit 
    # attribute. No other variables must be changed.
    # The player's strategy can ONLY be based
    # on his own cards, the discard pile, and
    # the number of cards his opponents hold.
    def play(self, game):
        if(self.strategy == 'naive'):
            
            top_card = game.discard_pile.peek()
            # if the top card is a special card and it's still valid
            if ((top_card == Card('Q','s') or top_card._rank == '2') and game.draw_count != 0):
                
                # if someone decalred the suit, ie, '2' is also the frime of the player who played the top_card
                if game.declared_suit:
                    deux = self.hand.play('2',game.declared_suit)
                    
                else:
                    deux = self.hand.play('2')
                
                # if we have 2 and 2 is also our frime
                if self.score == 2 and deux:
                    game.declared_suit = self.hand.get_most_common_suit()
                    game.discard_pile.add(deux)
                    return game
                    
                # if 2 is not our frime, we simply add it to our discard_pile
                elif deux:
                    game.discard_pile.add(deux)
                    return game
                    
                    
                # if we don't have 2, we have to play queen S.
                queen = self.hand.play('Q','s')
                # if there is a declared_suit, it have to be s if we want to play queen S.
                if game.declared_suit == 's' and queen:
                    game.discard_pile.add(queen)
                    return game
                
                # if there is no  declared_suit, we can just add it.
                elif queen:
                    game.discard_pile.add(queen)
                    return game
                
               
                return game
                
             
            # if top_card is not special
            else:
                suit_to_play = game.declared_suit if game.declared_suit else top_card._suit
                
                
                # we first play the card with same suit
                card_with_same_suit = self.hand.play(suit_to_play)
                
                
                # if the card we play is our frime, we have to put it back
                # because the priority of our frime is lower than other cards with the same suit we have
                if card_with_same_suit and card_with_same_suit._rank == str(self.score):
                    
                    frime = card_with_same_suit
                    
                    # and we try to play another card with same suit
                    card_with_same_suit = self.hand.play(suit_to_play)
                    
                    # put our frime back
                    self.hand[suit_to_play].add(frime)
                    
                
                # if we didn’t find the card with same suit, we then try to play the card with same rank
                if not card_with_same_suit and not game.declared_suit:
                    
                    
                    card_with_same_rank = self.hand.play(top_card._rank)
                    
                    # if we also didn't find the card with same rank, we then try to play frime
                    if not card_with_same_rank:
                        frime = self.hand.play(str(self.score))
                        
                        # if we have no frime , then we have no cards to play in this round.
                        if not frime:
                            return game
                        else:
                            game.declared_suit = self.hand.get_most_common_suit() 
                            game.discard_pile.add(frime)
                
                    else:
        
                        game.discard_pile.add(card_with_same_rank)
                        # if we have card with same rank to play, we have to check if this card is our frime
                        if card_with_same_rank._rank == self.score:
                            
                            # if it is, we can declare a suit for the next player.
                            game.declared_suit = self.hand.get_most_common_suit()
                            
                        # case for AS is special.
                        elif (card_with_same_rank._rank == 'A' or card_with_same_rank._rank == '1') and self.score == 1:
                            
                            game.declared_suit = self.hand.get_most_common_suit()
                            
                        else:
                            game.declared_suit = ''
                        
                    
                # if there is a declared suit but we have no cards with the same suit to play
                elif not card_with_same_suit and game.declared_suit:
                    
                    # we try to play our frime
                    frime = self.hand.play(str(self.score))
                    if not frime:
                        return game
                    else:
                        game.declared_suit = self.hand.get_most_common_suit() 
                        game.discard_pile.add(frime)
                    
                # if we have the card with same suit
                elif card_with_same_suit:
                    game.discard_pile.add(card_with_same_suit)
                    
                    # we also have to check if this card is our frime
                    if card_with_same_suit._rank == self.score:

                        game.declared_suit = self.hand.get_most_common_suit()

                    elif (card_with_same_suit._rank == 'A' or card_with_same_suit._rank == '1') and self.score == 1:

                        game.declared_suit = self.hand.get_most_common_suit()

                    else:
                        game.declared_suit = ''

            return game

        else:
            # TO DO(?): Custom strategy (Bonus)
            
            pass
        

### Game

class Game:
    def __init__(self):
        self.players = CircularLinkedList()

        for i in range(1,5):
            self.players.append(Player('Player '+ str(i)))

        self.deck = Deck()
        self.discard_pile = LinkedList()

        self.draw_count = 0
        self.declared_suit = ''
        
        
 #------------------------------------------------------------------------------------       
    def __str__(self):
        result = '--------------------------------------------------\n'
        result += 'Deck: ' + str(self.deck) + '\n'
        result += 'Declared Suit: ' + str(self.declared_suit) + ', '
        result += 'Draw Count: ' + str(self.draw_count) + ', '
        result += 'Top Card: ' + str(self.discard_pile.peek()) + '\n'

        for player in self.players:
            result += str(player) + ': '
            result += 'Score: ' + str(player.score) + ', '
            result += str(player.hand) + '\n'
        return result

    
#------------------------------------------------------------------------------------
    # Puts all cards from discard pile except the 
    # top card back into the deck in reverse order
    # and shuffles it 7 times
    def reset_deck(self):
        
        

        if len(self.discard_pile) != 0:
            TopCard = self.discard_pile.pop()
            
            # we put the card from the discard_pile back to the deck.
            for _ in range(len(self.discard_pile)):
                self.deck.append(self.discard_pile.pop())
                
            # and finally, we put the top card back
            self.discard_pile.add(TopCard)

        
        for _ in range(7):
            self.deck.shuffle()
            
        
#------------------------------------------------------------------------------------
    # Safe way of drawing a card from the deck
    # that resets it if it is empty after card is drawn
    def draw_from_deck(self, num):
        
                
        player = self.players.peek()
        
        if self.deck.isEmpty():
            self.reset_deck()  
    
        for _ in range(num):
            player.hand.add(self.deck.draw())
            if self.deck.isEmpty():
                self.reset_deck()
            
    
            
#------------------------------------------------------------------------------------
    def start(self, debug=False):
        # Ordre dans lequel les joeurs gagnent la partie
        result = LinkedList()
        self.reset_deck()
        
        # Each player draws 8 cards
        for player in self.players:
            for i in range(8):
                player.hand.add(self.deck.draw())

        self.discard_pile.add(self.deck.draw())

        transcript = open('result','w',encoding='utf-8')
        if debug:
            transcript = open('result_debug','w',encoding='utf-8')

            
        while(not self.players.isEmpty()):
            
            if debug:
                transcript.write(str(self))
            # player plays turn
            player = self.players.peek()

            old_top_card = self.discard_pile.peek()

            self = player.play(self)

            new_top_card = self.discard_pile.peek()

            # Player didn't play a card => must draw from pile
            if new_top_card == old_top_card:
                
                if self.draw_count != 0:
                    self.draw_from_deck(self.draw_count)
                    transcript.write(player.name + " draws " + str(self.draw_count) + ' cards' + '\n')
                    
                else:
                    self.draw_from_deck(1)
                    transcript.write(player.name + " draws " + '1' + ' card' + '\n')
                    
                # we have to make the draw_count to zero when the special card is no longer valid.
                self.draw_count = 0
                    
            # Player played a card
            else:
                
                # Skip flag
                skip = False
                
                transcript.write(player.name + " plays " + str(new_top_card) + '\n')
                
                # traitement for special card that the player played
                if new_top_card._rank == '2':
                    self.draw_count += 2
                
                elif new_top_card == Card('Q','s'):
                    self.draw_count += 5
                    
                elif new_top_card._rank == 'A' or new_top_card._rank == '1':
                    self.players.reverse()
                    
                elif str(new_top_card)[0] == 'J':
                    skip = True
                    
                        
                
#------------------------------------------------------------------------------------                
            # Handling player change
            # Player has finished the game
            if len(player.hand) == 0 and player.score == 1:
                place = 5 - len(self.players)
                output = str(player) + f" finishes in position {place}\n"
                transcript.write(output)
                finished = True
        
                
            else:
                
                # Finiah flag
                finished = False
                
                # Player is out of cards to play
                if len(player.hand) == 0:

                    player.score -= 1
                    self.draw_from_deck(player.score)               
                    output = str(player) + " is out of cards to play! " + str(player) + f" draws {player.score} cards\n"
                    transcript.write(output)
                    

                elif len(player.hand) == 1:
                    output = "*Knock, knock* - "+ str(player) + " has a single card left!\n"
                    transcript.write(output)
                    
#------------------------------------------------------------------------------------            

            # Handles player sequence
            if finished == True:
                self.players.pop()
                finished = False
                if skip == True:
                    self.players.next()
                    skip = False
            else:
                if skip == True:
                    self.players.next()
                    self.players.next()
                    skip = False
                else:                  
                    self.players.next()   
            
            if self.players._size == 1:
                output = str(self.players.peek()) + f" finishes last\n"
                transcript.write(output)
                self.players.pop()
                return result
            
        return result


#### Testing

if __name__ == '__main__':
    '''
    random.seed(420)
    game = Game()
    print(game.start(debug=True))

    # TESTS
    # LinkedList
    l = LinkedList()
    l.append('b')
    l.append('c')
    l.add('a')

    assert(str(l) == '[a, b, c]')
    assert(l.pop() == 'a')
    assert(len(l) == 2)
    assert(str(l.remove('c')) == 'c')
    assert(l.remove('d') == None)
    assert(str(l) == '[b]')
    assert(l.peek() == 'b')
    assert(l.pop() == 'b')
    assert(len(l) == 0)
    assert(l.isEmpty())

    # CircularLinkedList
    l = CircularLinkedList()
    l.append('a')
    l.append('b')
    l.append('c')

    assert(str(l) == '[a, b, c]')
    l.next()
    assert(str(l) == '[b, c, a]')
    l.next()
    assert(str(l) == '[c, a, b]')
    l.next()
    assert(str(l) == '[a, b, c]')
    l.reverse()
    assert(str(l) == '[a, c, b]')
    assert(l.pop() == 'a')
    assert(str(l) == '[c, b]')

    # Card
    c1 = Card('A','s')
    c2 = Card('A','s')
    # Il est pertinent de traiter le rang 1
    # comme étant l'ace
    c3 = Card('1','s')
    assert(c1 == c2)
    assert(c1 == c3)
    assert(c3 == c2)

    # Hand
    h = Hand()
    h.add(Card('A','s'))
    h.add(Card('8','s'))
    h.add(Card('8','h'))
    h.add(Card('Q','d'))
    h.add(Card('3','d'))
    h.add(Card('3','c'))

    assert(str(h) == '[8♠, A♠][8♡][3♢, Q♢][3♣]')
    assert(str(h['d']) == '[3♢, Q♢]')
    assert(h.play('3','d') == Card('3','d'))
    assert(str(h) == '[8♠, A♠][8♡][Q♢][3♣]')
    assert(str(h.play('8')) == '8♠')
    assert(str(h.play('c')) == '3♣')
    assert(str(h) == '[A♠][8♡][Q♢][]')
    assert(h.play('d','Q') == Card('Q','d'))
    assert(h.play('1') == Card('A','s'))
    assert(h.play('J') == None)

    # Deck
    d = Deck(custom=True)
    d.append(Card('A','s'))
    d.append(Card('2','s'))
    d.append(Card('3','s'))
    d.append(Card('A','h'))
    d.append(Card('2','h'))
    d.append(Card('3','h'))

    random.seed(15)

    temp = copy.deepcopy(d)
    assert(str(temp) == '[A♠, 2♠, 3♠, A♡, 2♡, 3♡]')
    temp.shuffle()
    assert(str(temp) == '[A♠, A♡, 2♠, 2♡, 3♠, 3♡]')
    temp = copy.deepcopy(d)
    temp.shuffle()
    assert(str(temp) == '[A♡, A♠, 2♡, 2♠, 3♡, 3♠]')
    assert(d.draw() == Card('A','s'))
    '''


