import time
import datetime
import turtle
from tqdm import tqdm
import colorama
import pyglet
import os
import sys
from prettytable import PrettyTable
if sys.platform == "win32":
    os.system("")

Ram1 = "35 mb"
Ram2 = "128 mb"
Disk = "C:\\4GB"

print("="*35)
print("StartOS")
print("="*35)
for i in tqdm(range(3)):
    time.sleep(0.5)

print("="*35)
print("RAM:"+Ram1)
print("ROM:"+Ram2)
print("DISK:"+Disk)
print("="*35)
table1 = PrettyTable()
table1.field_names = ["MaxOS"]
table1.add_rows([
        ["Version 1.0"],
        ["FazbearDevelopmentGame"],
        ["GameJolt:https://gamejolt.com/@FazbearDevelopmentGame"],
        ["Github:https://github.com/FazbearDevelopmentGame"],
        ["YouTube:https://www.youtube.com/c/FazbearDevelopmentGame"]
        ])
print(table1)
table = PrettyTable()
table.field_names = ["Commands:", ""]
table.add_rows([
            [">>help", "get list of the commands"],
            [">>info", "print information about OS"],
            [">>time", "print current time (HH.MM.SS)"],
            [">>date", "print current date (DD.MM.YY)"],
            [">>MaxOsPc","MaxOs"],
            [">>Files","print current Files"],
            [">>exit", "exit the program"]
        ])
