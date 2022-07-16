from tkinter import *
import random
BACKGROUND_COLOR = "NavajoWhite2"

class Interface:
	def __init__(self):
		self.window = Tk()
		self.window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
		self.window.title("Hra pro moji dceru")
		self.player_score = 0
		self.computer_score = 0

		self.player_score_label = Label(text=f"Hrac: {self.player_score}", fg="black", bg=BACKGROUND_COLOR, font=("Arial", 30, "italic"),
		                           padx=30, pady=30)
		self.player_score_label.grid(column=0, row=0)

		self.computer_score_label = Label(text=f"Protivnik: {self.computer_score}", fg="black", bg=BACKGROUND_COLOR, font=("Arial", 30, "italic"),
		                             padx=30, pady=30)
		self.computer_score_label.grid(column=1, row=0)

		self.canvas1 = Canvas(width=400, height=200, bg=BACKGROUND_COLOR, highlightthickness=0)

		self.card2_image = PhotoImage(file="card2.png")
		self.canvas1.create_image(200, 100, image=self.card2_image)
		self.canvas1.grid(column=0, row=1, padx=20, pady=20)

		self.canvas2 = Canvas(width=400, height=200, bg=BACKGROUND_COLOR, highlightthickness=0)
		self.card_image = PhotoImage(file="card.png")
		self.canvas2.create_image(200, 100, image=self.card_image)
		self.canvas2.grid(column=1, row=1, padx=20, pady=20, columnspan=2)

		self.rock_image = PhotoImage(file="rock100x100.png")
		self.rock_button = Button(image=self.rock_image, command=self.choose_rock)
		self.rock_button.grid(column=0, row=3, padx=30, pady=30)

		self.scissors_image = PhotoImage(file="nuzky100x100.png")
		self.scissors_button = Button(image=self.scissors_image, command=self.choose_scissors)
		self.scissors_button.grid(column=1, row=3, padx=30, pady=30)

		self.paper_image = PhotoImage(file="paper100x100.png")
		self.paper_button = Button(image=self.paper_image, command=self.choose_paper)
		self.paper_button.grid(column=2, row=3, padx=30, pady=30)

		self.window.mainloop()

	def choose_paper(self):
		self.result_of_round()
		self.canvas1.create_image(200, 100, image=self.paper_image)
		self.computer_round()
		if computer_number == 0:
			print("is draw")
		elif computer_number == 1:
			self.win()
		else:
			self.loose()


	def choose_rock(self):
		self.result_of_round()
		self.canvas1.create_image(200, 100, image=self.rock_image)
		self.computer_round()
		if computer_number == 0:
			self.loose()
		elif computer_number == 1:
			print("Is draw")
		else:
			self.win()

	def choose_scissors(self):
		self.result_of_round()
		self.canvas1.create_image(200, 100, image=self.scissors_image)
		self.computer_round()
		if computer_number == 0:
			self.win()
		elif computer_number == 1:
			self.loose()
		else:
			print("Is draw")

	def computer_round(self):
		global computer_number
		computer_number= random.randint(0, 2)
		if computer_number == 0:
			self.canvas2.create_image(200, 100, image=self.paper_image)
		elif computer_number == 1:
			self.canvas2.create_image(200, 100, image=self.rock_image)
		elif computer_number == 2:
			self.canvas2.create_image(200, 100, image=self.scissors_image)

	def next_round(self):
		if self.player_score < 3 and self.computer_score < 3:
			self.canvas1.create_image(200, 100, image=self.card2_image)
			self.canvas2.create_image(200, 100, image=self.card_image)
			self.button_enabled()
		else:
			self.button_disabled()
			self.canvas1.create_image(200, 100, image=self.card2_image)
			self.canvas2.create_image(200, 100, image=self.card_image)
			if self.player_score > self.computer_score:
				self.canvas1.create_text(200, 100, text="You win", font=("Arial", 30, "italic"))
				self.canvas2.create_text(200, 100, text="You loose", font=("Arial", 30, "italic"))
			elif self.player_score < self.computer_score:
				self.canvas2.create_text(200, 100, text="You win", font=("Arial", 30, "italic"))
				self.canvas1.create_text(200, 100, text="You loose", font=("Arial", 30, "italic"))


	def win(self):
		self.player_score += 1
		self.player_score_label.config(text=f"Hrac: {self.player_score}")

	def loose(self):
		self.computer_score += 1
		self.computer_score_label.config(text=f"Protivnik: {self.computer_score}")

	def result_of_round(self):
		self.button_disabled()
		self.window.after(1000, func=self.next_round)

	def button_disabled(self):
		self.scissors_button["state"] = DISABLED
		self.rock_button["state"] = DISABLED
		self.paper_button["state"] = DISABLED

	def button_enabled(self):
		self.scissors_button["state"] = ACTIVE
		self.rock_button["state"] = ACTIVE
		self.paper_button["state"] = ACTIVE

	def print_score(self):
		print(self.player_score)
		print(self.computer_score)
		if self.player_score == 3:
			self.button_disabled()
