print("Please think of a number between 0 and 100 !") 
step = 0 
min = 0 
max = 100 
x = int(max / 2) 
while x:
    print("Is your secret number " + str(x) + " ?") 
    s = raw_input("""Enter 'h' to indicate the guess is too high.
                    Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.""")
     
    if s == 'l':
        min = x 
        x = int((max + min) / 2)
    elif s == 'h':
        max = x
        x = int((max + min) / 2)
    elif s == 'c':
        break
    else:
        print("Sorry, I did not understand your input.")
        
print("Game over ! Your secret number is : " + str(x))