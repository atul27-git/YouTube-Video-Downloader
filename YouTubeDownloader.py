''' Initially we have to download the pytube Library which will enable you to download videos from YouTube. '''

#pip install pytube

import tkinter as tk
from pytube import YouTube

'''Creating the root window'''
root = tk.Tk()

'''Setting the dimension and the title for the root window'''
root.geometry('800x500')
root.title('Tkinter YouTube Downloader')

'''Creating the download video function'''
'''This will download the video only if the user has not prohibited it from downloading else it will show link Error'''
def downloadmp4():
    try:
        header.set('Downloading...')
        root.update()
		
        YouTube(link.get()).streams.first().download()
        link.set('Downloaded Successfully!')
        
    except Exception as e:
        
		header.set('Link Error')
        root.update()
        link.set('Enter the Correct Link!')

'''Creating a label widget at the start of the UI'''
tk.Label(root,text = 'Welcome to YouTube Video Downloader',font = 'Consolas 20 bold').pack()

'''Creating string variable header which would be used as the text in the widged'''
header = tk.StringVar()
header.set('Enter the link below')
tk.Entry(root, textvariable = header, font = ("Helvetica", 20),width = 0).pack(ipady = 3)

'''Creating the window for entering the link. Initially a string variable link was created for this. '''
link = tk.StringVar()
tk.Entry(root, textvariable = link, width = 40).pack(pady = 10)

'''Creating a Download button which has the downloadmp4 function as it's command'''
tk.Button(root, text = 'Download',command = downloadmp4).pack()

'''Looping the root window'''
root.mainloop()
