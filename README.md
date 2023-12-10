#  "HOTEL MANAGEMENT SYSTEM" 
In this project i have made total 4 files which is descirbed in detail below<br>
# The first 3 section contains information about admin interface
# 1 : The Non_veg Menu file:

This Python script uses the Tkinter library to create a simple GUI for a non-vegetarian restaurant order management system. The application allows the admin to select items from the non-veg menu, specify quantities, and generate a detailed bill in PDF format.

## Features:
- User-friendly GUI with a welcome message and a list of non-veg menu items.
- Checkboxes for item selection and Spinboxes for quantity input.
- "Order Here" button to confirm the order and generate a bill.
- Each order generates a PDF bill with itemized details, total cost, and timestamp.

## Menu:
- Chicken Biryani
- Grilled Salmon
- Beef Steak
- Butter Chicken
- Prawn Curry
- Lamb Kebabs
- Fish Tacos
- Chicken Alfredo Pasta
- Sizzling Garlic Shrimp
- Pepperoni Pizza

## Usage:
1. Check the items you want to order.
2. Enter the quantity for each selected item.
3. Click the "Order Here" button to confirm the order.
4. A PDF bill will be generated with detailed information.

Feel free to customize the menu, add more items, or modify the code as needed. Enjoy managing non-veg restaurant orders with this simple application!
# 2 : The Veg Menu File

This Python script utilizes the Tkinter library to create a user-friendly GUI for managing orders in a vegetarian restaurant. Admins can select items from the veg menu, specify quantities, and generate a detailed bill in PDF format.

## Features:
- Welcoming GUI with a greeting message and a list of vegetarian menu items.
- Checkboxes for item selection and Spinboxes for quantity input.
- "Order Here" button to confirm the order and generate a bill.
- Each order results in a PDF bill with itemized details, total cost, and timestamp.

## Veg Menu:
- Veggie Burger
- Margherita Pizza
- Vegetable Stir-Fry
- Spinach and Feta Salad
- Dal Tadka
- Aloo Gobi
- Paneer Tikka
- Veg Biryani
- Palak Paneer
- Chole Bhature

## Usage:
1. Check the items you want to order.
2. Enter the quantity for each selected item.
3. Click the "Order Here" button to confirm the order.
4. A PDF bill will be generated with detailed information.

Feel free to customize the menu, add more items, or modify the code according to your preferences. Enjoy managing vegetarian restaurant orders with this simple application!
# 3 : The Admin Interface

This Python script creates a graphical user interface for an admin to initiate order management systems for both vegetarian and non-vegetarian menus in the restaurant application. The script utilizes Tkinter for GUI development and subprocess to run external Python scripts.

## Features:
- Admin-friendly GUI with welcome messages and instructions.
- Buttons to trigger order management for both Veg and Non-Veg menus.

## Usage:
1. Click the "Veg Order" button to initiate the order management system for vegetarian food.
2. Click the "Non-Veg Order" button to initiate the order management system for non-vegetarian food.

### Note:
- Ensure that Python is installed on the system.
- The paths specified in the `run_file1` and `run_file2` functions should point to the respective Python scripts (`admin_veg.py` and `admin_nonveg.py`).

Feel free to customize the code, add more features, or modify the GUI according to your requirements. Enjoy managing orders efficiently with the Urban Choak Admin Interface! <br>
# This Last section contain information about user interface.
# 4 : The User Interface

This Python script creates a graphical user interface using Tkinter to allow users to generate QR codes for accessing both vegetarian and non-vegetarian menus at restaurant. The script utilizes the qrcode library for QR code generation and Tkinter for GUI development.

## Features:
- Welcome message and instructions displayed on the main window.
- Buttons to generate QR codes for accessing the Veg and Non-Veg menus.
- Separate windows displaying QR codes for Veg and Non-Veg menus.

## Usage:
1. Click the "Veg Menu" button to generate a QR code for accessing the vegetarian menu.
2. Click the "Non-Veg Menu" button to generate a QR code for accessing the non-vegetarian menu.

### Note:
- Make sure to replace the image paths in the `image_path` variables with the correct paths to your QR code images.

Feel free to customize the code, add more features, or modify the GUI according to your preferences. Enjoy generating QR codes for Urban Chowk menus with this simple application!
