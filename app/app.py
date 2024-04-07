import tkinter as tk
import subprocess
import os

# Create the main window
root = tk.Tk()

# Create a text area to display the status of the VPN
status_text = tk.StringVar()
status_label = tk.Label(root,textvariable=status_text)
status_label.pack()

# Create a drop-down menu to select a server
server_var = tk.StringVar()
server_dropdown = tk.OptionMenu(root,server_var,"server","client")
server_dropdown.pack()

# Create an entry field to enter custom options
options_var = tk.StringVar()
options_entry = tk.Entry(root,textvariable=options_var)
options_entry.pack()

def start_vpn():
    # Start the VPN
    try:
        os.chdir("C:\\Program Files\\OpenVPN\\config")
        server = server_var.get()
        options = options_var.get().split()
        subprocess.Popen(["openvpn","--config",f"{server}.ovpn"] + options)
        status_text.set("VPN started")
    except Exception as e:
        print(f"VPN Start Exception: {e}")
    

def stop_vpn():
    # Stop the VPN
    try:
        subprocess.Popen(["taskkill","/IM","openvpn.exe","/F"])
        status_text.set("VPN stopped")
    except Exception as e:
        print(f"VPN Stop Exception: {e}")
    
# Create the start button
start_button = tk.Button(root,text="Start VPN",command=start_vpn)
start_button.pack()

# Create the stop button
stop_button = tk.Button(root,text="Stop VPN",command=stop_vpn)
stop_button.pack()

# Now the app will run and listen for any events
root.mainloop()






