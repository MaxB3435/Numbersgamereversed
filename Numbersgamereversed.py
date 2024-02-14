import random
ng = 1

h = 64
l = 1
g = random.randint(l,h)

#print ('Välj ett nummer')
#number = int(input())
number = random.randint(l,h)
print(number)
while True:
    if g != number:
        ng = ng +1
        print(g)
        if g > number:
            print('Nix, lägre')
            h = g - 1
            g = random.randint(l,h)
        elif g < number:
            l = g + 1
            print('Nix, högre')
            g = random.randint(l,h)
    else:
         print('Jag klarade spelet på', ng,'gissningar!')
         exit()

    