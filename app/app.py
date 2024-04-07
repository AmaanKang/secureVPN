import tkinter as tk
from tkinter import *
from tkinter import ttk
import subprocess
import os

# Create the main window
root = tk.Tk()
root.title("Secure VPN")

# Use a nice frame
main_frame = ttk.Frame(root,padding="10")
main_frame.grid(row=0,column=0,sticky=(W,E,N,S))

# Use a nicer looking theme
style = ttk.Style()
style.theme_use('clam')

# Create a text area to display the status of the VPN
status_text = tk.StringVar()
status_label = ttk.Label(main_frame,textvariable=status_text,font=("Helvetica", 16))
status_label.grid(row=0, column=0, padx=10, pady=10)

# Create a drop-down menu to select a server
server_var = tk.StringVar()
server_dropdown = ttk.Combobox(main_frame, textvariable=server_var)
server_dropdown['values'] = ("server", "client")
server_dropdown.grid(row=1, column=0, padx=10, pady=10)

# Create an entry field to enter custom options
options_var = tk.StringVar()
options_entry = ttk.Entry(main_frame,textvariable=options_var)
options_entry.grid(row=1, column=1, padx=10, pady=10)

# Create a text area to display the status updates
status_update_text = tk.StringVar()
status_update_label = ttk.Label(main_frame,textvariable=status_update_text,font=("Helvetica", 12))
status_update_label.grid(row=3, column=1, padx=10, pady=10)


def start_vpn():
    # Start the VPN
    try:
        os.chdir("C:\\Program Files\\OpenVPN\\config")
        server = server_var.get()
        options = options_var.get().split()
        subprocess.Popen(["openvpn","--config",f"{server}.ovpn"] + options)
        status_text.set(f"{server} VPN started")
    except Exception as e:
        print(f"VPN Start Exception: {e}")
    

def stop_vpn():
    # Stop the VPN
    try:
        subprocess.Popen(["taskkill","/IM","openvpn.exe","/F"])
        status_text.set("VPN stopped")
    except Exception as e:
        print(f"VPN Stop Exception: {e}")

def check_server_status():
    # Check the status of the selected server
    try:
        server = server_var.get()
        if server == "server":
            server = "10.8.0.1"
        elif server == "client":
            server = "10.8.0.2"
        status = subprocess.check_output(["ping","-n","1",f"{server}"])
        status_update_text.set(status)
    except Exception as e:
        status_update_text.set(f"Server Status Exception: {e}")
    
# Create the start button
start_button = ttk.Button(main_frame,text="Start VPN",command=start_vpn)
start_button.grid(row=2, column=0, padx=10, pady=10)

# Create the stop button
stop_button = ttk.Button(main_frame,text="Stop VPN",command=stop_vpn)
stop_button.grid(row=2, column=1, padx=10, pady=10)

server_status_button = ttk.Button(main_frame,text="Check server status",command=check_server_status)
server_status_button.grid(row=2, column=2, padx=10, pady=10)

# Now the app will run and listen for any events
root.mainloop()






