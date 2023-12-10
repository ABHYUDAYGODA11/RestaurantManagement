import tkinter as tk
import subprocess

def run_file1():
    run_file("C:\\Users\\MR SLAYER\\Desktop\\Urban\\admin_veg.py")

def run_file2():
    run_file("C:\\Users\\MR SLAYER\\Desktop\\Urban\\admin_nonveg.py")

def run_file(file_path):
    subprocess.Popen(['python', file_path], shell=True)

root = tk.Tk()
root.title("Urban Choak")
root.geometry("600x600")
root.configure(bg='purple')
l1=tk.Label(root,text="Welcome Admin",font=("arial black",20),anchor="center",fg='lightblue',bg='purple').pack()
l2=tk.Label(root,text="**TO ORDER VEG FOOD CLICK 'Veg Order' BUTTON**",font=("herald",12),fg='cornsilk2',bg='purple').pack()
l3=tk.Label(root,text="**TO ORDER NON-VEG FOOD CLICK 'Non-Veg Order' BUTTON**",font=("herald",12),fg='cornsilk2',bg='purple').pack()

button1 = tk.Button(root, text="Veg Order", command=run_file1,font=("courier"),fg="white",bg="blue").pack(side=tk.LEFT)
button2 = tk.Button(root, text="Non-Veg Order", command=run_file2,font=("courier"),fg="white",bg="blue").pack(side=tk.RIGHT)
root.mainloop()
