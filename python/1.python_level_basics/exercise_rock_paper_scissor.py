import random

while True:
    player=input('choose between(rock, papper,scissor): ')
    options =['rock','paper','scissor']
    computer = random.choice(options)
    
    print(f'you  choose {player}, and the compuer choose {computer}')
    
    if player == computer:
        print('tied...')
    
    elif player =='rock':
        if computer == 'scissor':
            print('you win')
    
        else:
            print('you loose')
        
    elif player == 'paper':
        if computer =='rock':
            print('you win')
    
        else:
            print('you loose')
    
    elif palyer == 'scissor':
        if computer =='rock':
            print('you win')
            
        else:
            print('you loose')
            
    continue