# Script that houses main logic of bot
from messenger_parser import MessengerParser
from messenger_api_requests import send_message, send_numbers_message
from helpers import response
from db import User
from send import GenericTemplateMessage, GenericTemplateElement, URLButton
from doll_dictionary import quiet_dolls, sweet_dolls, lively_dolls, mischievous_dolls, wild_dolls

NUMBERS = ['1','2','3','4','5']

def response_handler(request):
     # Parse request and get the data we want out of it like messenger_id, text
    messenger_parser = MessengerParser(request)

    # Get user object from database so we can see the state of our user.
    try:
        user = User.select().where(User.messenger_id == messenger_parser.messenger_id).get()
    except:
        # If user doesn't exist, we create them. This would be a first time user.
        user = User.create(messenger_id=messenger_parser.messenger_id, state='start', score=0)
        
    # Here we need to decide what we need to do next for our user
    if user.state == 'start':
        # generic intro
        start(messenger_parser, user)
    elif user.state == 'question1':
        question1(messenger_parser, user)
    elif user.state == 'question2':
        question2(messenger_parser,user)
    elif user.state == 'question3':
        question3(messenger_parser,user)
    elif user.state == 'question4':
        question4(messenger_parser,user)
    elif user.state == 'question5':
        question5(messenger_parser,user)
    elif user.state == 'question6':
        question6(messenger_parser,user)
    elif user.state == 'question7':
        question7(messenger_parser,user)
    elif user.state == 'question8':
        question8(messenger_parser,user)
    elif user.state == 'question9':
        question9(messenger_parser,user)
    elif user.state == 'question10':
        question10(messenger_parser,user)
    else:
        results_handler(messenger_parser,user)

    # return the response to Facebook.
    return response()

def start(messenger_parser, user):
    send_message(user.messenger_id, 'Welcome to the Blabla Doll Sorter! We at Blabla are here to help you find the perfect doll for your child. Every doll has its own unique personality. Please answer this short quiz so that we can match you with your child’s ideal doll! To begin, please type start')
    user.state = 'question1'
    user.save()

def question1(messenger_parser, user):

    question_text = 'Compared to other babies, your baby is more: 1: Like a slow loris (quiet and calm) 5: Like a Chihuahua (loud and constantly active)'
    
    if messenger_parser.text.lower() == 'start': 
        send_numbers_message(user.messenger_id, question_text, NUMBERS) 
        return

    user.score += int(messenger_parser.text)

    question_text = 'Does your baby generally: 1: Move around and play only one no one is around 5: Move around and play only when others are around/watching'
    send_numbers_message(user.messenger_id, question_text, NUMBERS) 
    user.state = 'question2'
    user.save()

def question2(messenger_parser, user):
    user.score += int(messenger_parser.text)

    question_text = 'When your infant is upset does he/she calm down by: 1: Being left alone or taking a nap 5: Receiving attention and active comforting from parents'
    send_numbers_message(user.messenger_id, question_text, NUMBERS) 
    user.state = 'question3'
    user.save()

def question3(messenger_parser, user):
    user.score += int(messenger_parser.text)

    question_text = 'When engaging with other babies, is your baby: 1: More like Bashful Dwarf from Snow White and shy away from attention 5: More like Happy Dwarf from Snow White and enjoy the company of others, actively joining them in playing'
    send_numbers_message(user.messenger_id, question_text, NUMBERS) 
    user.state = 'question4'
    user.save()

def question4(messenger_parser, user):

    user.score += int(messenger_parser.text)

    question_text = 'Is your child more like: 1: Lisa Simpson, consistently stay with an activity for a long period of time to completion 5: Bart Simpson, easily distracted and start new activities frequently without finishing the previous ones'
    send_numbers_message(user.messenger_id, question_text, NUMBERS) 
    user.state = 'question5'
    user.save() 

def question5(messenger_parser, user):
    user.score += int(messenger_parser.text)

    question_text = 'When interacting with strangers/new people, does your baby act more like: 1: Neville Longbottom and initially resist interaction and become nervous around strangers 5: Ron Weasley and smile and coo at new people and interactions'
    send_numbers_message(user.messenger_id, question_text, NUMBERS) 
    user.state = 'question6'
    user.save()

def question6(messenger_parser, user):
    user.score += int(messenger_parser.text)

    question_text = 'When putting your baby to sleep, is your baby: 1: Highly selective with where he/she sleeps (i.e. will only sleep in her cradle, with a certain stuffed animal) 5: Content with sleeping anywhere'
    send_numbers_message(user.messenger_id, question_text, NUMBERS) 
    user.state = 'question7'
    user.save()  

def question7(messenger_parser, user):
    user.score += int(messenger_parser.text)

    question_text = 'When sharing a space with others for a long period of time, is your child more like: 1: Sadness from Inside Out and get overwhelmed or tired throughout the interaction 5: Joy from Inside Out and get energized and active throughout the interaction'
    send_numbers_message(user.messenger_id, question_text, NUMBERS) 
    user.state = 'question8'
    user.save()       

