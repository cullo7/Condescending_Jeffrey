from lxml import html
import requests
import random
import urllib2 as urllib
from PIL import Image
from cStringIO import StringIO

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
        page = requests.get('https://www.rottentomatoes.com/search/?search='+movie)
        tree = html.fromstring(page.content)
        ext_link = tree.xpath('//ul[@id="movie_results_ul"]/li[1]/div[@class="media-body media-body-alt"]/div[@class="nomargin media-heading bold"]/a[@class="unstyled articleLink"]/@href')
        ext_link = ext_link[0]
        print 'https://www.rottentomatoes.com'+ext_link
        page = requests.get('https://www.rottentomatoes.com'+ext_link)
        tree = html.fromstring(page.content)
        image = raw_input("enter any key to see the image, just press enter to skip to Synopsis")
        if len(image) != 0:
            print "image "+ str(tree.xpath('//img[@class="posterImage"]/@src'))
            img_file = urllib.urlopen(tree.xpath('//img[@class="posterImage"]/@src')[0])
            im = StringIO(img_file.read())
            im = Image.open(im)
            im.show()
        print "Title: "+ str(tree.xpath('//meta[@property="og:title"]/@content')[0])
        print "Summary: "+str(tree.xpath('//p[@class="critic_consensus superPageFontColor"]/text()')[2])
        print "Critics Score: "+str(tree.xpath('//span[@class="meter-value superPageFontColor"]/span/text()')[0])
        print "Top Critics Score: "+str(tree.xpath('//span[@class="meter-value superPageFontColor"]/span/text()')[1])

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
    page = requests.get('https://www.google.com/search?q='+name+'&source=lnms&tbm=isch')
    print tree.xpath('//div[@data-ri=0]/a/img/@src')[0]
    img_file = urllib.urlopen(tree.xpath('//div[@data-ri=0]/a/img/@src')[0])
    im = StringIO(img_file.read())
    im = Image.open(im)
    im.show()
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
