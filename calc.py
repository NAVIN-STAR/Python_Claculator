import tkinter as tk
white="#FFFFFF"
lightgray="#D3D3D3"
large_fontstyle=("Arial",40)
lable_color="#25265E"
small_fontstyle=("Arial",16)
digit_fontstyle=('Arial',24,"bold")
default_font=('Areal',20)
lightblue="#CCEDFF"

offwhite="#F8FAFF"
class Calculator:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("375x630")
        # self.window.resizable(0,0)
        self.window.title("Claculator")

        self.total_expression=""
        self.current_expression=""
        self.display_frame=self.create_display_frame()

        self.total_lebal,self.label=self.create_display_lables()


        self.digits={
            7:(1,1),8:(1,2),9:(1,3),
            4:(2,1),5:(2,2),6:(2,3),
            1:(3,1),2:(3,2),3:(3,3),
            0:(4,2),'.':(4,1)
        }
        self.operations={"/":"\u00F7","*":"\u00D7","-":"-","+":"+"}


        self.button_frame=self.create_button_frame()
        self.button_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.button_frame.rowconfigure(x,weight=1)
            self.button_frame.columnconfigure(x,weight=1)

        self.create_digit_button()
        self.create_operator_button()

        self.create_special_buttons()


    def create_special_buttons(self):

        self.create_equals_button()
        self.create_clear_button()

    def create_display_lables(self):
        total_lebal=tk.Label(self.display_frame
            ,text=self.total_expression,anchor=tk.E,bg=lightgray,fg=lable_color,padx=24,font=small_fontstyle)
        total_lebal.pack(expand=True,fill='both')

        lebal = tk.Label(self.display_frame
                               , text=self.current_expression, anchor=tk.E, bg=lightgray, fg=lable_color, padx=24,
                               font=large_fontstyle)
        lebal.pack(expand=True, fill='both')
        return total_lebal,lebal



    def create_display_frame(self):

        frame=tk.Frame(self.window,height=221,bg=lightgray)
        frame.pack(expand=True,fill='both')
        return frame




    def create_button_frame(self):
        frame=tk.Frame(self.window)
        frame.pack(expand=True,fill='both')
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()


    def create_digit_button(self):
        for digit,grid_value in self.digits.items():
            button=tk.Button(self.button_frame,text=str(digit),bg=white,fg=lable_color,font=digit_fontstyle,borderwidth=0,command=lambda x=digit:self.add_to_expression(x))
            button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)


    def append_operator(self,operator):
        self.current_expression+=operator
        self.total_expression+=self.current_expression
        self.current_expression=""
        self.update_total_lable()
        self.update_label()




    def clear(self):
        self.current_expression=""
        self.total_expression=""
        self.update_label()
        self.update_total_lable()
    def create_operator_button(self):
        i=0
        for operator,symbol in self.operations.items():
            button=tk.Button(self.button_frame,text=symbol,bg=offwhite,fg=lable_color,font=default_font,borderwidth=0,command=lambda x=operator:self.append_operator(x) )
            button.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1
    def create_clear_button(self):
        button = tk.Button(self.button_frame, text="C", bg=offwhite, fg=lable_color, font=digit_fontstyle,
                           borderwidth=0,command=self.clear)
        button.grid(row=0, column=1,columnspan=3, sticky=tk.NSEW)
    def evaluate(self):
        self.total_expression+=self.current_expression
        self.update_total_lable()
        try:
            self.current_expression=str(eval(self.total_expression))
            self.total_expression=""
        except Exception as e:
            self.current_expression="Error"
        self.update_label()
    def create_equals_button(self):
        button = tk.Button(self.button_frame, text="=", bg=lightblue, fg=lable_color, font=digit_fontstyle,
                           borderwidth=0,command=self.evaluate)
        button.grid(row=4, column=3,columnspan=2, sticky=tk.NSEW)

    def update_total_lable(self):
        self.total_lebal.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:12])

    def run(self):
        self.window.mainloop()


if __name__=="__main__":
    calc=Calculator()
    calc.run()