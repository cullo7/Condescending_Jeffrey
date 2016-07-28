import functions as fn
import subprocess
import sqlite3
import os
import sys
import time

command_desc = {
    "where is" : "Enter a city here and Jeffrey will tell you what country it is in and on what continent", 
    "how old is" : "Enter a full name here and Jeffrey will do his best to find their age", 
    "how good is" : "Enter movie title here", 
    "how can i" : "Ever been wondering how to do something? Alas enter that 'thing' here and Jeffrey will show you how", 
    "who am i" : "If you are feeling lost or going through a mid/quarter-life crisis Jeffrey is here to help you", 
    "i want to see" : "Enter whatever it is that you would like to see pictures of", 
    "tell me about" : "Enter a subject you are curious about",
    "show my history" : "If you ever want to see the history of all your commands",
    "choose command" : "Choose a command from your history to execute again",
    "inspire me" : "Returns an inspirational quote to brighten your day",
    "get insult" : "Returns a smashing insult if you're in need",
    "help" : "self explanatory"
}

db_file = ".commands_data.db"
commands_db = sqlite3.connect(db_file)
db = commands_db.cursor()
db.execute('''CREATE TABLE IF NOT EXISTS commands
                (command text, id int)''')
commands_db.commit()
current_command_id = 0

def help(choice = 0):
    if choice == 1:
        print "You need to enter three dots and an argument, its so easy, just do it"
        little_help()
    else:
        print "Here is a list of my possible commands and their how to use them"
        for com in command_desc.keys():
            print '<{}> : {}'.format(com, command_desc[com])
        print "Remember each question and noun/verb should be separate by an ellipses like so.."
        print "Format: [Question word(s)]...[noun/verb]"

def little_help():
    time.sleep(1)
    print "Bruh, the format is this -> [Question word(s)]...[noun/verb]"
    time.sleep(1)
    print "Enter help and I'll show you what I got in my arsenal if you want"    
    time.sleep(1)

def get_history(nothing):
    if len(nothing) != 0:
        print "I'll let this one slide, but next time don't add arguments to show my history, Imbecile!"
    print "get history"
    db.execute("SELECT * FROM commands") 
    rows = db.fetchall()
    for row in rows:
        print '{}. {}'.format(row[1], row[0])
        print ""

def choose_history(num):
    print "choose history"
    db.execute("SELECT command FROM commands WHERE id = (?)", num)
    row = db.fetchone()
    execute(row[0])

def execute(args_in):
    """
        Handles command by either throwing an exception or calling
        a function. On quit, the database is cleared 
    """
    if args_in == 'quit':
        db.execute("DELETE FROM commands")
        commands_db.commit()
        exit(1)
    
    # logging commands in SQL database
    global current_command_id
    current_command_id +=1
    db.execute("INSERT INTO commands \
                VALUES (?, ?)", (args_in, current_command_id))
    commands_db.commit()
    
    command_functions = {
        "where is" : fn.where_is, 
        "how old is" : fn.how_old_is, 
        "how good is" : fn.how_good_is, 
        "how can i" : fn.how_can_i, 
        "who am i" : fn.who_am_i, 
        "i want to see" : fn.i_want_to_see, 
        "tell me about" : fn.tell_me_about,
        "show my history" : get_history,
        "choose command" : choose_history,
        "get insult" : get_insult,
        "inspire me" : inspire_me
    }

    args = args_in.split("...")

    command = args[0]
    if command not in command_functions.keys():
        fn.error("Invalid command: '{}'".format(args[0]))
    elif len(args) == 1:
	help(1)
    elif command == "help":
	if len(args) > 2:
	    fn.error("Don't put arguments after 'help', dingus")
	else:
	    help()
    else:     
        command_functions[command](args[1:])
