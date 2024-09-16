import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw
import instaloader

def download_reel():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    try:
        L = instaloader.Instaloader()
        # Extract shortcode from URL
        shortcode = url.split('/')[-2]
        # Download the reel
        L.download_post(instaloader.Post.from_shortcode(L.context, shortcode), target='reels')
        messagebox.showinfo("Success", "Download complete!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def create_rounded_button(text, command, width=200, height=50, radius=15):
    # Create a blank image with white background
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    # Draw a rounded rectangle
    draw.rounded_rectangle([(0, 0), (width, height)], radius=radius, fill="#d4afb9", outline="#d4afb9")

    # Convert image to Tkinter-compatible format
    tk_image = ImageTk.PhotoImage(image)

    # Create a button with the image
    button = tk.Button(root, text=text, image=tk_image, compound="center", command=command, bg="#d4afb9", relief="flat", bd=0)
    button.image = tk_image  # Keep a reference to avoid garbage collection
    return button

# Create the main window
root = tk.Tk()
root.title("Instagram Reel Downloader")
root.geometry("400x200")
root.configure(bg="#d1cfe2")

# Style configuration
style = ttk.Style()
style.configure("TLabel", background="#d1cfe2", foreground="black", font=("Arial", 12))

# Create and place the header
header = tk.Label(root, text="Instagram Reel Downloader", font=("Arial", 16, "bold"), bg="#d1cfe2", fg="#000000", pady=10)
header.pack(fill="x")

# Create and place the URL entry
url_frame = tk.Frame(root, bg="#d1cfe2")
url_frame.pack(pady=20)

url_label = ttk.Label(url_frame, text="Reel URL:")
url_label.pack(side="left", padx=10)

url_entry = ttk.Entry(url_frame, width=50)
url_entry.pack(side="left")

# Create and place the download button
download_button = create_rounded_button("Download", download_reel, width=150, height=40, radius=20)
download_button.pack(pady=20)

# Run the application
root.mainloop()
