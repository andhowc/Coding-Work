#Deck of cards

import random
suits =["♠","♥","♦","♣"]
ranks =["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

cards=[]

for i in range(len(suits)):
    deck=[]
    for j in range(len(ranks)):
        card=suits[i]+ranks[j]
        cards.append(card)

        
print(cards, '\n')

#␣Generate␣a␣card␣with␣a␣suit␣and␣value


suit= suits[random.randint(1,4)-1]
rank=ranks[random.randint(1,13)-1]
card=suit+rank
print (card, '\n')

#␣and␣append␣to␣cards
cards.append("Joker")

print(cards, '\n')

#␣Shuffle␣cards␣and␣assign␣it␣to␣deck

deck =random.sample(cards, len(cards))
print(deck, '\n')

#␣Shuffle␣cards␣and␣assign␣it␣to␣deck

random.shuffle(cards)
print(cards, '\n')
