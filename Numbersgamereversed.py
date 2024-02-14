import random
ng = 1
g = 0


#print ('Välj ett nummer')
#number = int(input())
number = random.randint(1,100)
print(number)
while True:
    if g != number:
        g = random.randint(1,100)
        ng = ng +1
        print(g)
        if g > number:
            #print(g)
            print('Nix, lägre')
        elif g < number:
            #print(g)
            print('Nix, högre')
        else:
            print('Jag klarade spelet på', ng,'gissningar!')
            exit()

    