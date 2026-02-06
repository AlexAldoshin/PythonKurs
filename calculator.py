import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        
        self.expression = ""
        
        # Поле ввода
        self.input_field = tk.Entry(
            root, 
            font=('Arial', 24), 
            borderwidth=2, 
            relief="solid",
            justify='right'
        )
        self.input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=20)
        
        # Кнопки
        self.create_buttons()
    
    def create_buttons(self):
        # Определение кнопок
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('←', 5, 1), ('(', 5, 2), (')', 5, 3)
        ]
        
        for (text, row, col) in buttons:
            if text == '=':
                btn = tk.Button(
                    self.root,
                    text=text,
                    font=('Arial', 18, 'bold'),
                    bg='#4CAF50',
                    fg='white',
                    command=self.calculate,
                    height=2,
                    width=5
                )
            elif text == 'C':
                btn = tk.Button(
                    self.root,
                    text=text,
                    font=('Arial', 18, 'bold'),
                    bg='#f44336',
                    fg='white',
                    command=self.clear,
                    height=2,
                    width=5
                )
            elif text == '←':
                btn = tk.Button(
                    self.root,
                    text=text,
                    font=('Arial', 18, 'bold'),
                    bg='#FF9800',
                    fg='white',
                    command=self.backspace,
                    height=2,
                    width=5
                )
            elif text in ['+', '-', '*', '/']:
                btn = tk.Button(
                    self.root,
                    text=text,
                    font=('Arial', 18, 'bold'),
                    bg='#2196F3',
                    fg='white',
                    command=lambda t=text: self.append_to_expression(t),
                    height=2,
                    width=5
                )
            else:
                btn = tk.Button(
                    self.root,
                    text=text,
                    font=('Arial', 18),
                    bg='#e0e0e0',
                    command=lambda t=text: self.append_to_expression(t),
                    height=2,
                    width=5
                )
            
            btn.grid(row=row, column=col, padx=5, pady=5)
    
    def append_to_expression(self, value):
        self.expression += str(value)
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, self.expression)
    
    def clear(self):
        self.expression = ""
        self.input_field.delete(0, tk.END)
    
    def backspace(self):
        self.expression = self.expression[:-1]
        self.input_field.delete(0, tk.END)
        self.input_field.insert(0, self.expression)
    
    def calculate(self):
        try:
            result = eval(self.expression)
            self.input_field.delete(0, tk.END)
            self.input_field.insert(0, str(result))
            self.expression = str(result)
        except ZeroDivisionError:
            messagebox.showerror("Ошибка", "Деление на ноль!")
            self.clear()
        except Exception as e:
            messagebox.showerror("Ошибка", "Неверное выражение!")
            self.clear()

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

