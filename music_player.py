import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image
import pygame
import os

main=ctk.CTk()
main.geometry("400x500")
main.resizable(False,False)
main.title('Music Player')

songs=[]
current_song=""
paused=False


def load_music():
    global current_song
    main.directory= filedialog.askdirectory()
    for song in os.listdir(main.directory):
        name, ext=os.path.splitext(song)
        if ext=='.mp3':
            songs.append(song)

    for song in songs:
        songlist.insert("end", song)
    songlist.selection_set(0)
    current_song=songs[songlist.curselection()[0]]
    update_current_song_label() 


def play_song():
    global current_song, paused 
    if current_song:
        try:
            if not paused:
                pygame.mixer.music.load(os.path.join(main.directory, current_song))
                pygame.mixer.music.play()
            else:
                pygame.mixer.music.unpause()
                paused = False
                update_current_song_label()
        except pygame.error as e:
            print("Error playing song:", e)

def pause_song():
    global paused
    pygame.mixer.music.pause()
    paused=True
    update_current_song_label()
def next_song():
    global current_song, paused
    try:
        songlist.selection_clear(0,END)
        songlist.selection_set(songs.index(current_song)+1)
        current_song=songs[songlist.curselection()[0]]
        play_song()
        update_current_song_label()
    except:
        pass
def prev_song():
    global current_song,paused
    try:
        songlist.selection_clear(0,END)
        index = max(songs.index(current_song) - 1, 0)
        songlist.selection_set(index)
        current_song=songs[songlist.curselection()[0]]
        play_song()
        update_current_song_label() 
    except:
        pass

def update_current_song_label():
    global current_song
    current_song_showing.config(text=current_song)

menubar=Menu(main, bg='#2b3137', fg='white')
main.config(menu=menubar)
organize_menu= Menu(menubar, tearoff=False)
organize_menu.add_command(label='Select Folder', command=load_music)
menubar.add_cascade(label='Select', menu=organize_menu)

background=ctk.CTkFrame(main, fg_color="#2b3137", corner_radius=0)

music_image=Image.open('/home/zestyzoom/Python/music-player/cloud_1562821.png')
ctk_image = ctk.CTkImage(light_image=music_image, dark_image=music_image, size=(250, 250))

label_with_image = ctk.CTkLabel(background, image=ctk_image, text="")
label_with_image.pack(pady=20)

background.pack(fill='both',expand=True)

#pygame
pygame.mixer.init()

songlist= Listbox(background,bg="#2b3137",fg='white', width =40 ,height=5,bd=0,highlightthickness=0)
songlist.pack(pady=1)

play_button_image=PhotoImage(file='/home/zestyzoom/Python/music-player/play.png' )

pause_button_image=PhotoImage(file='/home/zestyzoom/Python/music-player/pause.png')

next_botton_image=PhotoImage(file='/home/zestyzoom/Python/music-player/next.png')

prev_button_image=PhotoImage(file='/home/zestyzoom/Python/music-player/prev.png')

control_frame=tk.Frame(background, bg='#2b3137', height=60, width=250)
control_frame.pack()

play_button=tk.Button(control_frame,image=play_button_image, borderwidth=0, bg='#2b3137', bd=0 ,highlightthickness=0, command=play_song)
pause_button=tk.Button(control_frame,image=pause_button_image, borderwidth=0, bg='#2b3137', bd=0,highlightthickness=0,command=pause_song)
next_button=tk.Button(control_frame,image=next_botton_image, borderwidth=0, bg='#2b3137', bd=0,highlightthickness=0, command=next_song)
prev_button=tk.Button(control_frame,image=prev_button_image, borderwidth=0, bg='#2b3137', bd=0,highlightthickness=0, command= prev_song)

play_button.grid(row=0,column=1,pady=6,padx=7)
pause_button.grid(row=0,column=2,pady=6,padx=7)
next_button.grid(row=0,column=3,pady=6,padx=7)
prev_button.grid(row=0,column=0,pady=6,padx=7)

current_song_showing=tk.Label(background, text=current_song,bg="#2b3137", fg="white")
current_song_showing.pack()

main.mainloop()