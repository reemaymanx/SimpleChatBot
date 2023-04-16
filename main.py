import re
import longAnswers as l

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_word = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1
    ## percentage of recognized words in inserted messages
    if len(recognised_words) > 0:
        percentage = float(message_certainty) / float(len(recognised_words))
    else:
        percentage = 0
    for word in required_words:
        if word not in user_message:
            has_required_word = False
            break
    if has_required_word or single_response:
        res = int(percentage * 100)
        return res
    else:
        return 0

def check_messages(message):
    highest_probability_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_probability_list
        highest_probability_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    ####################response area ##############################33
    response('Hello!', ['hello', 'hi', 'whatsup', 'sup', 'ciao', 'salam', 'hey', 'heyo'], single_response=True)
    response('I am doing fine, and you? ', ['how', 'are', 'you'], required_words=['how'])
    response('I am from Egypt', ['what', 'is', 'your','nationality'], required_words=['nationality'])
    response(l.bot_hearing , ['can', 'you','hear','me'], required_words=['you','hear'])
    best_match = max(highest_probability_list, key=highest_probability_list.get)
    ##print(highest_probability_list)
    return 'unknown' if highest_probability_list[best_match] < 1 else best_match

def get_response(user_response):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_response.lower())
    response = check_messages(split_message)
    return response

##check if the response system is working
while True:
    user_input = input('You: ')
    if user_input.lower() == 'quit':
        break
    print('ChatBot: ' + get_response(user_input))

