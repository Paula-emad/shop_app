import requests
from bs4 import BeautifulSoup
import webbrowser
from tkinter import Tk, Label, Entry, Button, messagebox, ttk, Frame, StringVar

def get_product_search_link(search_query, market):
    if market == "Noon Saudi":
        return f"https://www.noon.com/saudi-en/search/?q={search_query}"
    elif market == "Noon Egypt":
        return f"https://www.noon.com/egypt-en/search/?q={search_query}"
    elif market == "Noon Emirates":
        return f"https://www.noon.com/uae-en/search/?q={search_query}"
    elif market == "Amazon Egypt":
        return f"https://www.amazon.eg/s?k={search_query}"
    elif market == "Amazon America":
        return f"https://www.amazon.com/s?k={search_query}"
    elif market == "Jumia Egypt":
        return f"https://www.jumia.com.eg/catalog/?q={search_query}"
    elif market == "Ali Baba":
        return f"https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={search_query}"

    return None

def search_products():
    search_query = entry.get()
    market = market_list.get()

    if not search_query:
        messagebox.showinfo("Error", "Search query not found.")
        return

    product_search_link = get_product_search_link(search_query, market)
    if product_search_link:
        webbrowser.open(product_search_link)
    else:
        messagebox.showinfo("Error", "Product search link not found.")

# Create the GUI window
window = Tk()
window.title("Product Search")
window.geometry("400x250")  # Set a larger size for the window

# Add a label and an entry field
label = Label(window, text="Enter product name or SKU code:")
label.pack()
entry = Entry(window, width=40)  # Adjust the width of the entry field
entry.pack()

# Create a frame for the market selection
market_frame = Frame(window, width=400, height=50)  # Adjust the size of the frame
market_frame.pack(pady=10)

# Add a label for market selection
market_label = Label(market_frame, text="Select Market:")
market_label.pack(side="left")

# Create a list of markets
markets = ["Noon Egypt", "Noon Saudi", "Noon Emirates", "Amazon Egypt", "Amazon America", "Jumia Egypt", "Ali Baba"]

# Create a drop-down menu for market selection
market_list = ttk.Combobox(market_frame, values=markets, width=15)
market_list.pack(side="left")
market_list.set("Noon Egypt")  # Set the default market to Noon Egypt

# Create a frame for the button
button_frame = Frame(window, width=400, height=50)  # Adjust the size of the frame
button_frame.pack(pady=10)

# Add a button to search for products
search_button = Button(button_frame, text="Search Products", command=search_products)
search_button.pack(pady=5)

# Start the GUI main loop
window.mainloop()


