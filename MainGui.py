import tkinter as tk
from tkinter import *
from Password_logic import password_rating                      ### This file will not run if all files are not in the same directory
from BreachCheck import check_password_sample_space, check_number_of_leaked_passwords
from PasswordGen import generate_password, copy_to_clipboard

class root_window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        ### Declare root Frame
        self.title("Super Secure Password Checker")
        root_window = tk.Frame(self, height=1000, width=1000)
        root_window.pack()

        ### initializes all frames with root frame and root window then adds it to an array to access later
        self.frames = {}
        for F in (generator, checker, database):
            frame = F(root_window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.change_frame(generator)  

    
    def change_frame(self, frame):  ### takes in class and raises it to become the displayed frame, takes the values from the array of all initialized classess
        frame = self.frames[frame]
        frame.tkraise()


class generator(tk.Frame):
    def __init__(self, container, parent_class):
        tk.Frame.__init__(self, container)
        self.configure(bg="#1c1b1b")
        self.var1=tk.IntVar()
        self.var2=tk.IntVar()
        self.var3=tk.IntVar()
        self.var4=tk.IntVar()
        self.var5=tk.IntVar()

        ### Place Holders
        self.ph1 = tk.Label(self, bg="#1c1b1b")
        self.ph1.grid(row = 1, column = 2, columnspan = 3)

        ### Declare all checkboxs
        self.symbols = tk.Checkbutton(self, text="Symbols", onvalue=True, offvalue=False, command=lambda: self.genpassword(self.scale.get()), variable=self.var1, bg="#1c1b1b", fg="#FFFFFF")
        self.numbers = tk.Checkbutton(self, text="Numbers", onvalue=True, offvalue=False, command=lambda: self.genpassword(self.scale.get()), variable=self.var2, bg="#1c1b1b", fg="#FFFFFF")
        self.upper = tk.Checkbutton(self, text="Upper Case", onvalue=True, offvalue=False, command=lambda: self.genpassword(self.scale.get()), variable=self.var3, bg="#1c1b1b", fg="#FFFFFF")
        self.symbols.grid(row=2, column = 0)
        self.numbers.grid(row=3, column = 0)
        self.upper.grid(row=4, column = 0)
 

        ### Declare all labels, buttons, and scales
        self.pass_lbl = tk.Label(self, bg="#1c1b1b", fg="#FFFFFF")
        self.pass_lbl.grid(row = 2, column = 1)
        self.scale = tk.Scale(self, orient="horizontal", from_=1, to=25, length=150, bg="#1c1b1b", fg="#FFFFFF", command=self.genpassword)
        self.scale.grid(row=4, column=2)
        self.clipboard = tk.Button(self, text="Copy To Clipboard", command=lambda: copy_to_clipboard(str(self.pass_lbl.cget("text")[10:])))
        self.clipboard.grid(row=2, column=2)
        
        ### Initalize Different Frame Buttons to change the Root Window Frame
        switch_generator = tk.Button(self, text="Generator", command=lambda: parent_class.change_frame(generator), bg="#ba03fc")
        switch_checker = tk.Button(self, text="Checker", command= lambda: parent_class.change_frame(checker))
        switch_checker.grid(row=0, column=1, columnspan=1)
        switch_generator.grid(row=0, column=3, columnspan=1)

    
    def genpassword(self, length): ### Takes in the scale value and True/False values from all the checkboxes
        password = generate_password(int(length), self.var2.get(), self.var1.get(), self.var3.get())  ### Function than parses it into a function then returns random password
        self.pass_lbl.configure(text = f"Password : {str(password)}")


class checker(tk.Frame):
    def __init__(self, container, parent_class):
        tk.Frame.__init__(self, container)
        self.configure(bg="#1c1b1b")
        
        ### Place Holders
        self.ph1 = tk.Label(self, bg="#1c1b1b")
        self.ph1.grid(row = 1, column = 2, columnspan = 3)

        ### Declare all entries, labels, and buttons
        self.breached_lbl = tk.Label(self, text = "",  bg="#1c1b1b", fg="#FFFFFF")
        self.pass_inpt = tk.Entry(self, validate="all", validatecommand=self.password_checker, borderwidth=3)
        self.pass_inpt.grid(row=2, column=1, columnspan=3)
        self.password_rating_label = tk.Label(self, text="0 / 15", bg="#1c1b1b", fg="#FFFFFF")
        self.password_rating_label.grid(row=3, column=1, columnspan=3)
        self.t_t_k = tk.Label(self, text="Time to Crack : 0",  bg="#1c1b1b", fg="#FFFFFF")
        self.t_t_k.grid(row=4, column=1, columnspan=3)
        self.graph = tk.Button(self, text="HaveIBeenPwned", command=self.pwned,  bg="#1c1b1b", fg="#FFFFFF")
        self.graph.grid(row=5, column=1, columnspan=3)
        self.breached_lbl.grid(column=5, row=2)

        ### Initalize Different Frame Buttons to change the Root Window Frame
        switch_generator = tk.Button(self, text="Generator", command=lambda: parent_class.change_frame(generator))
        switch_checker = tk.Button(self, text="Checker", command= lambda: parent_class.change_frame(checker), bg="#ba03fc")
        switch_checker.grid(row=0, column=1, columnspan=1)
        switch_generator.grid(row=0, column=3, columnspan=1)
    
    def pwned(self): ### Function takes in password and returns number of times password has been breached
        pwned = check_number_of_leaked_passwords(str(self.pass_inpt.get()))
        if pwned != 0:
            self.breached_lbl.configure(text=f"Password Pwned : {pwned} Times!")
        else:
            print("Somthing went wrong")
 
    def password_checker(self):  ### Takes in value from pass_inpt entry then modifys password rating label and time to krack label to the require values returned from the external functions
        sample_space = str(check_password_sample_space(str(self.pass_inpt.get())))
        rating = password_rating(password=str(self.pass_inpt.get()))
        print(f"checking : value -> {str(self.pass_inpt.get())} || Time to Crack -> {sample_space}")
        self.password_rating_label.configure(text= f"{rating} / 15")
        self.t_t_k.configure(text= f"Time to Crack : {sample_space[0:14]}")
        return True


class database(tk.Frame):
    def __init__(self, container, parent_class):
        tk.Frame.__init__(self, container)
        self.configure(bg="#1c1b1b")

        switch_generator = tk.Button(self, text="Generator", command=lambda: parent_class.change_frame(generator))
        switch_checker = tk.Button(self, text="Checker", command= lambda: parent_class.change_frame(checker))
        switch_checker.grid(row=0, column=1, columnspan=1)
        switch_generator.grid(row=0, column=3, columnspan=1)
    

if __name__ == "__main__":
    ### Initialize root window and customize size, and colour
    root = root_window()
    root.configure(bg="#1c1b1b")
    #root.geometry("500x500")
    root.resizable(0,0)
    root.mainloop() 