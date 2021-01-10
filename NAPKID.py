
#Page accueil
print('Login')
print('Email:')
User_Mail = input()
print('Username:')
User_Name = input()
print('Number of places in vehicule:')
User_Num_Place = int(input())
print('Telephone number:')
User_Telephone = input()
print('Welcome')

#map#
import random
Num_Random = random.randint(0, 20)
print('Please give me your coordinates')
print('X coordinate:')
User_X = int(input())
print('Y coordinate:')
User_Y = int(input())
Close_Random = []
for _ in range(Num_Random):
    Random_X= random.randint(User_X-100,User_X+25)
    #print('a', Random_X)
    Random_Y= random.randint(User_Y-100,User_Y+50)
    #print(Random_Y)
    if abs(User_Y-Random_Y)<=25 and abs(User_X-Random_X)<=25:
        Random_Coor = list((Random_X, Random_Y))
        Close_Random.append(Random_Coor)
if bool(Close_Random) == True:
    print('People close to you:')
    print(Close_Random)
else:
    print('Nobody is close')

#Voiture pleine#
print('Please enter the amount of passengers:')
for i in range(999999):
    num_Passengers = int(input())
    Space_Left = int(User_Num_Place - num_Passengers)
    if Space_Left == 0:
        print('No space left')
        break
    elif Space_Left <= 0:
        print('Error 420, please insert the right amount')
    else: 
        print('There is '+ str(Space_Left) + ' spaces left')
        break

#Homepage
print('HOMEPAGE')
print('Username:'+User_Name)
print('no.places left: '+ str(Space_Left))
print('You have '+ str(num_Passengers) + ' passengers in your vehicule')
if num_Passengers > 50:
    print('Mission NapKid Success;') 
    print(' AUTODESTRUCT IN 5 SECONDS')

