from PIL import Image, ImageTk
from itertools import count, cycle
import tkinter as tk
import re
import SUNDAY_MAIN
import time
import threading
class ImageLabel(tk.Label):

    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
 
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
 
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
 
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
 
    def unload(self):
        self.config(image=None)
        self.frames = None
 
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)
 
#demo :
root = tk.Tk()
lbl = ImageLabel(root)
root.iconbitmap('D:\SUNDAY\\sunday1.ico')
root.title("   S.U.N.D.A.Y")
root.geometry("500x670")
root.configure(background="black")
text =tk.Text(root,width=40,height=3, bg="#150517", fg='white',font=('Times New Roman',15))
text.place(x=96,y=605)
label2 = tk.Label(root, text="S.U.N.D.A.Y:", bg="#43C6DB",font=("Impact",16))
label2.place(x=0, y=605)
#client:
text0 =tk.Text(root,width=42,height=1 , bg="#150517", fg='white',font=('Times New Roman',15))
text0.place(x=0,y=577)
label2 = tk.Label(root,height=1, text=": My.BOSS",font=("Impact",14))
label2.place(x=419, y=575)
lbl.pack()
lbl.load('D:\SUNDAY\sunday.gif')
def add_text():
    n=1; m=1
    text1=['text20']; text2=["text30"]
    with open('D:\SUNDAY\\texttt.txt', mode='r',encoding='UTF-8') as f:
        text1[0]=f.read()
        f.close()
    with open('D:\SUNDAY\\textttt.txt', mode='r',encoding='UTF-8') as f1:
        text2[0]=f1.read()
        f1.close()
    
    while True:
#Commonication for people-----
        text2.append("text3"+str(m))
        with open('D:\SUNDAY\\textttt.txt', mode='r',encoding='UTF-8') as f1:
            text2[m]=f1.read()
            f1.close()
        if text2[m]!=text2[m-1]:
            t=text2[m].split('\n')
            text0.delete("1.0","end")
            for i in t:
                i=i.strip()
                text0.tag_configure("center", justify='center')
                text0.insert('1.0', i)
                text0.tag_add("center", "1.0", "end")
                m2 = re.findall(r'\d', i)
                t=len(i.split())/5 +len(m2)/5.9
                time.sleep(t)
        m+=1 
        
        text1.append("text2"+str(n))
        with open('D:\SUNDAY\\texttt.txt', mode='r',encoding='UTF-8') as f:
            text1[n]=f.read()
            f.close()
        if text1[n]!=text1[n-1]:
            t=text1[n].split('\n')
            text.delete("1.0","end")
            for i in t:
                i=i.strip()
                text.tag_configure("center", justify='center')
                text.insert('1.0', i)
                text.tag_add("center", "1.0", "end")
                m1 = re.findall(r'\d', i)
                t=len(i.split())/5 +len(m1)/5.9
                time.sleep(t)
                text.delete("1.0","end")
        text0.delete("1.0","end")
        n+=1
        
run=SUNDAY_MAIN.run
thread = threading.Thread(target=run)
thread.daemon = True 
thread.start()
thread1=threading.Thread(target=add_text)
thread1.daemon=True
thread1.start()

text.tag_configure("center", justify='center')
text.insert("1.0","HI! I'M SUNDAY")
text.tag_add("center", "1.0","end")
root.mainloop()