App_size = (400, 700)
Main_rows = 7
Main_columns = 4

Font = 'Ubuntu'
Result_font_size = 70
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
    '/': {'col':3, 'row':2, 'character':'/','span':1, 'operator':'/'},
    '*': {'col':3, 'row':3, 'character':'x','span':1, 'operator':'*'},
    '+': {'col':3, 'row':4, 'character':'+','span':1, 'operator':'+'},
    '-': {'col':3, 'row':5, 'character':'-','span':1, 'operator':'-'},
    '=': {'col':3, 'row':6, 'character':'=','span':1, 'operator':'='}

}

Pro_operators = {
    'fac': {'col':4, 'row':2, 'character':'!','span':1, 'operator':'fac'},
    'sin': {'col':4, 'row':3, 'character':'sin','span':1, 'operator':'sin'},
    'cos': {'col':4, 'row':4, 'character':'cos','span':1, 'operator':'cos'},
    'tan': {'col':4, 'row':5, 'character':'tan','span':1, 'operator':'tan'}
}


Operators = {
    'clear': {'col':0, 'row':2, 'text':'AC', 'image-path': None},
    'invert': {'col':1, 'row':2, 'text':'+/-', 'image-path': None},
    'percent': {'col':2, 'row':2, 'text':'%', 'image-path': None},
    
}

Colors = {
    'light-gray': {'fg': ('#505050', '#D4D4D2'), 'hover': ('#686868','#efefed'), 'text':('white', 'black')},
    'dark-gray': {'fg': ('#D4D4D2', '#505050'), 'hover': ('#efefed','#686868'), 'text':('black', 'white')},
    'blue': {'fg': '#20416b', 'hover': '#436591', 'text':('white', 'black')},
    'orange-highlight': {'fg': '#white', 'hover': '#white', 'text':('black', '#FF9500')}
}

Black = '#000000'
White = '#EEEEEE'