print(table)
while True:
    print("=" * 35)
    command = input("C:\\User:")
    if command == "help":
        table = PrettyTable()
        table.field_names = ["Commands:", ""]
        table.add_rows([
            [">>help", "get list of the commands"],
            [">>info", "print information about OS"],
            [">>time", "print current time (HH.MM.SS)"],
            [">>date", "print current date (DD.MM.YY)"],
            [">>Files", "print current Files"],
            [">>command", "exit the program"],
            [">>exit", "exit the program"]
        ])
        print(table)
    elif command == "info":
        table1 = PrettyTable()
        table1.field_names = ["MaxOS"]
        table1.add_rows([
            ["Version 1.0"],
            ["FazbearDevelopmentGame"],
            ["GameJolt:https://gamejolt.com/@FazbearDevelopmentGame"],
            ["Github:https://github.com/FazbearDevelopmentGame"],
            ["YouTube:https://www.youtube.com/c/FazbearDevelopmentGame"],

        ])
        print(table1)
        table = PrettyTable()
        table.add_rows([
            ["MaxOS — это операционная система на основе Python с графическим интерфейсом и командной строкой, сочетающая в себе функции Windows, macOS и LightOS."],
            ["Она работает через окна и команды."],
            ["Функции включают справку, информацию о системе, калькулятор и файловые папки."],
            ["В более старых версиях для остановки воспроизведения музыки требовалась перезагрузка."],
            ["Выключение осуществляется с помощью команд Sleep или Exit."]
        ])
        print(table)
    elif command == "command":
        table1 = PrettyTable()
        table1.field_names = ["Commands:", ""]
        table1.add_rows([
            [">>help", "get list of the commands"],
            [">>info", "print information about OS"],
            [">>time", "print current time (HH.MM.SS)"],
            [">>date", "print current date (DD.MM.YY)"],
            [">>Files", "print current Files"],
            [">>Audios", "soon"],
            [">>Audio№1", "soon"],
            [">>Audio№2", "soon"],
            [">>Audio№3", "soon"],
            [">>Audio№4", "soon"],
            [">>Calculator", "calculator"],
            [">>command", "print current command"],
            [">>exit", "exit the program"]
        ])
        print(table1)
    elif command == "time":
        print("\r",time.strftime("%H:%M:%S"),"\r")
    elif command == "date":
        current_date = datetime.datetime.now()
        print("\r",current_date.strftime("%d/%m/%Y"),"\r")
    elif command == "Files":
        table1 = PrettyTable()
        table1.field_names = ["Files:", ""]
        table1.add_rows([
            [">>Audios", "audio"],
            [">>System", "system"],
            [">>Command", "command"],
            [">>Calculator", "calculator"],
        ])
        print(table1)
    elif command == "Audios":
        table1 = PrettyTable()
        table1.field_names = ["Files:", ""]
        table1.add_rows([
            [">>Audio№1", "audio№1"],
            [">>Audio№2", "audio№2"],
            [">>Audio№3", "audio№3"],
            [">>Audio№4", "audio№4"]
        ])
    elif command == "System":
        table1 = PrettyTable()
        table1.field_names = ["Files:", ""]
        table1.add_rows([
            [">>System", "system"],
        ])
        print(table1)
        turtle.mainloop()
    elif command == "Calculator":
        from tkinter import *

        # Let's create the Tkinter window
        window = Tk()

        # Then, you will define the size of the window in width(312) and height(324) using the 'geometry' method
        window.geometry("347x423")
        window.resizable(False, False)

        # In order to prevent the window from getting resized you will call 'resizable' method on the window
        # window.resizable(0, 0)

        # Finally, define the title of the window
        window.title("Calculator")


        # Let's now define the required functions for the Calculator to function properly.

        # 1. First is the button click 'btn_click' function which will continuously update the input field whenever a number is entered or any button is pressed it will act as a button click update.
        def btn_click(item):
            global expression
            expression = expression + str(item)
            input_text.set(expression)


        # 2. Second is the button clear 'btn_clear' function clears the input field or previous calculations using the button "C"
        def btn_clear():
            global expression
            expression = ""
            input_text.set("")


        # 3. Third and the final function is button equal ("=") 'btn_equal' function which will calculate the expression present in input field. For example: User clicks button 2, + and 3 then clicks "=" will result in an output 5.
        def btn_equal():
            global expression
            result = str(
                eval(expression))  # 'eval' function is used for evaluating the string expressions directly
            # you can also implement your own function to evalute the expression istead of 'eval' function
            input_text.set(result)
            expression = ""


        expression = ""
        # In order to get the instance of the input field 'StringVar()' is used
        input_text = StringVar()

        # Once all the functions are defined then comes the main section where you will start defining the structure of the calculator inside the GUI.

        # The first thing is to create a frame for the input field
        input_frame = Frame(window, width=312, height=50, bd=0, highlightbackground="black",
                            highlightcolor="black",
                            highlightthickness=1)
        input_frame.pack(side=TOP)

        # Then you will create an input field inside the 'Frame' that was created in the previous step. Here the digits or the output will be displayed as 'right' aligned
        input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50,
                            bg="#eee", bd=0,
                            justify=RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)  # 'ipady' is an internal padding to increase the height of input field

        # Once you have the input field defined then you need a separate frame which will incorporate all the buttons inside it below the 'input field'
        btns_frame = Frame(window, width=312, height=272.5, bg="grey")
        btns_frame.pack()

        # The first row will comprise of the buttons 'Clear (C)' and 'Divide (/)'
        clear = Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2",
                       command=lambda: btn_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        divide = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                        command=lambda: btn_click("/")).grid(row=0, column=3, padx=1, pady=1)

        # The second row will comprise of the buttons '7', '8', '9' and 'Multiply (*)'
        seven = Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                       command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
        eight = Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                       command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
        nine = Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                      command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
        multiply = Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                          command=lambda: btn_click("*")).grid(row=1, column=3, padx=1, pady=1)

        # The third row will comprise of the buttons '4', '5', '6' and 'Subtract (-)'
        four = Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                      command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)
        five = Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                      command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
        six = Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                     command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)
        minus = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                       command=lambda: btn_click("-")).grid(row=2, column=3, padx=1, pady=1)

        # The fourth row will comprise of the buttons '1', '2', '3' and 'Addition (+)'
        one = Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                     command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)
        two = Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                     command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)
        three = Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                       command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)
        plus = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                      command=lambda: btn_click("+")).grid(row=3, column=3, padx=1, pady=1)

        # Finally, the fifth row will comprise of the buttons '0', 'Decimal (.)', and 'Equal To (=)'
        zero = Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
                      command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        point = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                       command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)
        equals = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                        command=lambda: btn_equal()).grid(row=4, column=3, padx=1, pady=1)

        window.mainloop()
    elif command == "MaxOsPc":
        from tkinter import Button, Frame, Label
        import customtkinter as CTk
        import turtle
        import keyboard
        import time
        import tkinter as tk
        import datetime
        import time


        class App(CTk.CTk):
            def __init__(self):
                super().__init__()

                self.geometry("500x480")
                self.title("MaxOs")
                self.resizable(False, False)
                self.configure(fg_color="#4a2c4a")

                self.frame = CTk.CTkFrame(
                    master=self,
                    fg_color="#b84a8a",
                    border_color="#4a2c4a",
                    border_width=2,
                    corner_radius=10,
                    width=85,
                    height=65
                )
                self.frame.place(x=205, y=410)

                self.btn1 = CTk.CTkButton(master=self, text="system", command=self.system_command,
                                          width=70,
                                          height=70,
                                          corner_radius=15,
                                          fg_color="#f9b5a1",
                                          hover_color="#e6947a",
                                          text_color="black",
                                          font=("Arial", 12, "bold")
                                          )
                self.btn1.place(x=10, y=25)
                self.btn2 = CTk.CTkButton(master=self, text="Sleep", command=self.exit_command,
                                          width=20,
                                          height=50,
                                          corner_radius=15,
                                          fg_color="#f9b5a1",
                                          hover_color="#e6947a",
                                          text_color="black",
                                          font=("Arial", 12, "bold")
                                          )
                self.btn2.place(x=215, y=417)
                self.btn3 = CTk.CTkButton(master=self, text="Command", command=self.Command_command,
                                          width=20,
                                          height=50,
                                          corner_radius=15,
                                          fg_color="#f9b5a1",
                                          hover_color="#e6947a",
                                          text_color="black",
                                          font=("Arial", 12, "bold")
                                          )
                self.btn3.place(x=10, y=105)

            def system_command(self):
                print("system")
                root = tk.Tk()
                root.geometry("650x500")
                root.title("System")
                root.resizable(False, False)
                root.configure(bg='#4a2c4a')
                text_label = tk.Label(root, text="System Information", font=('Arial', 24, 'bold'), bg='#4a2c4a',
                                      fg='white')
                text_label.place(relx=0.5, rely=0.8, anchor='center')
                text_label0 = tk.Label(root, text="=" * 75, font=('Arial', 24, 'bold'), bg='#4a2c4a', fg='#f9b5a1')
                text_label0.place(relx=0.0, rely=0.0, anchor='center')
                text_label1 = tk.Label(root, text="DISK:C:/640 mb", font=('Arial', 24, 'bold'), bg='#4a2c4a',
                                       fg='#f9b5a1')
                text_label1.place(relx=0.2, rely=0.1, anchor='center')
                text_label2 = tk.Label(root, text="DISK:G:/640 mb", font=('Arial', 24, 'bold'), bg='#4a2c4a',
                                       fg='#f9b5a1')
                text_label2.place(relx=0.2, rely=0.2, anchor='center')
                text_label3 = tk.Label(root, text="RAM:125 mb", font=('Arial', 24, 'bold'), bg='#4a2c4a', fg='#f9b5a1')
                text_label3.place(relx=0.2, rely=0.3, anchor='center')
                text_label4 = tk.Label(root, text="ROM:105 mb", font=('Arial', 24, 'bold'), bg='#4a2c4a', fg='#f9b5a1')
                text_label4.place(relx=0.2, rely=0.4, anchor='center')
                text_label5 = tk.Label(root, text="=" * 75, font=('Arial', 24, 'bold'), bg='#4a2c4a', fg='#f9b5a1')
                text_label5.place(relx=0.0, rely=0.5, anchor='center')
                text_label6 = tk.Label(root, text="User:FDG", font=('Arial', 24, 'bold'), bg='#4a2c4a', fg='#f9b5a1')
                text_label6.place(relx=0.2, rely=0.6, anchor='center')
                text_label7 = tk.Label(root, text="Password:368025", font=('Arial', 24, 'bold'), bg='#4a2c4a',
                                       fg='#f9b5a1')
                text_label7.place(relx=0.3, rely=0.7, anchor='center')
                root.mainloop()

            def Command_command(self):
                print("command")
                root = tk.Tk()
                root.geometry("650x500")
                root.title("Command")
                root.resizable(False, False)
                root.configure(bg='#4a2c4a')
                text_label = tk.Label(root, text="Command", font=('Arial', 24, 'bold'), bg='#4a2c4a', fg='white')
                text_label.place(relx=0.5, rely=0.1, anchor='center')
                text_label0 = tk.Label(root, text="=" * 75, font=('Arial', 24, 'bold'), bg='#4a2c4a', fg='#f9b5a1')
                text_label0.place(relx=0.0, rely=0.0, anchor='center')
                text_label0 = tk.Label(root, text="=" * 75, font=('Arial', 24, 'bold'), bg='#4a2c4a', fg='#f9b5a1')
                text_label0.place(relx=0.0, rely=0.2, anchor='center')
                text_label1 = tk.Label(root, text="Help", font=('Arial', 24, 'bold'), bg='#4a2c4a', fg='#f9b5a1')
                text_label1.place(relx=0.5, rely=0.2, anchor='center')
                text_label2 = tk.Label(root, text="System", font=('Arial', 24, 'bold'), bg='#4a2c4a', fg='#f9b5a1')
                text_label2.place(relx=0.5, rely=0.3, anchor='center')
                text_label3 = tk.Label(root, text="info", font=('Arial', 24, 'bold'), bg='#4a2c4a', fg='#f9b5a1')
                text_label3.place(relx=0.5, rely=0.4, anchor='center')
                text_label4 = tk.Label(root, text="Games", font=('Arial', 24, 'bold'), bg='#4a2c4a', fg='#f9b5a1')
                text_label4.place(relx=0.5, rely=0.5, anchor='center')
                text_label6 = tk.Label(root, text="User", font=('Arial', 24, 'bold'), bg='#4a2c4a', fg='#f9b5a1')
                text_label6.place(relx=0.5, rely=0.6, anchor='center')
                text_label7 = tk.Label(root, text="Password", font=('Arial', 24, 'bold'), bg='#4a2c4a', fg='#f9b5a1')
                text_label7.place(relx=0.5, rely=0.7, anchor='center')
                root.mainloop()

            def exit_command(self):
                self.destroy()


        if __name__ == "__main__":
            app = App()
            app.mainloop()
    elif command == "exit":
        break
    else:
        print("=" * 35)
        print("ERROR Command:"+command)


