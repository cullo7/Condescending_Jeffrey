# Twelve_Questions

Condescending_Jerry is an interactive bot written in python. He is able to answer a very limited amount of questions, but will certainly answer them
in a rude way. Another crucial attribute of Jerry is that he can handle almost any input so as to simulate a real human more closely

###Details:
* Commands have to be formatted: [Commmand]...[noun/verb]
* All commands are stored in sqlite3 database
* To stop program simply enter 'quit' (this flushes command history)
* Jeffrey has a 'temper' that will increase when you enter incorrect commands and decrease with correct ones
* Jeffrey will try to guess what command you wanted amd/or pinpoint the problem in your entry

###Commands:
| Command         | Function                            | Example                     |
| ----------------|:-----------------------------------:|-----------------------------|
| where is        | finds country and continent of city | where is...Quebec           |
| how old is      | finds age of person                 | how old is...Charelie Sheen |
| how good is     | returns rating of movie             | how good is...Interstellar  |
| how can i       | routes you to video of task         | how can i...start a fire    |
| who am i        | tells you who you are               | who am i...                 |
| i want to see   | shows you pictures of subject       | i want to see...a dog       |
| show history    | prints command history              | show history...             |
| clear history   | clears command history              | clear history...            |
| execute history | executes history command            | execute history...1         |
| inspire me      | returns inspirational quotes        | inspire me...               |
| get insult      | returns a world class insult        | get insult...               |
| help            | shows help menu                     | help                        |

###Goals:
* Responsive bot that talks in vernacular or "slang" in order to appear semi-humanlike
* Perform useful and interesting functions for the user
* Be able to handle any possible input from the user

###Dependencies:
* subprocess
* termcolor
* requests
* lxml
* urllib2
* webbrowser
* Pillow
* random

###External Programs:
* navigator.py - helpful python script that allows you to navigate an html page recieved back from a server after a request
  * oftentimes an html pages retrieved from the requests module isn't exactly the same as the one seen in the source in your browser.
* find_city.cpp - c++ program that searches through a text file with cities of the world, then looks up their two letter country code
* no_quotes.c - program I used to clean the text files I downloaded so I could parse them easier

> Dependencies can be installed with pip or found online

###Run:
* python main.py or ./run.sh

Written by Aiden Cullo(cullo7)
