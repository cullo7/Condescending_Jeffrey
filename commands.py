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
    else:
        print "Here is a list of my possible commands and their how to use them"
        for com in command_desc.keys():
            print '<{}> : {}'.format(com, command_desc[com])
        print "Format: [Question word(s)]...[noun/verb]"

def get_history():
    print "get history"
    db.execute("SELECT * FROM commands") 
    rows = db.fetchall()
    for row in rows:
        for col in row:
            print "%s," % col
        print "\n"

def choose_history(num):
    print "choose history"
    db.execute("SELECT command FROM commands WHERE id = (?)", num)
    rows = db.fetchall()
    for row in rows:
        for col in row:
            print "%s," % col
        print "\n"

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
    }

    args = args_in.split("...")
    print args

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
        if len(args[1]) == 0:
            command_functions[command]()
        else:    
            command_functions[command](args[1:])
