import random, time, sys
print('I can guess your age!')
time.sleep(1)
print('Type "Ok" to begin!')
answer = input()
answer = answer.lower()                                                         #removes case sensitivity
while True:
    if answer == 'ok':
        time.sleep(1)
        print('''Let me know if the number is "higher", "lower", or "correct"!''')#start game here
        guess = int(random.randint(0, 100))
        floor = 0                                                               #initial definitions for var's: floor and ceiling to allow for check if only one input ever entered
        ceiling = 100
        print('Are you ' + str(guess) + '?')
        age = input()                                                           #every input needs 5 options: higher, lower, correct, quit and unknown input
        age = age.lower()
        if age == 'higher':
            if guess > 98:                                                      #initial cheating check
                print('Now now, this is no fun if you lie.')
                print('Let\'s try again! Or enter "Quit" to quit!')
                continue
            else:
                floor = guess                                                   #sending player to higher loop with current guess defined as the new number floor
                ceiling = 100                                                   #defines ceiling as a maximum of 100
                break
        elif age == 'lower':
            if guess < 2:
                print('Now now, this is no fun if you lie.')
                print('Let\'s try again! Or enter "Quit" to quit!')
                continue
            else:
                ceiling = guess                                                 #sends player to lower loop with current guess defined as new number ceiling
                floor = 0                                                       #defines floor as a minimum of 0
                break
        elif age == 'correct':                                                  #ends the game
            print('Aha! I told you I could guess it!')
            print('Thanks for playing!')
            time.sleep(1)
            sys.exit()
        elif age == 'quit':
            print('Goodbye!')
            time.sleep(1)
            sys.exit()
        else:
            print('Unknown input! Let\'s try again!')
            print('If you\'d like to quit, type "Quit"')
            answer == 'ok'                                                      #restarts loop with answer input as ok string
            continue                                                            
    else:
        print('Oops! Please type "Ok" to begin!')                               #if anything other than ok is input this is selected
        print('If you\'d like to quit, type "Quit"')
        answer = input()
        answer = answer.lower()
        if answer == 'ok':                                                      #restarts the while loop with "ok" set to answer var
            continue                                                            
        elif answer == 'quit':                                                  #quits the program
            print('Goodbye!')
            time.sleep(1)
            sys.exit()
        else:
            continue                                                            #restarts the while loop with no defined answer

while True:
    while age == 'higher':
                                                                                #higher guess loop here
        guess = int(random.randint((floor + 1), ceiling))                       #rolls for random between defined values of floor and ceiling (+1 on the floor so it isn't the same number)
        print('Are you ' + str(guess) + '?')
        age = input()
        age = age.lower()
        if age == 'higher':                                                     #starts new higher loop with floor defined as current guess
            if (guess + 1) >= ceiling:                                          #slightly more complicated cheating check
                print('Now now, this is no fun if you lie.')
                print('Let\'s try again! Or enter "Quit" to quit!')
                continue
            else:
                floor = guess
                continue
        elif age == 'lower':                                                    #ends higher loop and falls into lower loop with ceiling defined as current guess
            if (guess - 1) <= floor:
                print('Now now, this is no fun if you lie.')
                print('Let\'s try again! Or enter "Quit" to quit!')
                continue
            else:
                ceiling = guess
                break
        elif age == 'correct':
            print('Aha! I told you I could guess it!')
            print('Thanks for playing!')
            time.sleep(1)
            sys.exit()
        elif age == 'quit':
            print('Goodbye!')
            time.sleep(1)
            sys.exit()
        else:
            print('Uh oh, let\'s try again!')
            print('Or type quit to quit!')
            time.sleep(1)
            print('Are you ' + str(guess) + '?')                                #should allow loop to restart, seems to do nothing
            age = input()
            age = age.lower()
            continue
        

    while age == 'lower':
                                                                                #lower guess loop here
        guess = int(random.randint(floor, (ceiling - 1)))                       #rolls for random between defined values of floor and ceiling (-1 on ceiling so it won't guess same number)
        print('Are you ' + str(guess) + '?')
        age = input()
        age = age.lower()
        if age == 'higher':                                                     #ends lower loop and restarts higher loop with floor defined as current guess
            if (guess + 1) >= ceiling:
                print('Now now, this is no fun if you lie.')
                print('Let\'s try again! Or enter "Quit" to quit!')
                continue
            else:
                floor = guess
                break
        elif age == 'lower':                                                    #starts new lower loop with ceiling defined as current guess
            if (guess - 1) <= floor:
                print('Now now, this is no fun if you lie.')
                print('Let\'s try again! Or enter "Quit" to quit!')
                continue
            else:
                ceiling = guess
                continue
        elif age == 'quit':
            print('Goodbye!')
            time.sleep(1)
            sys.exit()
        elif age == 'correct':
            print('Aha! I told you I could guess it!')
            print('Thanks for playing!')
            time.sleep(1)
            sys.exit()
        else:
            print('Uh oh, let\'s try again!')
            print('Or type quit to quit!')
            time.sleep(1)
            print('Are you ' +str(guess) + '?')
            age = input()
            age = age.lower()
            continue

