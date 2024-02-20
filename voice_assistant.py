import os
import pyttsx3 as pt
import pywhatkit
import speech_recognition as sr
import pyaudio
import pywhatkit
from flask import Flask
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import webbrowser
import os.path
import subprocess
from tkinter import *
#from selenium.webdriver.common.by import By
res=sr.Recognizer()
speech_over=pt.init()
#init-->used to get the input like as constructor
#rate-->used to speech rate
#volume-->used for volume sound
#voice-->voice over (male/female)
rate=speech_over.getProperty('rate')
speech_over.setProperty('rate',130)
volume=speech_over.getProperty('volume')
speech_over.setProperty('volume',0.9)
voices=speech_over.getProperty('voices')
speech_over.setProperty('voices',voices[1].id)

speech_over.say("Hi friend how are you?")
speech_over.runAndWait()
browser= "http://www.mepcoeng.ac.in/"
google_browser="https://www.google.com"
def talk(text):
  speech_over.say(text)
  speech_over.runAndWait()
def take_command():
  with sr.Microphone() as source:
        res.energy_threshold = 1000
        # res=adjust_for_ambient_noise(source,1.2)
        print("listening...")
        voice=res.listen(source)
        voice_2=res.listen(source)
        command=res.recognize_google(voice)
        command_2 = res.recognize_google(voice_2)
        command=command.lower() # for lowercase
        if 'who' and 'are' and 'you' in command:
            talk("i am your virtual assistant,my name is marc")
        elif "what" and "are" and "you" and "doing" in command:
            speak("i am concurrently working with you buddy")
            speak("what are you doing with others?")
        elif 'hi' in command:
            hour=datetime.datetime.now().hour
            if (hour>=0 and hour<12):
                  talk("hello,good morning buddy")
            elif (hour>=12 and hour<18):
                  talk("hello,good afternoon buddy")
            else:
                  talk("hello,good evening")
        elif 'date' in command:
            now=datetime.datetime.now()
            my_date=datetime.datetime.today()
            month_name=now.month
            day_name=now.day
            month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
            ordinalnames = [ '1st', '2nd', '3rd', ' 4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd','24rd', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
            print("Today is"+month_names[month_name-1]+" "+ordinalnames[day_name-1]+'.')
            talk("Today is" + month_names[month_name - 1] + " " + ordinalnames[day_name - 1] + '.')
        elif 'marc' and 'play'in command:
           command=command.replace('marc','')
           song=command.replace('play','')
           print(command)  #function call is here
           talk('playing your song '+song)
           print('playing..')
           pywhatkit.playonyt(song)
        elif 'time' in command:
            time=datetime.datetime.now().strftime('%H:%M')
            print(time)
            talk('current time is'+time)
        elif 'take' and 'browser' in command:
            talk("going to browser...")
            webbrowser.open(browser)
        elif 'my music' in command:
            talk('playing your list')
            music="C:\\Users\\Buvi_123\\Music"
            my_music=os.listdir(music)
            print(my_music)
            os.startfile(os.path.join(music,my_music[0]))
        elif 'open app' in command:
            talk('open your editor')
            app_path='"C:\Program Files (x86)\Dev-Cpp\devcpp.exe"'
            os.startfile(app_path)
        elif 'note' and 'it' in command:
            command=command.replace('note','')
            command=command.replace('it','')
            talk("Its been writing in the notepad")
            date=datetime.datetime.now()
            file_name=str(date).replace(":","-")+"-note.txt"
            with open(file_name,"w") as f:
                talk("please tell the content..")
                note=command
                f.write(note)
            subprocess.Popen(["C:\\Windows\\System32\\notepad.exe",file_name])
        elif 'open' and 'google' in command:
             talk("google is opening")
                  
             webbrowser.open(google_browser)
take_command()

driver_path = './chromedriver'
driver = webdriver.Chrome(driver_path)
driver.get("https://www.amazon.com")
search_bar = driver.find_element_by_id("twotabsearchtextbox")
search_bar.clear()
search_bar.send_keys(self.talk())
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.quit()

name_file=open("v name.txt","r")
name_assistant=name_file.read()
def main_screen():
    global screen
    screen = Tk()
    screen.title(name_assistant)
    screen.geometry("100x250")
    img=PhotoImage(file='your-icon')
    screen.tk.call('wm','iconphoto',root._w,img)

    name_label = Label(text=name_assistant, width=300, bg="black", fg="white", font=("Calibri", 13))
    name_label.pack()

    microphone_photo = PhotoImage(file="assistant_logo.png")
    microphone_button = Button(image=microphone_photo, command=Process_audio)
    microphone_button.pack(pady=10)

    settings_photo = PhotoImage(file="settings.png")
    settings_button = Button(image=settings_photo, command=change_name_window)
    settings_button.pack(pady=10)

    info_button = Button(text="Info", command=info)
    info_button.pack(pady=10)

    screen.mainloop()
main_screen()

class inflow:
    def get_info(self,title):
        self.title=title
        self.serv=Service("C:\chromedriver_win32\chromedriver.exe")
        self.op=webdriver.ChromeOptions()
        self.driver=webdriver.Chrome(service=self.serv,options=self.op)
        url="https://www.wikipedia.in"
        self.driver.get(url)
        search=self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(title)
        enter=self.driver.find_elements_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()


extract=inflow()
extract.get_info("stars")



