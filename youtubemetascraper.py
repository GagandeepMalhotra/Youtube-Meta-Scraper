import tkinter as tk
from tkinter import ttk, messagebox
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs

session = HTMLSession()

def get_video_metadata(url):
    response = session.get(url)
    #Execute Javascript
    response.html.render(sleep=10)

    soup = bs(response.html.html, "html.parser")

    video_meta = {}

    title_element = soup.select_one(".title.style-scope.ytd-video-primary-info-renderer")
    video_meta["title"] = title_element.text.strip()

    #Video Description
    description_element = soup.select_one("#description")
    if description_element:
        video_meta["description"] = description_element.text.strip()
    else:
        video_meta["description"] = ""

    #Video Tags
    video_meta["tags"] = ', '.join([meta.attrs.get("content") for meta in soup.find_all("meta", {"property": "og:video:tag"})])

    return video_meta

def get_video_metadata_gui():
    url = entry.get()
    if not url.startswith("https://www.youtube.com/watch?v="):
        messagebox.showerror("Error", "Invalid YouTube link!")
        return

    try:
        video_meta = get_video_metadata(url)
        messagebox.showinfo("Video Metadata", str(video_meta))
    except Exception as e:
        messagebox.showerror("Error", str(e))

#Create Tkinter window
window = tk.Tk()
window.title("YouTube Video Metadata")

#Set window size and position
window_width = 800
window_height = int(window_width * 3 / 4)  #4:3 ratio
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

#Set window background color
window.configure(bg="#ECECEC")

#Create a frame to hold the GUI elements
frame = tk.Frame(window, bg="#ECECEC")
frame.pack(expand=True)

#Create a label and entry field for the YouTube link
label = tk.Label(frame, text="Enter YouTube Link:", font=("Arial", 14), bg="#ECECEC", fg="#333333")
label.pack(pady=20)

#Create a themed input box
style = ttk.Style()
style.configure("Custom.TEntry", padding=10, relief="solid", background="#FFFFFF", font=("Arial", 12))
entry = ttk.Entry(frame, width=50, style="Custom.TEntry")
entry.pack()

#Create a button to get the video metadata
button = tk.Button(frame, text="Get Metadata", command=get_video_metadata_gui, font=("Arial", 12), bg="#333333", fg="#ECECEC")
button.pack(pady=20)

#Center the frame vertically within the window
frame.update_idletasks()
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

#Start the Tkinter event loop
window.mainloop()
