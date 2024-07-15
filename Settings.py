App_size = (500, 700)
Main_rows = 7
Main_columns = 5

Font = 'Ubuntu'
Output_font_size = 70
Normal_font_size = 32

Styling = {'gap':0.5, 'corner-radius':0}

Number_Positions = {
    '.':{'col':2, 'row':6, 'span':1},
    0:{'col':0, 'row':6, 'span':2},
    1:{'col':0, 'row':5, 'span':1},
    2:{'col':1, 'row':5, 'span':1},
    3:{'col':2, 'row':5, 'span':1},
    4:{'col':0, 'row':4, 'span':1},
    5:{'col':1, 'row':4, 'span':1},
    6:{'col':2, 'row':4, 'span':1},
    7:{'col':0, 'row':3, 'span':1},
    8:{'col':1, 'row':3, 'span':1},
    9:{'col':2, 'row':3, 'span':1},
}

Operator_positions = {
    '/': {'col':3, 'row':2, 'character':'', 'operator':'/', 'image-path':{'light': ''}},
    '*': {'col':3, 'row':3, 'character':'', 'operator':'/', 'image-path': None},
    '+': {'col':3, 'row':4, 'character':'', 'operator':'/', 'image-path': None},
    '-': {'col':3, 'row':5, 'character':'', 'operator':'/', 'image-path': None},
    '=': {'col':3, 'row':6, 'character':'', 'operator':'/', 'image-path': None}
}




Operators = {
    'clear': {'col':3, 'row':2, 'text':'AC', 'image-path': None},
    'invert': {'col':3, 'row':2, 'text':'', 'image-path':{'light': '', 'dark':''}},
    'percent': {'col':3, 'row':2, 'text':'%', 'image-path': None},
    
}

Colors = {
    'light-gray': {'fg': ('#505050', '#D4D4D2'), 'hover': ('#686868','#efefed'), 'text':('white', 'black')},
    'dark-gray': {'fg': ('#D4D4D2', '#505050'), 'hover': ('#efefed','#686868'), 'text':('black', 'white')},
    'orange': {'fg': '#FF9500', 'hover': '#ffb143', 'text':('white', 'black')},
    'orange-highlight': {'fg': '#white', 'hover': '#white', 'text':('black', '#FF9500')}
}

Black = '#000000'
White = '#EEEEEE'