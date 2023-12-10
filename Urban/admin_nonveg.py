import tkinter as tk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from datetime import datetime

window = tk.Tk()
window.geometry("600x600")
window.title("Hello Admin...")
window.configure(bg="brown1")

l1 = tk.Label(window, text="Hello Welcome Admin", font=("arial black", 20), anchor="center", fg='Black', bg='brown1').pack()
l2 = tk.Label(window, text="WELCOME TO NON-VEG MENU", font=("geneva", 12), fg='Black', bg='brown1').pack()

menu = {
    "Chickenbiryani": 250.00,
    "Grilledsalmon": 350.00,
    "Beefsteak": 300.00,
    "Butterchicken": 280.00,
    "Prawncurry": 320.00,
    "Lambkebabs": 280.00,
    "Fishtacos": 200.00,
    "Chickenalfredopasta": 230.00,
    "Sizzlinggarlicshrimp": 300.00,
    "Pepperonipizza": 220.00,
}

window.pdf_counter = 1

def order():
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

    bill += f"\nTotal: Rs{total_cost:.2f}/-"
    bill += f"\nDate and Time: {current_datetime}"

    generate_pdf(bill, f"nonveg_bill_{window.pdf_counter}.pdf")

    window.pdf_counter += 1

    messagebox.showinfo("Bill", bill)

def generate_pdf(bill_text, filename):
    c = canvas.Canvas(filename)
    width, height = c._pagesize
    c.setFont("Helvetica", 12)
    lines = bill_text.split('\n')
    y_position = height - 100
    c.drawString(240, 800, "Non-Veg Restaurant Bill")
    for line in lines:
        c.drawCentredString(width / 2, y_position, line)
        y_position -= 15
    c.save()

checkboxes = {}
quantity_entries = {}
for item, price in menu.items():
    var = tk.IntVar(value=0)
    checkboxes[item] = var
    tk.Checkbutton(window, text=f"{item} (Rs{price:.2f}/-)", variable=var, bg='brown1').pack()

    quantity_var = tk.StringVar(value="0")
    quantity_entry = tk.Spinbox(window, from_=0, to=10, textvariable=quantity_var, width=5).pack()
    quantity_entries[item] = quantity_var
    

l3 = tk.Label(window, text="-CLICK ORDER HERE BUTTON TO CONFIRM ORDER", font=("herald", 12), fg='Black', bg='brown1').pack()
b1 = tk.Button(window, text="Order Here", command=order, height=4, width=15).pack(side=tk.BOTTOM)

window.mainloop()
