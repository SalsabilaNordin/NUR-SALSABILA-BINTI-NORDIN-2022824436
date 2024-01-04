import tkinter as tk
from tkinter import ttk 
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="make_up_booking"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

def INSERT_DATA():
 
    name = name_entry.get()
    date = date_entry.get()
    
    # Perform calculations or data processing here
    package = package_combobox.get()
    hour = int(hours_entry.get())

    prices = {
    "Package A": 40,
    "Package B": 80,
    "Package C": 100,
    }  

    total_price = (prices[package] * hour)

    result_label = tk.Label(price_for_booking, text=f"RM{total_price}")
    result_label.grid(row=8, column=1)

    print("Revenue data inserted into the 'price' table.")
    print("----------------------------------------------")
    print("Name:", name)
    print("Date:", date)
    print("hours:", hour)
    print("Package:", package)
    print("Total Revenue:", "RM", total_price)
    print("------------------------------------------")

    sql=("INSERT INTO booking (label_name, label_package, booking_date, label_hours) VALUES(%s, %s, %s, %s)")
    val=(name, package, date, hour)
    mycursor.execute(sql, val)
    mydb.commit()
         
#TkinterGUI
root = tk.Tk()
root.title("MAKEUP BOOKING")
root.geometry("700x500")
root.configure(bg="#030303")

label_name = tk.Label(root, text="MAKEUP BOOKING", font=("abadi", 20),bg="#F1948A", fg="#85C1E9", )
label_name.pack(padx=10, pady=10)

frame = tk.Frame(root)
frame.pack()

text_prices = tk.LabelFrame(frame, bg="#F1948A", fg="#ECF0F1", font=('abadi', 18))
text_prices.grid(row=0, column=0)

prices_text = tk.Text(text_prices, height=8, width=60, bg="#F1948A", font=("abadi"))
prices_text.pack(padx=10, pady=10)
prices_text.insert(tk.END, "Package & Prices:\n\n" )
prices_text.insert(tk.END, "Package A: makeup artist A Price: RM40\n\n")
prices_text.insert(tk.END, "Package B: makeup artist B Price: RM80\n\n")
prices_text.insert(tk.END, "Package C: makeup artist C Price: RM100\n\n")

price_for_booking = tk.LabelFrame(frame, text="Booking Information", bg="#F1948A", fg="#ECF0F1", font=('abadi', 18,))
price_for_booking.grid(row=1, column=0)

label_name = tk.Label(price_for_booking, text="Name :", bg="#F1948A", fg="#ECF0F1", font=("abadi", 18))
label_name.grid(row=0, column=0)
name_entry = tk.Entry(price_for_booking)
name_entry.grid(row=0, column=1)

booking_date = tk.Label(price_for_booking, text="Date:",font =("abadi", 18), bg="#F1948A", fg="#ECF0F1")
booking_date.grid(row=1, column=0)
date_entry = tk.Entry(price_for_booking) 
date_entry.grid(row=1, column=1)
date_entry.insert(0, "dd/mm/yyyy")

label_package= tk.Label(price_for_booking, text="package", bg="#F1948A", fg="#ECF0F1", font=("abadi", 18))
label_package.grid(row=2, column=0)
package_combobox = ttk.Combobox(price_for_booking, values=["Package A",
                                                          "Package B",
                                                          "Package C"])
package_combobox.grid(row=2, column=1)

label_hours = tk.Label(price_for_booking, text="hours", bg="#F1948A", fg="#ECF0F1", font=("abadi", 18))
label_hours.grid(row=3, column=0)
hours_entry = ttk.Combobox(price_for_booking,  values=["1", "2", "3", "4"])
hours_entry.grid(row=3, column=1)

#Button
total_price_button = tk.Button(price_for_booking, text="Total Price", command=INSERT_DATA, bg="#030303", fg="#ECF0F1", font=('abadi', 14,))
total_price_button.grid(row=8, column=3)
root.mainloop()