def question8(messenger_parser, user):
    user.score += int(messenger_parser.text)

    question_text = 'In terms of sensitivity, is your baby: 1: Very fussy at even the smallest provocation? (e.g. too many people, soiled diaper, etc.) 5: Rarely set off by inconveniences or changes to his or her environment'
    send_numbers_message(user.messenger_id, question_text, NUMBERS) 
    user.state = 'question9'
    user.save() 

def question9(messenger_parser, user):
    user.score += int(messenger_parser.text)

    question_text = 'Is your child: 1: Highly observant and notice small details in his/her surroundings 5: Inattentive and gloss over details, preferring to focus on the big picture instead'
    send_numbers_message(user.messenger_id, question_text, NUMBERS) 
    user.state = 'question10'
    user.save()     

def question10(messenger_parser, user):
    user.score += int(messenger_parser.text)

    results_handler(messenger_parser, user)  


# 1-10 points = quiet, 11-20 = sweet, 21-30 = lively, 31-40 = mischievous, 41-50 = wild

def results_handler(messenger_parser, user):

    if (user.score >= 1 and user.score <= 10):
        quiet_description = 'Your child’s ideal doll falls under the Quiet category, meaning that he or she is typically very reserved and calm. Dolls in the Quiet category have muted colors, calm facial expressions, and a generally very tranquil disposition. Check out these recommended dolls from the Quiet category!'
        send_message(user.messenger_id, quiet_description)
        
        elements = []
        for i in quiet_dolls:
            title = i['name']
            item_url = i['url']
            image_url = i['urlImage']

            b = URLButton('Learn More', item_url)
            elements.append(GenericTemplateElement(title, item_url, image_url, '', [b])) 

        mess = GenericTemplateMessage(elements, user.messenger_id)
        mess.send()

    elif (user.score >= 11 and user.score <= 20):
        sweet_description = 'Your child’s ideal doll falls under the Sweet category! This means that your child is generally pretty quiet and calm, but likes to socialize from time to time! Overall, dolls that fall in the Sweet category have happy-go-lucky, laid-back demeanors. Check out these recommended dolls from the Sweet category!'
        send_message(user.messenger_id, sweet_description)
        
        elements = []
        for i in sweet_dolls:
            title = i['name']
            item_url = i['url']
            image_url = i['urlImage']

            b = URLButton('Learn More', item_url)
            elements.append(GenericTemplateElement(title, item_url, image_url, '', [b])) 

        mess = GenericTemplateMessage(elements, user.messenger_id)
        mess.send()

    elif (user.score >= 21 and user.score <= 30):
        lively_description = 'Your child’s ideal doll is in the Lively category! Your child possesses both introverted and extroverted tendencies, needing an equal amount of time alone as time with other people! Dolls that fall under the Lively category have some really cool outfits and bright personalities that will liven up any room! Check out these recommendations from the Lively category!'
        send_message(user.messenger_id, lively_description)
        
        elements = []
        for i in lively_dolls:
            title = i['name']
            item_url = i['url']
            image_url = i['urlImage']

            b = URLButton('Learn More', item_url)
            elements.append(GenericTemplateElement(title, item_url, image_url, '', [b])) 

        mess = GenericTemplateMessage(elements, user.messenger_id)
        mess.send()

    elif (user.score >= 31 and user.score <= 40):
        mischievous_description = 'Your child’s ideal doll match is in the Mischievous category! This means your child is probably a bit of a trouble maker! But that’s alright, because dolls in this category have really colorful personalities, even if they are a bit rebellious as well! Check out these recommendations from the Mischievous category!'
        send_message(user.messenger_id, mischievous_description)
        
        elements = []
        for i in mischievous_dolls:
            title = i['name']
            item_url = i['url']
            image_url = i['urlImage']

            b = URLButton('Learn More', item_url)
            elements.append(GenericTemplateElement(title, item_url, image_url, '', [b])) 

        mess = GenericTemplateMessage(elements, user.messenger_id)
        mess.send()

    elif (user.score >= 41 and user.score <= 50):
        wild_description = 'Your child’s ideal doll falls in the Wild category, so your child is generally a great big ball of energy! He or she loves socializing, whether it’s meeting new people or just being around others. Dolls in the Wild category are equally as spontaneous and, as the name suggests, wild! Check out these recommendations from the Wild category!'
        send_message(user.messenger_id, wild_description)
        
        elements = []
        for i in wild_dolls:
            title = i['name']
            item_url = i['url']
            image_url = i['urlImage']

            b = URLButton('Learn More', item_url)
            elements.append(GenericTemplateElement(title, item_url, image_url, '', [b])) 

        mess = GenericTemplateMessage(elements, user.messenger_id)
        mess.send()
        
    user.score = 0
    user.state = 'start'
    user.save()
