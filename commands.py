global_commands = {
    "where is" : "Enter a city here and Jeffrey will tell you what country it is in and on what continent", 
    "how old is" : "Enter a full name here and Jeffrey will do his best to find their age", 
    "how good is" : "Enter movie title here", 
    "how can i" : "Ever been wondering how to do something? Alas enter that 'thing' here and Jeffrey will show you how", 
    "who am i" : "If you are feeling lost or going through a mid/quarter-life crisis Jeffrey is here to help you", 
    "i want to see" : "Enter whatever it is that you would like to see pictures of", 
    "tell me about" : "Enter a subject you are curious about"
}

db_file = ".commands_data.db"
commands_db = sqlite3.connect(db_file)
db = commands_db.cursor()
db.execute('''CREATE TABLE IF NOT EXISTS commands
                (command text, id int)''')
commands_db.commit()
current_command_id = 0
history_id = 0

def help(choice = 0):
    if choice == 1:
        print "You need to enter three dots and an argument, its so easy, just do it\n"
    if choice == 2:
        print "Sorry I don't recognize the command\n"
    print "Here is a list of my possible commands and their how to use them\n"
    for com in global_commands.keys():
        print '<{}> : {}'.format(com, global_commands[com])
    print "Format: [Question word(s)]...[noun/verb]"

def execute(args_in):
    """
        Handles command by either throwing an exception or calling
        a function. On quit, the database is cleared 
    """
    if args_in == 'quit':
        db.execute("DELETE FROM commands")
        commands_db.commit()
        exit(1)

def get_history():
    pass

def choose_history(num):
    pass

    commands = {
        "where is" : f.where_is, 
        "how old is" : f.how_old_is, 
        "how good is" : f.how_good_is, 
        "how can i" : f.how_can_i, 
        "who am i" : f.who_am_i, 
        "i want to see" : f.i_want_to_see, 
        "tell me about" : f.tell_me_about
    }

    args = args_in.split("...")
    print args

    if len(args) == 1:
	help(1)

    command = args[0]
    if command == "help":
	if len(args) > 2:
	    f.error("Don't put arguments after 'help', dingus")
	else:
	    help(2)
    if command not in commands:
        f.error("Invalid command: '{}'".format(args[0]))
    else: 
        commands[command](args[1:])
