import sqlite3
import os
import sys

global_commands = {
    "where is" : "Enter a city here and Jeffrey will tell you what country it is in and on what continent", 
    "how old is" : "Enter a full name here and Jeffrey will do his best to find their age", 
    "how good is" : "Enter movie title here", 
    "how can i" : "Ever been wondering how to do something? Alas enter that 'thing' here and Jeffrey will show you how", 
    "who am i" : "If you are feeling lost or going through a mid/quarter-life crisis Jeffrey is here to help you", 
    "i want to see" : "Enter whatever it is that you would like to see pictures of", 
    "tell me about" : "Enter a subject you are curious about"
}


db_file = os.path.expanduser("~") + "/.command_history.db"
commands_db = sqlite3.connect(db_file)
db = commands_db.cursor()
db.execute('''CREATE TABLE IF NOT EXISTS commands
                (command text, id int)''')
commands_db.commit()
current_command_id = 0
history_id = 0

def help(choice = 0):
    if choice == 1:
        print "Argument required!\n"
    if choice == 2:
        print "Sorry I don't recognize the command"
    print "Here is a list of my possible commands and their how to use them\n"
    for com in global_commands.keys():
        print '<{}> : {}'.format(com, global_commands[com])

def error(message = None):
    if message is not None:
        print(message)
    exit(1)

def where_is(place):
    pass

def how_old_is(person):
    pass

def how_good_is(movie):
    pass

def how_can_i(task):
    pass

def who_am_i(soul):
    print "You are snoop doggy dog"

def i_want_to_see(name):
    pass

def tell_me_about(thing):
    pass

def execute(args_in):
    """Ensures user input contains valid commands
    Input:
	args:
    """
    if args_in == 'quit':
        db.execute("DELETE FROM commands")
        commands_db.commit()
        exit(1)

    args = args_in.split("...")
    print args

    # available commands
    commands = {
        "where is" : where_is, 
        "how old is" : how_old_is, 
        "how good is" : how_good_is, 
        "how can i" : how_can_i, 
        "who am i" : who_am_i, 
        "i want to see" : i_want_to_see, 
        "tell me about" : tell_me_about
    }

    if len(args) == 0:
	help(1)

    command = args[0]
    if command == "help":
	if len(args) > 2:
	    error("Too many args provided for 'help'")
	else:
	    help(2)

    if command not in commands:
	error("Invalid command: '{}'".format(args[0]))

    # Map to command function
    commands[command](args[1:])


if __name__ == '__main__':
        print "Condescending Jeffrey: Hello! My name is Jeffrey, I'm a bot and I was created to answer 'all' your questions."
        print "         Go ahead, try to stump me."
        print "         Okay fine, since you asked I'll give you some ideas."
        print "         Every question you have has to have an ellipses (...) after the question word(s)"
        print "         And before the object. For example here are a couple of acceptable commands:"
        print "         1. where is...Qatar"
        print "         2. how old is...Charlie Sheen"
        print "         3. how good is...Interstellar (It's amazing by the way)"
        print "         Okay you get the idea."
        print "         I'm still in my robot infancy so I only know the following commands"
        help()
        print "\nJeffrey: Alright chief what questions do you have? "
	while True:
            command = raw_input(">> ")
            
            # logging commands in SQL database
            current_command_id +=1
            db.execute("INSERT INTO commands \
                        VALUES (?, ?)", (command, current_command_id))
            commands_db.commit()

            # then execute command
            execute(command.strip())
