import os
import sys

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
	help()

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
	for x in sys.argv:
		print x + '\n'
	execute_commands(sys.argv[1:])
