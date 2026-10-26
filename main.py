# Working with Dictionaries
from pyscript import display, document


def game_details(e):
    document.getElementById('result').innerHTML = ' '
    favorite_game = document.getElementById('dictionary').value.lower().strip()

    game_developers = {
        'roblox': 'David Baszucki', 
        'codm': 'TiMi Studio',
        'fnaf': 'Scott Cawthon',
        'minecraft': 'Notch',
    } # specifying dictionaries

    game_check = favorite_game in game_developers

    display_message = ('Sorry, your game is not in the list!', f'{game_developers[favorite_game]}')

    display(display_message[game_check], target='result')
    
    game_developers['geshin impact'] = 'Hoyoverse' # adding new element
    display(game_developers, target='result')

    list_with_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
    tuple_with_strings = ('ab', 'cd', 'ef')
    list_with_strings = ['ax', 'by', 'cz']

    display(dict(list_with_tuples), target='result')
    display(dict(list_with_strings), target='result')
    display(dict(tuple_with_strings), target='result')

    keywords = ['say', 'jm', 'jay', 'mace']
    values = ['esguerra', 'piansay', 'estrada', 'panela']

    student_nicknames = dict(zip(keywords, values)) 

    display(student_nicknames, target='result')

    philadelphia = {
        'center':'Joel Embilid',
        'pf':'Lebron James',
        'sf':'Jaylen Brown',
        'sg':'VJ Edgecomb',
        'pg':'Tyrese Maxey'
    }

    philadelphia['pg'] = 'Stephen Curry'
    del philadelphia['sg']
    display(philadelphia, target='result')

    dict1 = {'x':1, 'y':2, 'z':3}
    dict2 = {'a':4, 'b':5, 'c':6}

    display(dict1 | dict2, target='result')
    merged_dictionary = {**dict1, **dict2,}

    display(merged_dictionary, target='result') 

    display(len(merged_dictionary), target='result')

    ai = {
        'tony stark':'creator',
        'JARVIS':'AI1',
        'FRIDAY':'AI2',
        'Edith':'AI3',
        'Vision':'AI4'
    }

    display('Vision' in ai, target='result')
    display(ai.get('JARVIS'), target='result')
    display(ai.keys(), target='result')
    display(ai.values(), target='result')
    display(ai['tony stark'], target='result')



