from bs4 import BeautifulSoup
import requests
import re
import pyttsx3
import speech_recognition as sr 
import tkinter as tk
import tkinter.messagebox
from tkinter import Label
from tkinter import Button
import webbrowser

def main_win():
	engine = pyttsx3.init()

	url = "https://coinmarketcap.com/currencies/bitcoin/"
	get = requests.get(url).text
	soup = BeautifulSoup(get, "html.parser")

	prices = soup.find_all("div",attrs={"class":"priceValue"})
	for price in prices:
		print(f"The prices of bitcoin is: {price.text}." )

	url_2 = "https://coinmarketcap.com/currencies/ethereum/"
	get_2 = requests.get(url_2).text
	soup_2 = BeautifulSoup(get_2, "html.parser")

	prices_2 = soup_2.find_all("div",attrs={"class":"priceValue"})
	for price_2 in prices_2:
		print(f"The prices of Ether is: {price_2.text}." )

	url_3 = "https://coinmarketcap.com/currencies/dogecoin/"
	get_3 = requests.get(url_3).text
	soup_3 = BeautifulSoup(get_3, "html.parser")

	prices_3 = soup_3.find_all("div",attrs={"class":"priceValue"})
	for price_3 in prices_3:
		print(f"The prices of DogeCoin is: {price_3.text}." )

	url_4 = "https://coinmarketcap.com/currencies/solana/"
	get_4 = requests.get(url_4).text
	soup_4 = BeautifulSoup(get_4,"html.parser")
	prices_4 = soup_4.find_all("div",attrs={"class":"priceValue"})
	for price_4 in prices_4:
		print(f"The price for Solana is: {price_4.text}.")
	win = tk.Tk()
	win.title("Crypto Assistant")
	win.geometry("400x200")
	win.config(bg="black")
	win.attributes("-alpha",0.8)


	l_one = Label(text="Crypto Assistant",font=("comicsansms",15))
	l_one.config(bg="black",fg="green")
	l_one.pack()

	l_2 = Label(text=price.text,font=("comicsansms",12))
	l_2.config(bg="black",fg="green")
	l_2.place(x="100",y="33")


	l_3 = Label(text="Bitcoin Price:",font=("comicsansms",12))
	l_3.config(bg="black",fg="green")
	l_3.place(x="0",y="33")

	l_4 = Label(text=price_2.text,font=("comicsansms",12))
	l_4.config(bg="black",fg="green")
	l_4.place(x="100",y="65")


	l_4 = Label(text="Ether Price:",font=("comicsansms",12))
	l_4.config(bg="black",fg="green")
	l_4.place(x="0",y="65")

	l_4 = Label(text=price_3.text,font=("comicsansms",12))
	l_4.config(bg="black",fg="green")
	l_4.place(x="120",y="95")


	l_4 = Label(text="DogeCoin Price:",font=("comicsansms",12))
	l_4.config(bg="black",fg="green")
	l_4.place(x="0",y="95")

	l_5 = Label(text=price_4.text,font=("comicsansms",12))
	l_5.config(bg="black",fg="green")
	l_5.place(x="115",y="125")


	l_5 = Label(text="Solana Price:",font=("comicsansms",12))
	l_5.config(bg="black",fg="green")
	l_5.place(x="0",y="125")

	b_one = Button(text="Bitcoin",command=lambda:webbrowser.open("https://coinmarketcap.com/currencies/bitcoin/"))
	b_one.config(width="10",padx="5",pady="5",bg="green",fg="white")
	b_one.place(x="200",y="33")

	b_two = Button(text="Ethereum",command=lambda:webbrowser.open("https://coinmarketcap.com/currencies/ethereum/"))
	b_two.config(width="10",padx="5",pady="5",bg="green",fg="white")
	b_two.place(x="200",y="65")

	b_three = Button(text="DogeCoin",command=lambda:webbrowser.open("https://coinmarketcap.com/currencies/dogecoin/"))
	b_three.config(width="10",padx="5",pady="5",bg="green",fg="white")
	b_three.place(x="200",y="95")

	b_four = Button(text="Solana",command=lambda:webbrowser.open("https://coinmarketcap.com/currencies/solana/"))
	b_four.config(width="10",padx="5",pady="5",bg="green",fg="white")
	b_four.place(x="200",y="125")

	win.iconbitmap("bitlogo.ico")

	win.mainloop()

main_win()