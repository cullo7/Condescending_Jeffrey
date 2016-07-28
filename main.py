import subprocess
import time
import commands as cmd

if __name__ == '__main__':
        width = 180
        '''
        subprocess.call(['clear'])
        print "_______ _____   ______  ______  ______   _____  __  __".center(width, " ")
        print "|_   _| | __|   | ___|  | ___|  | .  |   | __|  \ \/ /".center(width, " ")
        print "  | |   | |_    | |_    | |_    |___/    | |_    \  / ".center(width, " ")
        print "  | |   | __|   | __|   | __|   |  _ \   | __|    | | ".center(width, " ")
        print " _| |   | |_    | |     | |     | | | |  | |_     | | ".center(width, " ")
        print "|___|   |___|   |_|     |_|     |_| |_|  |___|    |_| ".center(width, " ")
        print "\n\n"
        print "Hello! My name is Condescending Jeffrey, I'm a bot and I was created to answer 'all' your questions.".center(width, " ")
        time.sleep(2.5)
        print "While at the same time belittling you and making you feel inadequate.".center(width, " ")
        time.sleep(2.5)
        print "Go ahead, try to stump me.".center(width, " ")
        time.sleep(2.5)
        print "Okay fine, since you asked I'll give you some ideas.".center(width, " ")
        time.sleep(2.5)
        print "Every question you have has to have an ellipses (...) after the question word(s)".center(width, " ")
        time.sleep(2.5)
        print "And before the object. For example here are a couple of acceptable commands:".center(width, " ")
        time.sleep(2.5)
        print "1. where is...Qatar".center(width, " ")
        print "2. how old is...Charlie Sheen".center(width, " ")
        print "3. how good is...Interstellar (It's amazing by the way)".center(width, " ")
        time.sleep(2.5)
        print "Okay you get the idea.".center(width, " ")
        time.sleep(2.5)
        print "I'm still in my robot infancy so I only know the following commands".center(width, " ")
        time.sleep(2.5)
        help()
        time.sleep(2.5)
        '''
        print "\nJeffrey: Alright chief what questions do you have? ".center(width, " ")
	while True:
            command = raw_input(">> ")
            
            # execute command
            cmd.execute(command.strip())
