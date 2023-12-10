import tkinter as tk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from datetime import datetime

window = tk.Tk()
window.geometry("600x600")
window.title("Hello Admin...")
window.configure(bg="lightgreen")

l1 = tk.Label(window, text="Hello Welcome Admin", font=("arial black", 20), anchor="center", fg='Black', bg='lightgreen')
l1.pack()
l2 = tk.Label(window, text="WELCOME TO VEG MENU", font=("geneva", 12), fg='Black', bg='lightgreen')
l2.pack()

menu = {
    'Veggie Burger': 150.00,
    'Margherita Pizza': 200.00,
    'Vegetable Stir-Fry': 120.00,
    'Spinach and Feta Salad': 180.00,
    'Dal Tadka': 100.00,
    'Aloo Gobi': 130.00,
    'Paneer Tikka': 160.00,
    'Veg Biryani': 220.00,
    'Palak Paneer': 190.00,
    'Chole Bhature': 150.00
}
window.pdf_counter = 1

def order():
    global pdf_counter 
    total_cost = 0
    bill = "Bill:\n"
    for item, price in menu.items():
        qty = int(quantity_entries[item].get())
        if qty > 0:
            total_cost += price * qty
            bill += f"{item}: {qty} x Rs{price:.2f} = Rs{qty * price:.2f}\n"

    if total_cost == 0:
        messagebox.showinfo("Order", "Please select at least one item")
        return
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    bill += f"\nTotal: Rs{total_cost:.2f}"
    bill += f"\nDate and Time: {current_datetime}"
    generate_pdf(bill, f"veg_bill_{window.pdf_counter}.pdf")
    window.pdf_counter += 1

    messagebox.showinfo("Bill", bill)

def generate_pdf(bill_text, filename):
    c = canvas.Canvas(filename)
    width, height = c._pagesize
    c.setFont("Helvetica", 12)
    lines = bill_text.split('\n')
    y_position = height - 100
    c.drawString(240, 800, "Veg Restaurant Bill")
    for line in lines:
        c.drawCentredString(width / 2, y_position, line)
        y_position -= 15
    c.save()

checkboxes = {}
quantity_entries = {}
for item, price in menu.items():
    var = tk.IntVar(value=0)
    checkboxes[item] = var
    tk.Checkbutton(window, text=f"{item} (Rs{price:.2f}/-)", variable=var, bg="lightgreen", fg="black").pack()

    quantity_var = tk.StringVar(value="0")
    quantity_entry = tk.Spinbox(window, from_=0, to=10, textvariable=quantity_var, width=5).pack()
    quantity_entries[item] = quantity_var
    

l3 = tk.Label(window, text="-CLICK ORDER HERE BUTTON TO CONFIRM ORDER", font=("herald", 12), fg='Black', bg='lightgreen')
l3.pack()
b1 = tk.Button(window, text="Order Here", command=order, height=4, width=15)
b1.pack(side=tk.BOTTOM)

window.mainloop()
