from tkinter import *
from PIL import Image, ImageTk, ImageDraw
from datetime import *
import time
from math import *
# import pymysql
import sqlite3
from tkinter import messagebox, ttk
import os


class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        left_lbl = Label(self.root, bg="#08A3D2", bd=0)
        left_lbl.place(x=0, y=0, relheight=1, width=600)
        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)
        # frames
        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=250, y=100, width=800, height=500)
        title = Label(login_frame, text="LOGIN HERE", font=(
            "times new roman", 30, "bold"), bg="white", fg="#08A3D2").place(x=250, y=50)
        email = Label(login_frame, text="EMAIL ADDRESS", font=(
            "times new roman", 18, "bold"), bg="white", fg="gray").place(x=250, y=150)
        self.txt_email = Entry(login_frame, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_email.place(x=250, y=180, width=350, height=35)
        pass_ = Label(login_frame, text="PASSWORD", font=(
            "times new roman", 18, "bold"), bg="white", fg="gray").place(x=250, y=250)
        self.txt_pass_ = Entry(login_frame, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_pass_.place(x=250, y=280, width=350, height=35)
        btn_reg = Button(
            login_frame, cursor="hand2", command=self.register_window, text="Register new Account?", font=("times new roman", 14), bg="white", bd=0, fg="#B00857").place(x=250, y=320)
        btn_forget = Button(
            login_frame, cursor="hand2", command=self.forget_password_window, text="Forget Password", font=("times new roman", 14), bg="white", bd=0, fg="#B00857").place(x=450, y=320)
        btn_login = Button(
            login_frame, text="Login", command=self.login, font=("times new roman", 20, "bold"), fg="white", bg="#B00857", cursor="hand2").place(x=250, y=380, width=180, height=40)
        #####################################clock##############################
        self.lbl = Label(self.root, text="\nClock", font=(
            "Book Antiqua", 25, "bold"), compound=BOTTOM, fg="white", bg="#081923", bd=0)
        self.lbl.place(x=90, y=120, height=450, width=350)
        # self.clock_image()
        self.working()

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_pass.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_pass_.delete(0, END)
        self.txt_email.delete(0, END)

    def forget_password(self):
        if self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_new_pass.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root2)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=?",
                            (self.txt_email.get(), self.cmb_quest.get(), self.txt_answer.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Please provide correct security or answer", parent=self.root2)

                else:
                    cur.execute("update employee set password=? where email=?",
                                (self.txt_new_pass.get(), self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo(
                        "Success", "Your password has been reset,you can login now", parent=self.root2)
                    # row2 = cur.fetchone()
                    self.reset()
                    self.root2.destroy()

            except EXCEPTION as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)

    def forget_password_window(self):
        if self.txt_email.get() == "":
            messagebox.showerror(
                "Error", "First enter your email to reset your", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=?",
                            (self.txt_email.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Please enter your valid email to reset your password", parent=self.root)
                else:
                    con.close()
                    self.root2 = Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+450+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    t = Label(self.root2, text="Forget Password", font=(
                        "times new roman", 20, "bold"), bg="white", fg="red").place(x=0, y=10, relwidth=1)
            # forget paassword
                    question = Label(self.root2, text="Security Question", font=(
                        "times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=100)
                    self.cmb_quest = ttk.Combobox(self.root2, font=(
                        "times new roman", 13), state='readonly', justify=CENTER)
                    self.cmb_quest['values'] = ("Select", "Your pet name",
                                                "Your birth place", "Your best friend name")
                    self.cmb_quest.place(x=50, y=130, width=250)
                    self.cmb_quest.current(0)
                    answer = Label(self.root2, text="Answer", font=(
                        "times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=180)
                    self.txt_answer = Entry(self.root2, font=("times new roman", 15),
                                            bg="lightgray")
                    self.txt_answer.place(x=50, y=210, width=250)
                    new_password = Label(self.root2, text="New Password", font=(
                        "times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=260)
                    self.txt_new_pass = Entry(self.root2, font=("times new roman", 15),
                                              bg="lightgray")
                    self.txt_new_pass.place(x=50, y=290, width=250)
                    btn_change_password = Button(self.root2, text="Reset Password", command=self.forget_password, bg="green", fg="white", font=(
                        "times new roman", 15, "bold")).place(x=100, y=340)
            except EXCEPTION as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)

    def register_window(self):
        self.root.destroy()
        import register

    def login(self):
        # print(self.txt_email.get(), self.txt_pass_.get())
        if self.txt_email.get() == "" or self.txt_pass_.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                con = sqlite3.connect(database="rms.db")
                cur = con.cursor()
                cur.execute("select * from employee where email=? and password=?",
                            (self.txt_email.get(), self.txt_pass_.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror(
                        "Error", "Invalid username or password", parent=self.root)
                else:
                    messagebox.showinfo(
                        "Success", f"Welcome: {self.txt_email.get()}", parent=self.root)

                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()
            except EXCEPTION as es:
                messagebox.showerror(
                    "Error", f"Error due to: {str(es)}", parent=self.root)

    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)
        bg = Image.open("images/c.png")
        bg = bg.resize((300, 300), Image.ANTIALIAS)
        clock.paste(bg, (50, 50))
        # formula to rotate the anticlock
        # angle_in_radians = angle_in_degrees*math.pi/180
        # line_length=100
        # center_x=250
        # center_y=250
        # end_x=center_x+line_length*math.cos(angle_in_radians)
        # end_y=center_y-line_length*math.sin(angle_in_radians)
        # for Hour line image
        # x1,y1,x2,y2
        origin = 200, 200
        draw.line((origin, 200+50*sin(radians(hr)), 200-50 *
                  cos(radians(hr))), fill="#DF005E", width=4)
        # for Minutes line image
        draw.line((origin, 200+80*sin(radians(min_)), 200 -
                  80*cos(radians(min_))), fill="white", width=3)
        # for Seconds line image
        draw.line((origin, 200+100*sin(radians(sec_)), 200 -
                  100*cos(radians(sec_))), fill="yellow", width=2)
        # ellipse
        draw.ellipse((195, 195, 210, 210), fill="#1AD5D5")
        clock.save("images/clock_new.png")

    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr = (h/12)*360
        min_ = (m/60)*360
        sec_ = (s/60)*360
        # print(h, m, s)
        # print(hr,min_,sec_)
        self.clock_image(hr, min_, sec_)
        self.img = ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)


root = Tk()
obj = Login_window(root)
root.mainloop()
