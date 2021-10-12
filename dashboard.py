from tkinter import*
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
import os
from PIL import Image, ImageTk, ImageDraw
from datetime import *
import time
from math import *
# import pymysql
import sqlite3
from tkinter import messagebox, ttk

class RMS:
    def __init__(self, root):
        self.root = root  # reintialising root
        self.root.title("Student Result Software")
        # for width and height of the window # (width*height+placing in x axis + placing in y axis)
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")  # for background colour
        # icons
        title = Label(self.root, text="Student Result Software", padx=10, compound=LEFT, font=(
            "goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height="50")
        # Menu
        M_Frame = LabelFrame(self.root, text="Menu", font=(
            "times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1340, height=80)
        btn_course = Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377",
                            fg="white", cursor="hand2", command=self.add_course).place(x=20, y=5, width=200, height=40)
        btn_student = Button(M_Frame, text="Students", font=("goudy old style", 15, "bold"), bg="#0b5377",
                             fg="white", cursor="hand2", command=self.add_student).place(x=240, y=5, width=200, height=40)
        btn_result = Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377",
                            fg="white", cursor="hand2", command=self.add_result).place(x=460, y=5, width=200, height=40)
        btn_view = Button(M_Frame, text="View student result", font=("goudy old style", 15, "bold"), bg="#0b5377",
                          fg="white", cursor="hand2", command=self.add_report).place(x=680, y=5, width=200, height=40)
        btn_logout = Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"),
                            bg="#0b5377", fg="white", cursor="hand2", command=self.logout).place(x=900, y=5, width=200, height=40)
        btn_exit = Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"),
                          bg="#0b5377", fg="white", cursor="hand2", command=self.exit_).place(x=1120, y=5, width=200, height=40)
        # content window
        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920, 350), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image=self.bg_img).place(
            x=400, y=170, width=920, height=350)
        # update details
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]", font=(
            "old goudy style", 20), bd=10, relief=RIDGE, bg="#e43B06", fg="white")
        self.lbl_course.place(x=400, y=530, width=300, height=100)
        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]", font=(
            "old goudy style", 20), bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=710, y=530, width=300, height=100)
        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]", font=(
            "old goudy style", 20), bd=10, relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=1020, y=530, width=300, height=100)
        #####################################clock##############################
        self.lbl = Label(self.root, text="\nClock", font=(
            "Book Antiqua", 25, "bold"), compound=BOTTOM, fg="white", bg="#081923", bd=0)
        self.lbl.place(x=10, y=170, height=460, width=350)
        # self.clock_image()
        self.working()
        # for footer
        footer = Label(self.root, text="SRS - Manage Your Student Results\nContact us for any technical issue: 7073xxxx18",
                       font=("goudy old style", 12), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)
        self.update_details()
    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")

            cur.execute("select * from student")
            cr = cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")
            cur.execute("select * from result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")

            self.lbl_course.after(200, self.update_details)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}")

    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr = (h/12)*360
        min_ = (m/60)*360
        sec_ = (s/60)*360
        self.clock_image(hr, min_, sec_)
        self.img = ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)

    def clock_image(self, hr, min_, sec_):
        clock = Image.new("RGB", (400, 400), (8, 25, 35))
        draw = ImageDraw.Draw(clock)
        bg = Image.open("images/c.png")
        bg = bg.resize((300, 300), Image.ANTIALIAS)
        clock.paste(bg, (50, 50))
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
    # to open course panel
    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)
    # to open student panel
    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)
    # to open result panel
    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)
    # to open view result
    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)
    # logout
    def logout(self):
        op = messagebox.askyesno(
            "Confirm", "Do you really want to logout?", parent=self.root)
        if op == True:
            self.root.destroy()
            os.system("python login.py")
    def exit_(self):
        op = messagebox.askyesno(
            "Confirm", "Do you really want to Exit?", parent=self.root)
        if op == True:
            self.root.destroy()

# For creating window
if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()