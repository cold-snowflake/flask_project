import random
# adding function for game one
answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely',
            'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 
            'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 
            'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 
            'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good',
            'Very doubtful']

def get_answer(answers):
    return(answers[random.randint(0, len(answers)-1)])
