import random
# adding function for game one
answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely',
            'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 
            'Yes Signs point to yes', 'Reply hazy', 'try again', 'Ask again later', 
            'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 
            'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good',
            'Very doubtful']


# adding function for game two

houses = ['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin']


def get_answer(value):
    return(value[random.randint(0, len(value)-1)])
