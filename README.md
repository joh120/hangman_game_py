Hangman game

A hangman game that prompts user to guess correctly the characters of a random word. 
The user will be given a hint of the amount of letters for the random word that they are guessing.
For every wrong character guessed a part of the hangman ascii art gets displayed. The game keeps 
going either until the user guesses all the characters correctly or even the hangman ascii art gets 
fully displayed.

Inspiration

The popular hangman game in which a one person put down a hint in terms if dashes to represent a word. 
Another person guesses letters of the word the person who knows the word with every wrong guess 
lead to draw another part of the hangman. The game ends either when the person guessing gets all the letters right 
or the hangman becomes complete 

Challenges we ran into 

The words being guessed if was a word sperated by a space was not properly allowing the user ever guess right even if all the 
characters they guessed were right. This challenge was easily solved and the game properly allow users to get win the game even all 
the characters there guessed is correct


Hangman pseudo code 

This is the pseudo code that I created for the game:

first hangman dictionary depicts the hangman ascii art 

def clue_display(): take in underscores and seperates each underscore with a space.
The amount of underscores is determined by the length of our random word

def answer_display(): this takes in the random word and seperates in with a space. 
This will shown if all characters by the user is guessed correctly. Also, the answer will shown 
at the end of the game the user guessed too many characters incorrectly. 

def hangman_display(): this takes in the wrong guesses and display a part of the hangman ascii art 
for every wrong guess

def main(): this takes a random word from a list of words and prompts the user to guess correct characters of 
the random word. For every character not a alphabetical the user will get a print of invalid input. 
In addition to any guesses more than one character will a user get a print of invalid input. 

If a charcter is already guess the user will get a print of that character as already been guessed.
If all the characters have been guessed correctly the user will get a print of "You win". Otherwise if 
hangman ascii art is fully displayed the user will get a print of "You lose!"
