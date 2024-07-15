from customtkinter import CTkButton
from Settings import *

class Button(CTkButton):
    def __init__(self, parent, function, text, col, row, font, span=1, color='dark-gray'):
        super().__init__(
            master=parent,
            command=function,
            text=text,
            corner_radius=Styling['corner-radius'],
            font=font,
            fg_color=Colors[color]['fg'],
            hover_color=Colors[color]['hover'],
            text_color=Colors[color]['text'])
        self.grid(column=col,columnspan=span, row=row, sticky='NSEW', padx=Styling['gap'], pady=Styling['gap'])
        
class NumberButton(Button):
    def __init__(self, parent, function, text, col, row, font, span, color='light-gray'):
        super().__init__(
            parent=parent,
            function=lambda:function(text),
            text=text,
            col=col,
            row=row,
            font=font,
            span=span,
            color=color,
        )


class OperatorButtons(Button):
    def __init__(self, parent, operator, function, text, col, row, font, span, color='blue'):
        super().__init__(
            parent=parent,
            function=lambda:function(operator),
            text=text,
            col=col,
            row=row,
            font=font,
            span=span,
            color=color,
        )