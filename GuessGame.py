
user_guess = ""
answer = "Apple"
count = 0


while user_guess is not answer:
    user_guess = input("Enter your guess: ")
    count += 1
    if user_guess == answer:
        print("You guessed it right, secret word is " + user_guess + " it took " + str(count) + " times.")

