from tkinter import *
from tkinter import messagebox
import datetime
import os
import csv
from fpdf import FPDF
import re
from classes import Victim

class Home_screen:
    """
    This class represents the GUI and most of its' functionality
    """

    def __init__(self):
        # counter for already triaged victims
        self.triaged = 0
        # crew id str
        self.crew_id = ""
        # window definition
        self.window = Tk()
        self.window.geometry("900x700")
        self.window.title("START triage guide")

        # Wanna quit? pop up
        self.window.protocol("WM_DELETE_WINDOW", self.fnc_end_triage_btn)

        # Main header
        self.main_label = Label(
            self.window,
            text="Triage writer",
            font=("Arial", 30, "bold"),
            padx=10,
            pady=10,
        )
        self.main_label.pack(padx=10, pady=10)

        # sort of a copyright label
        self.logo_label = Label(
            self.window, text="KLOKANPES 2024", font=("Arial", 10), padx=10, pady=10
        )
        self.logo_label.pack(padx=10, pady=10, side="bottom")

        # Crew ID descriptor label
        self.id_label = Label(
            self.window,
            text="Triage Crew ID",
            font=("Arial", 15, "bold"),
            padx=10,
            pady=10,
        )
        self.id_label.place(x=10, y=100)

        # Crew ID input textbox
        self.crew_id_input = Entry(self.window, font=("Arial", 15), width=12)
        self.crew_id_input.place(x=20, y=150)

        # listens for "Enter" press while in Crew ID textbox
        self.crew_id_input.bind("<KeyPress>", self.enter)

        # Crew ID delete button
        self.delete_btn = Button(
            self.window,
            text="DELETE",
            font=("Arial", 10, "bold"),
            pady=10,
            width=7,
            command=self.fnc_delete_btn,
        )
        self.delete_btn.place(x=20, y=190)

        # Crew ID submit button
        self.submit_btn = Button(
            self.window,
            text="SUBMIT",
            font=("Arial", 10, "bold"),
            pady=10,
            width=7,
            command=self.fnc_submit_btn,
        )
        self.submit_btn.place(x=90, y=190)

        # Already triaged victims - counter
        self.number_triaged_label = Label(
            self.window,
            text=f"Victims triaged: {self.triaged}",
            font=("Arial", 15, "bold"),
            padx=10,
            pady=10,
        )
        self.number_triaged_label.place(x=700, y=100)

        # Start triage button
        self.start_triage_btn = Button(
            self.window,
            text="Start Triage",
            font=("Arial", 25, "bold"),
            padx=20,
            pady=20,
            width=13,
            command=self.fnc_start_triage_btn,
            state=DISABLED,
        )
        self.start_triage_btn.place(x=20, y=550)

        # End triage button
        self.end_triage_btn = Button(
            self.window,
            text="End Triage",
            font=("Arial", 25, "bold"),
            padx=20,
            pady=20,
            command=self.fnc_end_triage_btn,
            width=13,
            state=DISABLED,
        )
        self.end_triage_btn.place(x=570, y=550)

        # Green button
        self.green_btn = Button(
            self.window,
            text="MINOR",
            font=("Arial", 18, "bold"),
            bg="green",
            fg="black",
            padx=20,
            pady=20,
            command=self.fnc_green_btn,
            width=10,
            height=3,
            state=DISABLED,
        )
        self.green_btn.place(x=20, y=300)

        # Yellow button
        self.yellow_btn = Button(
            self.window,
            text="DELAYED",
            font=("Arial", 18, "bold"),
            bg="yellow",
            fg="black",
            padx=20,
            pady=20,
            command=self.fnc_yellow_btn,
            width=10,
            height=3,
            state=DISABLED,
        )
        self.yellow_btn.place(x=240, y=300)

        # Red button
        self.red_btn = Button(
            self.window,
            text="IMMEDIATE",
            font=("Arial", 18, "bold"),
            bg="red",
            fg="black",
            padx=20,
            pady=20,
            command=self.fnc_red_btn,
            width=10,
            height=3,
            state=DISABLED,
        )
        self.red_btn.place(x=460, y=300)

        # Black button
        self.black_btn = Button(
            self.window,
            text="EXPECTANT",
            font=("Arial", 18, "bold"),
            bg="black",
            fg="white",
            padx=20,
            pady=20,
            command=self.fnc_black_btn,
            width=10,
            height=3,
            state=DISABLED,
        )
        self.black_btn.place(x=680, y=300)

        self.window.mainloop()

    def enter(self, event):
        if event.keysym == "Return":
            self.fnc_submit_btn()

    def fnc_delete_btn(self):
        self.crew_id_input.delete(0, END)

    def fnc_submit_btn(self):
        # as per the country I am from I expect triage crews to identify either by a three digit number, or by three uppercase letters followed by three digits
        self.expression = r"^(?:[A-Z][A-Z][A-Z] )?\d\d\d$"
        if self.crew_id_input.get() != "":
            if re.search(self.expression, self.crew_id_input.get()):
                if messagebox.askyesno(title="Are you sure?", message="Are you sure?"):
                    self.crew_id = self.crew_id_input.get()
                    self.crew_id_input.config(state=DISABLED)
                    self.delete_btn.config(state=DISABLED)
                    self.submit_btn.config(state=DISABLED)
                    self.start_triage_btn.config(state=ACTIVE)
                    self.end_triage_btn.config(state=ACTIVE)

    def fnc_start_triage_btn(self):
        self.fnc_create_instance()
        self.start_triage_btn.config(state=DISABLED)
        self.green_btn.config(
            state=ACTIVE, activeforeground="black", activebackground="green"
        )
        self.yellow_btn.config(
            state=ACTIVE, activeforeground="black", activebackground="yellow"
        )
        self.red_btn.config(
            state=ACTIVE, activeforeground="black", activebackground="red"
        )
        self.black_btn.config(
            state=ACTIVE, activeforeground="white", activebackground="black"
        )

    def fnc_end_triage_btn(self):
        if messagebox.askyesno(title="Quit?", message="Do you want to quit?"):
            Check_victims_and_print(self.crew_id, self.triaged)
            self.window.destroy()

    def fnc_green_btn(self):
        self.triaged += 1
        self.victim.colour = "Green"
        self.fnc_update()
        self.fnc_victim_save()
        self.fnc_create_instance()

    def fnc_yellow_btn(self):
        self.triaged += 1
        self.victim.colour = "Yellow"
        self.fnc_update()
        self.fnc_victim_save()
        self.fnc_create_instance()

    def fnc_red_btn(self):
        self.triaged += 1
        self.victim.colour = "Red"
        self.fnc_update()
        self.fnc_victim_save()
        self.fnc_create_instance()

    def fnc_black_btn(self):
        self.triaged += 1
        self.victim.colour = "Black"
        self.fnc_update()
        self.fnc_victim_save()
        self.fnc_create_instance()

    def fnc_create_instance(self):
        self.victim = Victim()

    def fnc_victim_save(self):
        Make_csv(self.triaged, self.victim.now.date(), self.victim.formated_time, self.victim.colour)

    def fnc_update(self):
        self.number_triaged_label.config(text=f"Victims triaged: {self.triaged}")


