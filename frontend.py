

from tkinter import Tk, Frame, Label, Entry, Button, Toplevel
from backend import Smartphone, PhotosApp, YourTubeApp

phone = Smartphone(512)
photos_app = PhotosApp(phone)
tube_app = YourTubeApp(phone)

#functions in GUI
def update_labels():
    battery_label.config(text=f"Battery: {phone.battery}%")
    saver_label.config(text=f"Battery Saver Mode: {'Enabled' if phone.battery_saver_mode else 'Disabled'}")
    storage_label.config(text=f"Storage Left: {phone.storage_left():.2f}GB")
    photos_label.config(text=f"Number of Photos: {photos_app.num_photos}")
    videos_label.config(text=f"Number of Videos: {len(tube_app.videos)}")

def show_error(msg):
    bottom_error.config(text=msg)

def clear_error():
    bottom_error.config(text="")

    
def take_photo():
    clear_error()
    try: photos_app.take_photo()
    except ValueError as e: show_error(str(e))
    update_labels()

def delete_photo():
    clear_error()
    try: photos_app.delete_photo()
    except ValueError as e: show_error(str(e))
    update_labels()

def save_video():
    clear_error()
    try:
        duration = int(duration_entry.get())
        tube_app.save_video(duration)
        update_videos_popup()
    except ValueError as e: show_error(str(e))
    update_labels()

def delete_video():
    clear_error()
    try:
        index = int(index_entry.get())
        tube_app.delete_video(index)
        update_videos_popup()
    except (ValueError, IndexError) as e: show_error(str(e))
    update_labels()

def toggle_saver():
    clear_error()
    if phone.battery_saver_mode:
        phone.battery_saver_mode = False
    else:
        phone.battery_saver_mode = True
    update_labels()

def charge_battery():
    clear_error()
    phone.charge_battery()
    update_labels()

def update_videos_popup():
    global video_popup
    try:
        video_popup.destroy()
    except:
        pass
    video_popup = Toplevel(window)
    video_popup.title("Saved Videos")
    video_popup.geometry("250x200")
    Label(video_popup, text="Saved Videos:").pack(anchor="w")
    vids = [f"{m:02}:{s:02}" for m, s in (divmod(v, 60) for v in tube_app.videos)]
    if vids:
        for v in vids: Label(video_popup, text=v).pack(anchor="w")
    else:
        Label(video_popup, text="No videos saved").pack(anchor="w")

window = Tk()
window.title("BnL Smartphone")
window.geometry("326x383")

#stands for smartphone frame
sf = Frame(window); sf.pack(anchor="w")
Label(sf, text="BnL Smartphone").pack(anchor="w")
Label(sf, text=f"Storage Capacity: {phone.storage_capacity}GB").pack(anchor="w")
battery_label = Label(sf, text=""); battery_label.pack(anchor="w")
saver_label = Label(sf, text=""); saver_label.pack(anchor="w")
storage_label = Label(sf, text=""); storage_label.pack(anchor="w")
#stands for button frame
bf = Frame(sf); bf.pack(anchor="w")
Button(bf, text="Toggle Battery Saver", width=16, command=toggle_saver).pack(side="left")
Button(bf, text="Charge Battery", width=12, command=charge_battery).pack(side="left")

#stands for photos frame
pf = Frame(window); pf.pack(anchor="w")
Label(pf, text="Photos App").pack(anchor="w")
photos_label = Label(pf, text=""); photos_label.pack(anchor="w")
photos_storage_label = Label(pf, text="Storage Used: 0GB")
photos_storage_label.pack(anchor="w")
#stands for photos buttons
pb = Frame(pf); pb.pack(anchor="w")
Button(pb, text="Take Photo", width=15, command=take_photo).pack(side="left")
Button(pb, text="Delete Photo", width=15, command=delete_photo).pack(side="left")

#stands for yourtube frame
yf = Frame(window); yf.pack(anchor="w")
Label(yf, text="YourTube App").pack(anchor="w")
videos_label = Label(yf, text=""); videos_label.pack(anchor="w")
youtube_storage_label = Label(yf, text="Storage Used: 0GB")
youtube_storage_label.pack(anchor="w")
#stand for duration
dur_row = Frame(yf); dur_row.pack(anchor="w")
duration_entry = Entry(dur_row, width=25); duration_entry.pack(side="left")
Button(dur_row, text="Save Video", width=12, command=save_video).pack(side="left")
#stands for index
idx_row = Frame(yf); idx_row.pack(anchor="w")
index_entry = Entry(idx_row, width=25); index_entry.pack(side="left")
Button(idx_row, text="Delete Video", width=12, command=delete_video).pack(side="left")


bottom_error = Label(window, text=""); bottom_error.pack()

update_labels()
window.mainloop()

