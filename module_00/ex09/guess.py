# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alvgomez <alvgomez@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/20 11:13:06 by alvgomez          #+#    #+#              #
#    Updated: 2023/03/20 12:02:13 by alvgomez         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import randint

def where_the_number(numb, guess):
	if guess > numb:
		print("To high!")
	elif guess < numb:
		print("To low!")
	elif guess > 99 or guess < 1:
		print("The number is not between 1 and 99")

def check(guess):
	if guess == "exit":
		print("Goodbye!")
		return 1
	elif guess.isdigit() == 0:
		return 2
	return 0

if __name__ == "__main__":
	print('''This is an interactive guessing game! 
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game. 
Good luck!
	''')
	numb = randint(1, 99)
	tries = 0
	print("What's yout guess between 1 and 99?")
	guess = input(">> ")
	if check(guess) == 1:
		exit()
	elif check(guess) == 2:
		print("That's not a number")
	else:
		guess = int(guess)
		where_the_number(numb, guess)
		tries = 1
		if guess == numb:
			print("Congratulations! You got it on your firs try!")
			exit()
	while guess != numb:
		print("What's yout guess between 1 and 99?")
		guess = input(">> ")
		if check(guess) == 1:
			exit()
		elif check(guess) == 2:
			print("That's not a number")
		else:
			guess = int(guess)
			where_the_number(numb, guess)
			tries += 1
	print("Congratulations, you've got it!")
	print(f"You won in {tries} attempts")