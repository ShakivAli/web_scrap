from tkinter import *
from tkinter import Scrollbar
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34'}

def flipkart(name=''): 
    global flipkart 
    name1 = name.replace(" ", "+") 
    res = requests.get(f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off', headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')
    flipkart_page = soup.select('._4rR01T')
    flipkart_page_len=int(len(flipkart_page))
    for i in range(0,flipkart_page_len):
        flipkart_name = soup.select('._4rR01T')[i].getText().strip()
        flipkart_name = flipkart_name.upper()
        name=name.upper()
        if name in flipkart_name:
            flipkart_price = soup.select('._1_WHN1')[i].getText().strip()
            return f"{flipkart_name}\nPrice : {flipkart_price}\n"
    else:
        flipkart_price = 'Product Not Found'
        return flipkart_price


def ebay(name=''):
    global ebay
    name1 = name.replace(" ", "+")
    res = requests.get(f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={name1}&_sacat=0', headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')
    ebay_page = soup.select('.s-item__price')
    ebay_page_length=int(len(ebay_page))
    for i in range (0,ebay_page_length):
        ebay_name = soup.select('.s-item__title')[i].getText().strip()
        ebay_name=ebay_name.upper()
        name=name.upper()
        if name in ebay_name:
            ebay_price = soup.select('.s-item__price')[i].getText().strip()
            ebay_price = ebay_price.replace("INR", "₹")
            return f"{ebay_name}\nPrice : {ebay_price}\n"
    else:
            ebay_price = 'Product Not Found'
            return ebay_price


def amazon(name=""):
        global amazon
        name1 = name.replace(" ", "-")
        name2 = name.replace(" ", "+")
        res = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}', headers=headers)

        soup = BeautifulSoup(res.text, 'html.parser')
        amazon_page = soup.select('.a-color-base.a-text-normal')
        amazon_page_length = int(len(amazon_page))
        for i in range(0, amazon_page_length):
            amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
            amazon_name=amazon_name.upper()
            name = name.upper()
            if name in amazon_name:
                amazon_price = soup.select('.a-price-whole')[i].getText().strip()
                return f"{amazon_name}\nPrice : {amazon_price}\n"
        else:
            amazon_price = 'Product Not Found'
            return amazon_price
    

def olx(name=""):
        global olx
        name1 = name.replace(" ", "-")
        res = requests.get(f'https://www.olx.in/items/q-{name1}?isSearchCall=true', headers=headers)

        soup = BeautifulSoup(res.text, 'html.parser')
        olx_page = soup.select('._2tW1I')
        olx_page_length = len(olx_page)
        for i in range(0,olx_page_length):
            olx_name = soup.select('._2tW1I')[i].getText().strip()
            name = name.upper()
            olx_name = olx_name.upper()
            if name in olx_name:
                olx_price = soup.select('._89yzn')[i].getText().strip()
                return f"{olx_name}\nprice : {olx_price}\n"
        else:
            olx_price = 'Product Not Found'
            return olx_price

def search():

    t1 = flipkart(product_name.get())
    box1.insert(1.0, t1)
    t2 = ebay(product_name.get())
    box2.insert(1.0, t2)
    t3 = amazon(product_name.get())
    box3.insert(1.0, t3)
    t4 = olx(product_name.get())
    box4.insert(1.0, t4)

window = Tk()
window.wm_title("Price comparison App")
window.geometry("900x500")
# bg = PhotoImage(file = "wp6899569-dark-mountain-wallpapers.jpg")
lable_one = Label(window, text="Enter Product Name :",font=("bold", 18), fg="green")
lable_one.place(relx=0.2, rely=0.1, anchor="center")

product_name = StringVar() 
product_name_entry = Entry(window, textvariable=product_name, width=50)
product_name_entry.place(relx=0.5, rely=0.1, anchor="center")

search_button = Button(window, text="Search", width=12, command=search)
search_button.place(relx=0.5, rely=0.18, anchor="center")


l1 = Label(window, text="Flipkart", font=("bold", 16), fg="green")
l2 = Label(window, text="Ebay", font=("bold", 16), fg="green")
l3 = Label(window, text="Amazon", font=("bold", 16), fg="green")
l4 = Label(window, text="Olx", font=("bold", 16), fg="green")

l1.place(relx=0.25, rely=0.25, anchor="center")
l2.place(relx=0.7, rely=0.25, anchor="center")
l3.place(relx=0.25, rely=0.548, anchor="center")
l4.place(relx=0.7, rely=0.548, anchor="center")

scrollbar = Scrollbar(window)
box1 = Text(window, height=7, width=50,yscrollcommand=scrollbar.set, bg="#9f9f9f", fg="black")

box2 = Text(window, height=7, width=50,yscrollcommand=scrollbar.set, bg="#9f9f9f", fg="black")

box3 = Text(window, height=7, width=50, yscrollcommand=scrollbar.set, bg="#9f9f9f", fg="black")

box4 = Text(window, height=7, width=50,yscrollcommand=scrollbar.set, bg="#9f9f9f", fg="black")
box1.place(relx=0.25, rely=0.4, anchor="center")
box2.place(relx=0.72, rely=0.4, anchor="center")
box3.place(relx=0.25, rely=0.7, anchor="center")
box4.place(relx=0.72, rely=0.7, anchor="center")

window.mainloop()