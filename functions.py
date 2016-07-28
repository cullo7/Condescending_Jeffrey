from lxml import html
import requests
import random

temper = 0

def error(message = None):
    global temper
    temper +=1
    if message is not None:
        print(message)
    if temper > 2:
        print "Just keep on getting on my nerves"
    elif temper > 5:
        print "Do you know how to type?"
    elif temper > 8:
        print "You vile beast, you should be ashamed of yourself"
    elif temper > 10:
        print "Get the hello out of here and come back when you have a brain cell in your puny brain, you make me sick"

def decrement_temper():
    global temper
    temper -=1

def where_is(place):
   print "Where is" 

def how_old_is(person):
    print "how old is"

def how_good_is(movie):
    if len(movie) == 0:
        error("How good is what? Give me a movie name nextime, Jackass")
    else:
        decrement_temper()
        page = requests.get('https://www.rottentomatoes.com/search/?search=interstellar')
        tree = html.fromstring(page.content)
        ext_link = tree.xpath('//ul[@id="movie_results_ul"]/li[1]') #/div[@class="media-body media-body-alt"]/div[@class="nomargin media-heading bold"]/a[@class="nomargin media-heading bold"]@href')
        print ext_link
        print "how good is"

def how_can_i(task):
    print "how can i"

def who_am_i(nothing):
    if nothing == 'kemosabe':
        print "Justice is what I seek Kemosabe.."
        decrement_temper()
    elif len(nothing) != 0:
        error("who am i doesn't take any arguments!")
    else:    
        decrement_temper()
        responses = [
            "You are Snoop Doggy Dog",
            "You are a raisin in the sun brother",
            "You are the first and last of your kind"
        ]
        print responses[random.randint(0,2)]

def i_want_to_see(name):
    print "i want to see"

def tell_me_about(thing):
    print "tell me about it"

def inspire_me(nothing):
    if len(nothing[0]) != 0:
        error("inspire me doesn't take any argument man")
    else:
        print "You're worthless, hows that"
def get_insult(nothing):
    if len(nothing[0]) != 0:
        error("get insult doesn't take any arguments knave")
    else:
        print "Coming soon"