def main():
    Home_screen()

def Print_to_pdf(crew_id, total):
    """
    This function imports the temporary .csv file and reads it before it is deleted.
    It counts the triaged victims and with some other collected data (like the Triage crew ID)
    prints it all to a pdf file as a Triage report.
    """


    # values that will be printed in the PDF
    green = 0
    yellow = 0
    red = 0
    black = 0
    crew_id = crew_id
    date_start = ""
    date_end = ""
    time_start = ""
    time_end = ""
    total = total

        # this loop count every itteration of each colour and gets the starting and enging times and dates
    with open("victims.csv", "r") as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader):
            if i == 0:
                time_start = row["time"]
                date_start = row["date"]
            if row["colour"] == "Green":
                green += 1
            elif row["colour"] == "Yellow":
                yellow += 1
            elif row["colour"] == "Red":
                red += 1
            elif row["colour"] == "Black":
                black += 1
            time_end = row["time"]
            date_end = row["date"]

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    # create page
    pdf.add_page()
    pdf.set_font("Arial", "B", 30)
    pdf.set_y(20)
    pdf.cell(50)

    # header
    pdf.cell(50, 60, "Triage report", align="C")

    # actual data
    pdf.set_y(80)
    pdf.set_font("Arial", "", 15)
    pdf.cell(100, 10, f"Triage Crew ID: {crew_id}", 0, 1)
    pdf.cell(100, 10, f"Triage started on: {date_start} at {time_start}", 0, 1)
    pdf.cell(80, 10, f"Last victim was triaged on: {date_end} at {time_end}", 0, 1)

    pdf.set_y(120)
    pdf.cell(80, 10, f"Total number of victims triaged by this crew was: {total}", 0, 1)

    pdf.set_y(140)
    pdf.set_fill_color(0, 254, 0)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(120, 10, f"Total number of MINOR victims {green}", 0, 1, fill=True)
    pdf.set_fill_color(254, 254, 0)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(120, 10, f"Total number of DELAYED victims: {yellow}", 0, 1, fill=True)
    pdf.set_fill_color(254, 0, 0)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(120, 10, f"Total number of IMMEDIATE victims: {red}", 0, 1, fill=True)
    pdf.set_fill_color(0, 0, 0)
    pdf.set_text_color(254, 254, 254)
    pdf.cell(120, 10, f"Total number of EXPECTANT victims: {black}", 0, 1, fill=True)

    # output file
    pdf.output(f"Triage report from {date_start}.pdf")

def Make_csv(id, date, time, colour):
    """
    This function creates the temporary .csv file and ads data to it on every itteration of the app, meaning after every colour button press
    a new row is added.
    """
    with open("victims.csv", "a", newline="") as file:
            writer = csv.DictWriter(
                file, fieldnames=["id", "date", "time", "colour"]
            )
            with open("victims.csv", "r") as file_check:
                if not file_check.read(1):
                    writer.writeheader()
            writer.writerow(
                {
                    "id": id,
                    "date": date,
                    "time": time,
                    "colour": colour,
                }
            )

def Check_victims_and_print(crew_id, triaged):
    if os.path.exists("victims.csv"):
                Print_to_pdf(crew_id, triaged)
                os.remove("victims.csv")


if __name__ == "__main__":
    main()
