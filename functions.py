from lxml import html
import webbrowser
import requests
import random
import urllib2 as urllib
import PIL
from PIL import Image
from cStringIO import StringIO
import subprocess

'''
Contains all the command functions. Each method has an error check to avoid the program breaking.
'''

temper = 0

# prints error and assesses how angry Jeff is
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

# finds the country and continent of a chosen city
def where_is(city):
    print "Let me get that for you sport\n"
    subprocess.call(["./find_city", city])
    print "\nAre you satisfied? Of course you aren't, you heathen\n"

# finds the age of a celeb
def how_old_is(person):
    search = person.split(' ')
    search = search[0].capitalize() + "_" + search[1].capitalize()
    page = requests.get("https://en.wikipedia.org/wiki/"+person)
    tree = html.fromstring(page.content)
    if tree.xpath('//table[@id="noarticletext"]/tr/td/b/text()')[0] == "Wikipedia does not have an article with this exact name.":
        print "Sorry I could not find that person"
    else:
        age = tree.xpath('//table[@class="infobox biography vcard"]/tr[3]/td/span[3]/text()')[0]
        print person + str(" is ") + age[5:7] + str(" years old")

# searches for movie and returns short summary and crtic scores
def how_good_is(movie):
    if len(movie) == 0:
        error("How good is what? Give me a movie name nextime, Jackass")
    else:
        decrement_temper()
        page = requests.get('https://www.rottentomatoes.com/search/?search='+movie)
        tree = html.fromstring(page.content)
        if len(tree.xpath('//h1[@class="center noresults"]/text()')) == 0:
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
        else:
            print str(tree.xpath('//h1[@class="center noresults"]/text()')[0])

# queries youtube for users 'how to' request and launches a webbrowser with the url of the first result
def how_can_i(task):
    print "task "+task
    if len(task) == 0:
        print "Gotta enter a task squire"
    else:
        print 'https://www.youtube.com/results?search_query='+'how to '+task
        page = requests.get('https://www.youtube.com/results?search_query='+'how to '+task)
        tree = html.fromstring(page.content)
        if len(tree.xpath('//div[@class="search-message"]/text()')) == 0:
            vid_url = tree.xpath('//ol[@class="item-section"]//div[@class="yt-lockup-dismissable yt-uix-tile"][1]/div[1]/a/@href')[0]
            print vid_url
            webbrowser.open_new('https://www.youtube.com'+vid_url)
            print "Here's how you do that"
        else:
            print "No results for "+str(tree.xpath('//div[@class="search-message"]/b/text()')[0])

# Answers the traditional coming of age question
def who_am_i(nothing):
    if nothing == 'kemosabe':
        print "Justice is what I seek Kemosabe.."
        decrement_temper()
        decrement_temper()
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

# Finds the image you want to see on google and returns a shittier version of it basically..
def i_want_to_see(name):
    page = requests.get('https://www.google.com/search?q='+name+'&source=lnms&tbm=isch')
    tree = html.fromstring(page.content)
    not_found = tree.xpath('//div[@style="font-size:16px;padding-left:10px"]/p/b/text()')
    if len(not_found) == 0:
        imgURL =  tree.xpath('//table[@class="images_table"]/tr[1]/td[1]/a/img/@src')[0]
        img_file = urllib.urlopen(imgURL)
        im = StringIO(img_file.read())
        img = Image.open(im)
        img.show()
        print "As you wish.."
    else:
        print "Your search - "+str(not_found[0])+" - did not match any documents"

# Finds random inspirational quotes
def inspire_me(nothing):
    if len(nothing[0]) != 0:
        error("inspire me doesn't take any argument man")
    else:
        page = requests.get('http://www.brainyquote.com/quotes/topics/topic_inspirational.html')
        tree = html.fromstring(page.content)
        print tree.xpath('//a[@title="view quote"]/text()')[random.randint(1,26)]
# returns an insult when you need one
def get_insult(nothing):
    if len(nothing[0]) != 0:
        error("get insult doesn't take any arguments knave")
    else:
        page = requests.get('http://all-that-is-interesting.com/hilarious-insults#1')
        tree = html.fromstring(page.content)
        print tree.xpath('//p[@class="slideshow-caption slideshow-bottom"]/text()')[random.randint(1,45)]    
