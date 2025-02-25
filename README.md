Hangman game

A hangman game that prompts the user to guess correctly the characters of a random word. 
The user will be given a hint of the amount of letters for the random word that they are guessing.
For every wrong character guessed a part of the hangman ascii art gets displayed. The game keeps 
going either until the user guesses all the characters correctly or that the hangman ascii art gets 
fully displayed.

Inspiration

The popular hangman game in which a one person put down a hint in terms of dashes to represent a word. 
Another person guesses letters of the word and with every wrong guess leading drawing a part of the hangman. 
The game ends either when the person guessing gets all the letters right 
or the hangman drawing becomes complete.

Challenges we ran into 

The words being guessed if was a word seperated by a space was not properly allowing the user to win even if all the 
characters they guessed were right. This challenge was easily solved and the game now properly allow users to win the game if there 
guess all the characters correctly.


Hangman pseudo code 

This is the pseudo code that I created for the game:

first the hangman dictionary depicts the hangman ascii art. 

def clue_display(): take in underscores and seperates each underscore with a space.
The amount of underscores is determined by the length of our random word.

def answer_display(): this takes in the random word and seperates it with a space. 
This will shown if all characters by the user is guessed correctly. Also, the answer will be shown 
at the end of the game whether the user win or lose. 

def hangman_display(): this takes in the wrong guesses and display a part of the hangman ascii art 
for every time they make a wrong guess.

def main(): this takes a random word from a list of words and prompts the user to guess the correct characters of 
the random word. For every character guessed that is not alphabetical the user will get a print of invalid input. 
In addition to any guesses more than one character will a user get a print of invalid input. 

If a character is already guessed the user will get a print of that character as already been guessed. Characters 
that have already been guessed won't count as a wrong guess for the user.In the end if all the characters have been 
guessed correctly the user will get a print of "You win". Otherwise the 
hangman ascii art will become fully displayed and then the user will get a print of "You lose!"
