import os
import sys

def help(choice = 0):
    if choice == 0:
        print "Argument required!\n"
    if choice == 1:
        print "Sorry I don't recognize the command"
    print "help yourself, coming soon"

def error(message = None):
    if message is not None:
        print(message)
    exit(1)

def execute_commands(args_in):
    """Ensures user input contains valid commands
    Input:
	args:
    """
    args = [arg.lower() for arg in args_in]

    # available commands
    # TODO consider consolidating with help()
    commands = ["where is", "how old is", "how good is", "how can i", "who am i", "i want to see", "tell me about"]

    if len(args) == 0:
	help(1)

    command = args[0]
    if command == "help":
	if len(args) > 2:
	    error("Too many args provided for 'help'")
	else:
	    help()

    if command not in commands:
	error("Invalid command: '{}'".format(args[0]))

    # Map to command's handler function
    # Remaining args are passed regardless, dealt with in handler
    handlers = {
	    "update" : update_tracker,
	    "list"   : display_list,
	    "show"   : show_tracker,
	    "rename" : rename_tracker,
	    "delete" : delete_tracker,
	    "stats"  : display_stats,
	    "plot"   : display_plot
	    }
    handlers[command](args[1:])


if __name__ == '__main__':
        print "Jeffrey: Hello! My name is Jeffrey, I'm a bot and I was created to answer 'all' your questions.\n"
        print "         Go ahead, try to stump me.\n"
        print "         Okay fine, since you asked I'll give you some ideas.\n"
        print "         Every question you have has to have an ellipses (...) after the question word(s)\n"
        print "         And before the object. For example here are a couple of acceptable commands:\n"
        print "         1. where is...Qatar\n"
        print "         2. how old is...Charlie Sheen\n"
        print "         3. how good is...Interstellar (It's amazing by the way)\n"
        print "         Okay you get the idea.\n"
        print "         I'm still in my robot infancy so I only know the following commands\n"
        help(2)
        print "Jeffrey: Alright chief what questions do you have?\n "
	while True:
            command = raw_input(">> ")
	    #execute(command)
