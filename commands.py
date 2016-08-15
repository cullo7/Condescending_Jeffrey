import functions as fn
import subprocess
import sqlite3
import os
import sys
import time

'''

Contains database commands and interaction. Also handles execution of command entered by either
delegating to function file or by refusing it due to improper syntax. Finally, contains a method
to help user by suggesting the mistake in the command

'''

# descriptions
command_desc = {
    "where is" : "Enter a city here and Jeffrey will tell you what country it is in and on what continent", 
    "how old is" : "Enter a full name here and Jeffrey will do his best to find their age", 
    "how good is" : "Enter movie title here", 
    "how can i" : "Ever been wondering how to do something? Alas enter that 'thing' here and Jeffrey will show you how", 
    "who am i" : "If you are feeling lost or going through a mid/quarter-life crisis Jeffrey is here to help you", 
    "i want to see" : "Enter whatever it is that you would like to see pictures of", 
    "show history" : "If you ever want to see the history of all your commands",
    "inspire me" : "Returns an inspirational quote to brighten your day",
    "get insult" : "Returns a smashing insult if you're in need",
    "help" : "self explanatory",
    "clear history" : "clear history currently stored in database",
    "execute history" : "executes a certain command in your command history"
}

# initiate database
db_file = ".commands_data.db"
commands_db = sqlite3.connect(db_file)
db = commands_db.cursor()
db.execute('''CREATE TABLE IF NOT EXISTS commands
                (command text, id int)''')
commands_db.commit()
current_command_id = 0

# lists possible commands and their format, rudely
def help():
    print "Here is a list of my possible commands and their how to use them"
    print ""
    print "_"*123
    print "*"+(123*" ")+"*"
    for com in command_desc.keys():
        print '*    ~{}~ : {}'.format(com, command_desc[com])+ ((114-(len(com)+ len(command_desc[com])))*" ")+ "*"
    print "*"+(123*" ")+"*"
    print "*"+("_"*123)+"*"
    print ""
    print "Remember each question and noun/verb should be separate by an ellipses like so.."
    print "Format: [Question word(s)]...[noun/verb]"

# lists commands entered, from database
def get_history(nothing):
    if len(nothing) != 0:
        print "I'll let this one slide, but next time don't add arguments to show my history, Imbecile!"
    print "get history"
    db.execute("SELECT * FROM commands") 
    rows = db.fetchall()
    for row in rows:
        print '{}. {}'.format(row[1], row[0])
        print ""

# selecting command from history to execute
def get_command(index):
    if len(index)  == 0:
        print "Please enter a index"
    else:
        if int(index) >= 0 and int(index) < current_command_id:
            db.execute("SELECT command FROM commands WHERE id = (?)", (index)) 
            com = db.fetchone()
            com =  str(com[0])
            if 'execute' in com:
                print "cannot excute this command, it will go on recursively"
            else:
                execute(com)
        else:
            print "no command in history with index"

# increment command count for database
def increment_command_count():
    global current_command_id
    current_command_id+=1    

# when history is flushed reset command id
def zero_command_id():
    global current_command_id
    current_command_id = 0

# clear database
def clear_history(nothing):
    if len(nothing) != 0 and nothing != 'no message':
        print "clear histtory doesn't take any arguments"
    else:
        db.execute("DELETE FROM commands")
        commands_db.commit()
        if nothing != 'no message':
            print "Clearing history...are you trying to hide something?"
            time.sleep(2)
            print "Calling 911..."
            time.sleep(2)
            print "Just Kidding"
        zero_command_id()
        
# checks command attempt and tries to suggest what user was trying to enter
def check_suggestions(comstr):
    attempt = comstr.split(" ")
    if attempt[0] == 'how':
        print "did you mean 'how old is...', 'how can i...', or 'how good is...'?"
    elif attempt[0] == 'where':
        print "did you mean 'where is...'?"
    elif attempt[0] == 'get':
        print "did you mean 'get insult...'?"
    elif attempt[0] == 'i':
        print "did you mean 'i want to see...'?"
    elif attempt[0] == 'tell':
        print "did you mean 'tell me about...'?"
    elif attempt[0] == 'inspire':
        print "did you mean 'inspire me...'?"
    elif attempt[0] == 'choose':
        print "did you mean 'choose history...'?"
    elif attempt[0] == 'show':
        print "did you mean 'show my history...'?"
    elif attempt[0] == 'who':
        print "did you mean 'who am i...'?"
    elif attempt[0] == 'clear':
        print "did you clear history...'?"
    elif attempt[0] == 'execute':
        print "did you mean execute history...?"
    elif 'history' in comstr:
        print "did you mean clear history..., show history... or execute history...?"
    elif "..." not in comstr:
        print "You're missing an ellipses ('...')" 

# executed on every method, processes command
def execute(args_in):
    """
        Handles command by either throwing an exception or calling
        a function. On quit, the database is cleared 
    """
    if args_in == 'quit':
        db.execute("DELETE FROM commands")
        commands_db.commit()
        print "Peace out girl scout"
        zero_command_id()
        clear_history('no message')
        exit(1)
   
    # logging commands in SQL database
    increment_command_count()
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
        "show history" : get_history,
        "get insult" : fn.get_insult,
        "inspire me" : fn.inspire_me,
        "clear history" : clear_history,
        "execute history" : get_command
    }

    args = args_in.split("...")

    command = args[0]
    if command not in command_functions.keys():
        fn.error("Invalid command: '{}'".format(args[0]))
        check_suggestions(args_in)
    elif len(args) == 1:
        fn.error("You need to enter three dots and an argument, its so easy, just do it")
    elif command == "help":
	if len(args) > 2:
	    fn.error("Don't put arguments after 'help', dingus")
	else:
	    help()
    else:     
        command_functions[command](args[1])
