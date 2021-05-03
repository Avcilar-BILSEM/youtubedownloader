from pytube import YouTube
from pytube import Playlist
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import HORIZONTAL
import time


class ytd:
    def __init__ (self):
        self.p = 0
        self.master = tk.Tk()
        self.master.title("Youtube Video ve Liste İndirme")
        tk.Label(self.master, text="URL Girin").grid(row=0)
        tk.Label(self.master, text="Klasör Girin").grid(row=1)
        self.e1 = tk.Entry(self.master)
        self.e2 = tk.Entry(self.master)
        self.e2.insert(10, "indir")
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)

        self.e1.grid(row=0, column=1)

        tk.Button(self.master,
                  text='İndir',
                  command=self.start).grid(row=3,
                                           column=0,
                                           sticky=tk.W,
                                           pady=4)
        self.plabel = tk.Label(self.master, text="URL Girin").grid(row=4)
        self.progress = Progressbar(self.master, variable=self.p, orient=HORIZONTAL, length=100, mode='indeterminate')
        self.progress.grid(row=4)
        tk.Label(self.master, text="Avcılar BİLSEM").grid(row=5)
        self.progress.start()
        self.master.protocol("WM_DELETE_WINDOW", self.ask_quit)
        self.master.mainloop()
        exit()

    def ask_quit (self):
        if messagebox.askokcancel("Çık", "Programdan çıkmak istiyor musunuz? *sniff*"):
            self.master.destroy()

    def start (self):
        link = self.e1.get()
        klasor = self.e2.get()
        if link.find('playlist') != -1:
            self.listeindir(link, klasor)
        else:
            self.getInfo(link)
            self.printInfo()
            self.streams()
            self.indir(klasor=klasor)
        messagebox.showinfo("İşlem Tamamlandı", "Tüm dosyalar indirildi!")

    def getInfo (self, url):
        try:
            self.yt = YouTube(url)
            return self.yt
        except:
            raise Exception("Videoyu Bulamadım!")

    def printInfo (self):
        # Title of video
        print("Title: ", self.yt.title)
        # Number of views of video
        print("Number of views: ", self.yt.views)
        # Length of the video
        print("Length of video: ", self.yt.length, "seconds")
        # Description of video
        print("Description: ", self.yt.description)
        # Rating
        print("Ratings: ", self.yt.rating)

    def streams (self):
        liste = self.yt.streams.order_by('resolution').desc()
        return liste

    def indir (self, resolution="", klasor="indir"):

        print(self.yt.title + " indiriliyor")
        self.yt.streams.get_highest_resolution().download(klasor)
        print("İndirildi")

    def listeindir(self, url, klasor):
        playlist = Playlist(url)
        adet = len(playlist)
        simdiki = 1
        print("{} video bulunuyor".format (adet))

        for video_url in playlist.video_urls:
            self.master.update_idletasks ()
            self.p = simdiki / adet
            self.progress.grab_status ()
            time.sleep (0.5)
            print("İndirilen:{}/{} indiriliyor".format (simdiki, adet))
            simdiki += 1
            self.getInfo(video_url)
            self.printInfo()
            self.streams()
            self.indir(klasor)
