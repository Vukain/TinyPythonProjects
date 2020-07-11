import random

playing = True

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        return self.deck

    def show_cards(self):
        cards_list = []
        for elem in self.deck:
            cards_list.append(str(elem))
        print(cards_list)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        self.deck.pop(0)


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):

        self.cards.append(deck.deck[card])
        self.value += deck.deck[card].value
        if deck.deck[card].value == 11:
            self.aces += 1

    def adjust_for_ace(self):
        if self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
            print('Ace as 1 point!')


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def take_bet(self):

        while True:
            try:
                zaklad = int(input("\nHow much do you want to bet?\n"))
                if self.total >= zaklad:
                    self.bet = zaklad
                    print('Bet accepted\n\n')
                    break
                else:
                    raise ValueError
            except:
                print('Bet too big')
                continue

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def hit(deck, hand):
    hand.add_card(0)
    deck.deal()


def hit_or_stand(deck, hand):
    x = True
    while x:
        print(f'\nYou currently have {hand.value} points.')
        show_ca(player)
        hist = input('Wanna hit or stand? Enter "Hit" or "Stand"\n')

        if hist[0].lower() == 's':
            x = False
            break

        elif hist[0].lower() == 'h':
            hit(deck, hand)
            player.adjust_for_ace()
            if player.value <= 21:
                continue
            else:
                x = False

        else:
            print('Wrong input, enter "Hit" or "Stand"')
            continue


def dealer_hit(deck, hand):
    global playing
    print('\n\nDealer turn!')
    while playing:
        if hand.value <= 17:
            hit(deck, hand)
            dealer.adjust_for_ace()
            continue
        else:
            # print(f'Dealer have {hand.value} points')
            break


def show_some(player, dealer):
    cards_of_player = []
    cards_of_dealer = []

    for elem in player.cards:
        cards_of_player.append(str(elem))
    # print('Sum of player cards: ',player.value)
    # print('You have ',cards_of_player)

    for elem in dealer.cards:
        cards_of_dealer.append(str(elem))
    print('Dealer have one hidden card and: ', cards_of_dealer[1:])


def show_all(player, dealer):
    cards_of_player = []
    cards_of_dealer = []

    for elem in player.cards:
        cards_of_player.append(str(elem))
    print('Sum of player cards: ', player.value)
    print('You have ', cards_of_player)

    for elem in dealer.cards:
        cards_of_dealer.append(str(elem))
    print('Sum of dealer cards: ', dealer.value)
    print('Dealer have ', cards_of_dealer)


def show_ca(player):
    cards_of_player = []

    for elem in player.cards:
        cards_of_player.append(str(elem))
    print('You have ', cards_of_player)


def player_busts():  # powyzej 21
    chips.lose_bet()
    print('\nYOU BUSTED and lost your bet!\n')


def player_wins():  # gracz blizej 21
    chips.win_bet()
    print('\nYOU WON and doubled your bet!\n')


def dealer_busts():  # dealer powyzej 21
    chips.win_bet()
    print('\nDEALER BUSTED, you won and doubled your bet!\n')


def dealer_wins():  # dealer blizej
    chips.lose_bet()
    print('\nDEALER WON, you lost your bet!\n')


def push():  # maja tyle samo, zwrot zakladu
    chips.bet = 0
    print('\nDRAW, your bet was returned!\n')


while True:
    print(10 * '\n')
    print('''
     ***************************************   
     *  ####   #       ###    ###   #  ##  *  
     *  #   #  #      #   #  #   #  # #    *    
     *  ####   #      #####  #      #      *    
     *  #   #  #      #   #  #   #  # #    *  
     *  ####   #####  #   #   ###   #  ##  *
     *                                     *
     *         #####   ###    ###   #  ##  *  
     *             #  #   #  #   #  # #    *     
     *             #  #####  #      #      *    
     *          #  #  #   #  #   #  # #    *    
     *           ###  #   #   ###   #  ##  *
     ***************************************       
    ''')
    print('{:*^50}'.format('Welcome to Black Jack'))
    print(
        '\nWhoever gets closer to 21 without going over wins!\nAces count as 11 or 1 - depending on the situation\nYou can also use Y/N/H/S while making choices.')
    print('\n{:^50}'.format("Let's play!"))
    print(10 * '\n')

    chips = Chips()

    while playing:
        print(f'You currently have {chips.total} chips.')
        chips.take_bet()

        deck = Deck()
        deck.shuffle()

        player = Hand()
        dealer = Hand()

        hit(deck, player)
        hit(deck, player)

        hit(deck, dealer)
        hit(deck, dealer)

        show_some(player, dealer)
        print('\n')

        player.adjust_for_ace()
        dealer.adjust_for_ace()

        if player.value <= 21:
            hit_or_stand(deck, player)

        if (player.value <= 21 and dealer.value <= 21) and (21 - player.value < 21 - dealer.value):
            dealer_hit(deck, dealer)

        print(2 * '\n')
        show_all(player, dealer)

        if player.value > 21:
            player_busts()
        elif dealer.value > 21:
            dealer_busts()
        elif dealer.value == player.value:
            push()
        elif player.value > dealer.value:
            player_wins()
        else:
            dealer_wins()

        if chips.total > 0:
            nextru = input('\nKeep playing? Yes/No\n')

            if nextru.lower() == 'yes' or nextru.lower() == 'y':
                continue
            else:
                print("\nYou don't want to keep playing.")
                print(f"You're leaving the table with {chips.total} chips.")
                playing = False

        else:
            print("\nYou don't have funds to keep playing.")
            playing = False

    endi = input('\nGame Over, want to play again? Yes/No\n')

    if endi.lower() == 'yes' or endi.lower() == 'y':
        playing = True
        continue
    else:
        print('\nBye,bye!')
        break