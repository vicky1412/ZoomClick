import subprocess
try:
    from pynput.mouse import Controller as MouseController
except:
    pass
from playsound import playsound
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
import psutil
import pyautogui
import clipboard
import tkinter
import threading
import time
import os

class gui:

    def __init__(self):
        self.thread1 = threading.Thread(target=self.run, daemon=True)
        self.exit_flag = False

    def run(self):
        while self.exit_flag == False:
            j = 0
            for i in range(20):
                self.bar['value'] = j + 5
                j += 5
                self.window.update_idletasks()
                time.sleep(0.02)

    def increase(self):
        try:
            value = int(self.t2["text"])
            self.t2["text"] = f"{value + 1}"
            self.t2.config(text=self.t2["text"])
        except Exception:
            pass



    def windows(self):
        self.window = tkinter.Tk()
        self.window.title("ZOOM CLICK")
        self.window.geometry("600x400+400+120")

    def labels(self):
        frame1 = tkinter.Frame()
        frame2 = tkinter.Frame()
        self.t1 = tkinter.Label(master=frame1, text="\nClass Attended", font=(8))
        self.t1.pack()
        self.t2 = tkinter.Label(master=frame2, text="0", bg='#dae3dc', font=(5))
        self.t2.pack(pady=20)
        tkinter.Label(self.window, text="Program running...", font=("Arial", 15)).place(x=230, y=200)
        frame1.pack()
        frame2.pack()

    def close_btn(self):
        os.system("TASKKILL /F /IM ZoomClick.exe")

    def butttons(self):
        tkinter.Button(self.window,text="Close", bg='#bab2b1',command = self.close_btn).place(x=280,y=300)

    def icons(self):
        p1 = tkinter.PhotoImage(file='zoom.png')
        self.window.iconphoto(False, p1)

    def progressbars(self):
        style = ttk.Style()
        style.theme_use('default')
        style.configure("grey.Horizontal.TProgressbar", background='green', thickness=5)
        self.bar = Progressbar(self.window, length=400, style='grey.Horizontal.TProgressbar', mode='indeterminate')
        self.bar.place(x=100, y=250)
        self.thread1.start()


    def window_loop(self):
        self.window.mainloop()
        self.exit_flag = True

class zoomproject:

    def __init__(self):
        self.mouse = MouseController()
        self.exit_flag = False
        self.t1 = threading.Thread(target=self.warning,daemon=True)


    def open_Chrome(self):
        subprocess.Popen("chrome.shortcut",shell=True)
        time.sleep(5)
        pyautogui.hotkey('alt', 'space', 'x')

    def loging_zoom(self):
        pyautogui.press('tab')
        pyautogui.write('email')
        pyautogui.press('tab')
        pyautogui.write('password')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')

    def feedback_giving(self):
        time.sleep(2)
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.click(170, 360)
        time.sleep(1)
        pyautogui.click(76, 532)
        time.sleep(1)
        pyautogui.scroll(-1000000)
        time.sleep(2)
        pyautogui.click(116, 673)
        time.sleep(2)
        pyautogui.press('tab')
        pyautogui.press('enter')

    def open_website(self):
        time.sleep(10)
        pyautogui.write("https://olympus.greatlearning.in/dashboard")
        time.sleep(1)
        pyautogui.press('enter')

        time.sleep(10)
        pyautogui.click(543, 52)
        pyautogui.hotkey('ctrl', 'c')
        url = clipboard.paste()

        if url == 'https://olympus.greatlearning.in/login':
            self.loging_zoom()

        time.sleep(5)
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        content = clipboard.paste()
        pyautogui.click(704, 97)
        if "Mentored session feedback" in content:
            self.feedback_giving()
        else:
            pass

    def ongoing_click(self):
        time.sleep(10)
        pyautogui.click(324,445)

    def scroll(self):
        time.sleep(2)
        try:
            self.mouse.scroll(0, -2)
        except:
            pass

    def join_session_click(self):
        time.sleep(2)
        pyautogui.click(688, 333)

    def close_chrome(self):
        if self.process_exists("chrome.exe"):
            os.system("TASKKILL /F /IM chrome.exe")
        else:
            pass

    def read_pointer_position(self):
        time.sleep(5)
        print('The current pointer position is {0}'.format(self.mouse.position))
        # or
        # currentMouseX, currentMouseY = pyautogui.position()

    def closing_zoom(self):
        if self.process_exists("Zoom.exe"):
            time.sleep(5)
            pyautogui.hotkey('alt','q')
            time.sleep(2)
            pyautogui.press('enter')
        else:
            pass

    def process_exists(self,process_name):
        progs = [ proc for proc in psutil.process_iter() if proc.name() == process_name ]
        if progs:
            return True
        else:
            return False

    def warning(self):
        while True:
            if self.exit_flag == True:
                break
            playsound('sound.mp3')

    def alertbox(self):
        x = tkinter.Tk()
        x.withdraw()
        messagebox.showerror("Alert", "something went wrong!\n check and fix it soon!!!")

    def exception(self):
        self.t1.start()
        self.alertbox()
        self.exit_flag = True
        time.sleep(3)
        self.exit_flag = False

    def do(self):
        try:
            self.open_Chrome()
            self.open_website()
            self.ongoing_click()
            self.scroll()
            self.join_session_click()
            self.checking_zoom()
            time.sleep(120)
            self.closing_zoom()
        except Exception:
            self.exception()

    def checking_zoom(self):
        time.sleep(120)
        if self.process_exists('Zoom.exe'):
            time.sleep(5)
            test1.increase()
        else:
            self.exception()

    def run(self):
        while True:
            if int(time.strftime("%H", time.localtime())) == 9 and int(time.strftime("%M", time.localtime())) == 45:
                self.do()
            elif int(time.strftime("%H", time.localtime())) == 11 and int(time.strftime("%M", time.localtime())) == 45:
                self.do()
            elif int(time.strftime("%H", time.localtime())) == 13 and int(time.strftime("%M", time.localtime())) == 45:
                self.do()
            elif int(time.strftime("%H", time.localtime())) > 13:
                break


test = zoomproject()
test1 = gui()

def zoom_access():
    test.run()

def gui_access():
    test1.windows()
    test1.labels()
    test1.butttons()
    test1.icons()
    test1.progressbars()
    test1.window_loop()

windowthread = threading.Thread(target=gui_access,daemon=True)


windowthread.start()
time.sleep(5)
zoom_access()
windowthread.join()

