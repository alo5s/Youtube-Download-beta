#import customtkinter
from customtkinter import CTk,CTkButton,CTkImage,CTkLabel,CTkEntry,set_appearance_mode
from pytube import YouTube
from PIL import Image

set_appearance_mode("dark") 
class App(CTk):
    def __init__(self):
        super().__init__()  
        self.geometry(f"{400}x{200}")
        self.resizable(0,0)
        self.iconbitmap("documentation_images/t.ico")
        self.deiconify()
        
        

        self.btn = CTkButton(self,  text="Dowlade", command=self.url_dowlader)
        self.btn.place(x=180, y=90)
        
        self.img_youtube = CTkImage(Image.open("documentation_images/YouTube.png"),size=(120, 120))

        self.label_img_youtube=CTkLabel(self, image=self.img_youtube, text=None)
        self.label_img_youtube.place(x=45 , y=20)

        self.url_entry=CTkEntry(self ,placeholder_text="URl")
        self.url_entry.place(x=180, y=55 )

    def url_dowlader(self):
        text = (self.url_entry.get())
        yt = YouTube(text)
        yt.streams.filter(file_extension='mp4', res="720p").first().download()


if __name__=="__main__":
    app=App()
    app.mainloop()