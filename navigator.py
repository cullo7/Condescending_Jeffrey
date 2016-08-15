from lxml import html
import requests
import sys

def execute_command(path, cmd):
    ext = ''
    cmd  = cmd.split(" ")
    if cmd[0] == 'help':
        print "Commands:"
        print "'attr' [attribute] : The name of an attribute or the word all"
        print "'list' : Lists children of current node"
        print "'search' : You will be prompted to list a tag and attribute"
        print "'branch' [child] : Move to children node specified"
        print "'choose' [index] : For when current node is a list of multiple"
        print "'root : Revert to parent node'\n"
    elif cmd[0] == 'attr':
        if cmd[1] == 'text':
            ext = '/text()'
        elif cmd[1] == 'all':
            ext = '/@*'
        else:
            ext = '/@'+cmd[1]
    elif cmd[0] == 'list':
        ext = '/*'
    elif cmd[0] == 'search':
        search = raw_input("What html tag do you want to search: ")
        path = '//'+search
        attr = raw_input("What attribute will you specify: Ex: (id = 'Cat')")
        if len(attr) != 0:
            path += '[@'+attr+']'
        print path
    elif cmd[0] == 'branch':
        path+='/'+cmd[1]
    elif cmd[0] == 'choose':
        path+='['+cmd[1]+']'
    elif cmd[0] == 'root':
        x = len(path)-1
        record = False
        new_path = ''
        while x >= 0:   
            if not record and path[x] == '/':
                record = True
            elif record:
                new_path += path[x]
            x -= 1
        path = new_path[::-1]
    else:
        print "Sorry I didn't recognize the command"     
        print "Enter help to see commands"
    print tree.xpath(path+ext)
    print "path "+path
    return path

if __name__ == "__main__":
    easyTarget = sys.argv[1]
    print easyTarget
    page = requests.get(easyTarget)
    tree = html.fromstring(page.content)
    path = '/html'
    while True:
        command = raw_input(">> ")
        path = execute_command(path, command)
