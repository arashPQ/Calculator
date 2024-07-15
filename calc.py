import customtkinter as ctk
from Buttons import Button, NumberButton, OperatorButtons
import darkdetect
from Settings import *


class Calculator(ctk.CTk):
    def __init__(self, is_dark):
        super().__init__(fg_color=(White, Black))

        # Settings
        ctk.set_appearance_mode(f'{"dark" if is_dark else "light"}')
        self.geometry(f'{App_size[0]}x{App_size[1]}')
        self.resizable(False, False)
        self.title("Calculator")


        # Layouts
        self.rowconfigure(list(range(Main_rows)), weight=1, uniform='a')
        self.columnconfigure(list(range(Main_columns)), weight=1, uniform='b')


        # Data
        self.result_string = ctk.StringVar(value='0')
        self.formula_string = ctk.StringVar(value='')
        self.display_numbers = []
        self.full_operations = []


        # Widgets
        self.create_widgets()


        self.mainloop()

    def create_widgets(self):
        main_font = ctk.CTkFont(family=Font, size=Normal_font_size)
        Result_font = ctk.CTkFont(family=Font, size=Result_font_size)

        Outout_Label(self, 0, 'SE', main_font, self.formula_string)
        Outout_Label(self, 1, 'E', Result_font, self.result_string)

        Button(parent=self,
               function=self.clear,
               text=Operators['clear']['text'],
               col=Operators['clear']['col'],
               row=Operators['clear']['row'],
               font=main_font
               )
        

        Button(parent=self,
               function=self.percent,
               text=Operators['percent']['text'],
               col=Operators['percent']['col'],
               row=Operators['percent']['row'],
               font=main_font)

        Button(parent=self,
               function=self.invert,
               text=Operators['invert']['text'],
               col=Operators['invert']['col'],
               row=Operators['invert']['row'],
               font=main_font)
        

        for num, data in Number_Positions.items():
            NumberButton(parent=self,
                         text = num,
                         function=self.num_pressed,
                         col=data['col'],
                         row=data['row'],
                         font=main_font,
                         span=data['span'])


        for operator, data in Operator_positions.items():
            OperatorButtons(
                parent=self,
                text=data['character'],
                operator=operator,
                function=self.Operator,
                col=data['col'],
                row=data['row'],
                span=data['span'],
                font=main_font
            )



    def clear(self):
        self.result_string.set(0)
        self.formula_string.set('')

        self.display_numbers.clear()
        self.full_operations.clear()

    def invert(self):
        current_number = ''.join(self.display_numbers)
        if current_number:
            if float(current_number) > 0:
                self.display_numbers.insert(0, '-')

            else:
                del self.display_numbers[0]


            self.result_string.set(''.join(self.display_numbers))

    def percent(self):
        if self.display_numbers:
            current_numbers = float(''.join(self.display_numbers))
            percent_number = current_numbers / 100

            self.display_numbers = list(str(percent_number))
            self.result_string.set(''.join(self.display_numbers))

    def num_pressed(self, value):
        self.display_numbers.append(str(value))
        full_number = ''.join(self.display_numbers)
        self.result_string.set(full_number)


    def Operator(self, value):
        current_number = ''.join(self.display_numbers)
        if current_number:
            self.full_operations.append(current_number)
            
            if value != '=':
                # Update Data
                self.full_operations.append(value)
                self.display_numbers.clear()
                
                # Update Output
                self.result_string.set('')
                self.formula_string.set(' '.join(self.full_operations))

            else:
                formula = ' '.join(self.full_operations)
                Result = eval(formula)

                # Result Configuration

                if isinstance(Result, float):
                    
                    if Result.is_integer():
                        Result = int(Result)

                    else:
                        Result = round(Result, 3)

                # Update Date
                self.full_operations.clear()
                self.display_numbers = [str(Result)]

                # Update Output
                self.result_string.set(Result)
                self.formula_string.set(formula)


class Outout_Label(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(master=parent, text='', font=font, textvariable=string_var)
        self.grid(column = 0, columnspan=5, row=row, sticky=anchor, padx=10)
        



if __name__ == '__main__':
    Calculator(darkdetect.isDark())