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
        user = User.create(messenger_id=messenger_parser.messenger_id, state='start')
        
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
    send_message(user.messenger_id, 'Welcome to Blabla Kids Doll Matching Bot! To match your child with a doll, we will ask a series of questions about your childs personality. To being, please type Start')
    user.state = 'question1'
    user.save()

def question1(messenger_parser, user):

    question_text = 'Compared to other babies, your baby is more: /n 1: Like a slow loris (quiet and calm) /n 5: Like a Chihuahua (loud and constantly active)'
    
    if messenger_parser.text.lower() == 'start': 
        send_numbers_message(user.messenger_id, question_text, NUMBERS) 
        return
    else:
        start(messenger_parser, user)
        return

    user.score += int(messenger_parser.text)

    question_text = 'Does your baby generally: /n 1: Move around and play only one no one is around /n 5: Move around and play only when others are around/watching'
    send_numbers_message(user.messenger_id, question_text, NUMBERS) 
    user.state = 'question2'
    user.save()

def question2(messenger_parser, user):
    user.score += int(messenger_parser.text)

    question_text = 'When your infant is upset does he/she calm down by: /n 1: Being left alone or taking a nap /n 5: Receiving attention and active comforting from parents'
    send_numbers_message(user.messenger_id, question_text, NUMBERS) 
    user.state = 'question3'
    user.save()

def question3(messenger_parser, user):
    user.score += int(messenger_parser.text)

    question_text = 'When engaging with other babies, is your baby: /n 1: More like Bashful Dwarf from Snow White and shy away from attention /n More like Happy Dwarf from Snow White and enjoy the company of others, actively joining them in playing'
    send_numbers_message(user.messenger_id, question_text, NUMBERS) 
    user.state = 'question4'
    user.save()

def question4(messenger_parser, user):

    user.score += int(messenger_parser.text)

    question_text = 'Is your child more like: /n 1: Lisa Simpson, consistently stay with an activity for a long period of time to completion /n 5: Bart Simpson, easily distracted and start new activities frequently without finishing the previous ones'
    send_numbers_message(user.messenger_id, question_text, NUMBERS) 
    user.state = 'question4'
    user.save() 

def question5(messenger_parser, user):
    user.score += int(messenger_parser.text)

    question_text = 'When interacting with strangers/new people, does your baby act more like: /n 1: Neville Longbottom and initially resist interaction and become nervous around strangers /n 5: Ron Weasley and smile and coo at new people and interactions'
    send_numbers_message(user.messenger_id, question_text, NUMBERS) 
    user.state = 'question5'
    user.save()

def question6(messenger_parser, user):
    user.score += int(messenger_parser.text)

    question_text = 'When putting your baby to sleep, is your baby: /n 1: Highly selective with where he/she sleeps (i.e. will only sleep in her cradle, with a certain stuffed animal) /n 5: Content with sleeping anywhere'
    send_numbers_message(user.messenger_id, question_text, NUMBERS) 
    user.state = 'question6'
    user.save()  

def question7(messenger_parser, user):
    user.score += int(messenger_parser.text)

    question_text = 'When sharing a space with others for a long period of time, is your child more like: /n 1: Sadness from Inside Out and get overwhelmed or tired throughout the interaction /n 5: Joy from Inside Out and get energized and active throughout the interaction'
    send_numbers_message(user.messenger_id, question_text, NUMBERS) 
    user.state = 'question7'
    user.save()       

def question8(messenger_parser, user):
    user.score += int(messenger_parser.text)

    question_text = 'In terms of sensitivity, is your baby: /n 1: Very fussy at even the smallest provocation? (e.g. too many people, soiled diaper, etc.) /n 5: Rarely set off by inconveniences or changes to his or her environment'
    send_numbers_message(user.messenger_id, question_text, NUMBERS) 
    user.state = 'question8'
    user.save() 

def question9(messenger_parser, user):
    user.score += int(messenger_parser.text)

    question_text = 'Is your child: /n 1: Highly observant and notice small details in his/her surroundings /n 5: Inattentive and gloss over details, preferring to focus on the big picture instead'
    send_numbers_message(user.messenger_id, question_text, NUMBERS) 
    user.state = 'question9'
    user.save()     

def question10(messenger_parser, user):
    user.score += int(messenger_parser.text)

    user.state = 'results_handler'
    user.save()    



# 1-10 points = quiet, 11-20 = sweet, 21-30 = lively, 31-40 = mischievous, 41-50 = wild

def results_handler(messenger_parser, user):

    if (user.score >= 1 and user.score <= 10):
        quiet_description = 'some text'
        send_message(user.messenger_id, quiet_description)
        
        elements = []
        for i in quiet_dolls:
            title = a['name']
            item_url = a['url']
            image_url = a['urlImage']

            b = URLButton('Learn More', item_url)
            elements.append(GenericTemplateElement(title, item_url, image_url, '', [b])) 

        mess = GenericTemplateMessage(elements, user.messenger_id)
        mess.send()
        user.state = 'start'
        user.save()

    elif (user.score >= 11 and user.score <= 20):
        sweet_description = 'some text'
        send_message(user.messenger_id, sweet_description)
        
        elements = []
        for i in sweet_dolls:
            title = a['name']
            item_url = a['url']
            image_url = a['urlImage']

            b = URLButton('Learn More', item_url)
            elements.append(GenericTemplateElement(title, item_url, image_url, '', [b])) 

        mess = GenericTemplateMessage(elements, user.messenger_id)
        mess.send()
        user.state = 'start'
        user.save()

    elif (user.score >= 21 and user.score <= 30):
        lively_description = 'some text'
        send_message(user.messenger_id, lively_description)
        
        elements = []
        for i in lively_dolls:
            title = a['name']
            item_url = a['url']
            image_url = a['urlImage']

            b = URLButton('Learn More', item_url)
            elements.append(GenericTemplateElement(title, item_url, image_url, '', [b])) 

        mess = GenericTemplateMessage(elements, user.messenger_id)
        mess.send()
        user.state = 'start'
        user.save()

    elif (user.score >= 31 and user.score <= 40):
        mischievous_description = 'some text'
        send_message(user.messenger_id, mischievous_description)
        
        elements = []
        for i in mischievous_dolls:
            title = a['name']
            item_url = a['url']
            image_url = a['urlImage']

            b = URLButton('Learn More', item_url)
            elements.append(GenericTemplateElement(title, item_url, image_url, '', [b])) 

        mess = GenericTemplateMessage(elements, user.messenger_id)
        mess.send()
        user.state = 'start'
        user.save()

    elif (user.score >= 41 and user.score <= 50):
        wild_description = 'some text'
        send_message(user.messenger_id, wild_description)
        
        elements = []
        for i in wild_dolls:
            title = a['name']
            item_url = a['url']
            image_url = a['urlImage']

            b = URLButton('Learn More', item_url)
            elements.append(GenericTemplateElement(title, item_url, image_url, '', [b])) 

        mess = GenericTemplateMessage(elements, user.messenger_id)
        mess.send()
        user.state = 'start'
        user.save()

    else:
        start(messenger_parser, user)