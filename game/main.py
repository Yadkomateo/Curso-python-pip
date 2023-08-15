#Rock, paper or scissors
import random

options = ('piedra','papel','tijera')

computer_wins = 0
user_wins = 0

rounds = 1
print(" Welcome PIEDRA PAPEL O TIJERA EMPECEMOS HUMANO 🤔")

while True:
    
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
    
    print("computer_wins💻",computer_wins)
    print("User_wins🧔👶",user_wins)
    

    user_option = input('piedra, papel o tijera =>')
    computer_option = random.choice(options)
    
    
    
    if  not user_option in options:
        print('Eso que joda es seleccione  algo valido ')
        continue
    
    print('user option=>', user_option)
    print('Computer options=>')
    if user_option == computer_option:
        print('Empate!!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')
            print('User gana .l.')
            user_wins += 1
        else:
            print('papel gana ala piedra')
            print('Computer gana')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')  
            print ('User win')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('computador gana')
            computer_wins += 1
    
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')  
            print ('User win')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('computadora gana')
            computer_wins += 1
    if computer_wins == 3:
        print("El ganador es la Cpu")
        break
    if user_wins == 3:
        print("Usuario es el king")
        break
            
    rounds +=1
