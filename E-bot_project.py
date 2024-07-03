import sys
import time
import pyautogui
# from getpass import getpass
# passkey = getpass("Enter the passkey: ")
passkey = pyautogui.password(
    text = "Enter the password: ", 
    title = "Password Entry",
    default = "", mask = "@")
if passkey == "161120" or passkey.lower() == "adarsh" or passkey == ".":
    # from distutils.cmd import Command
    # import smtplib
    # from tkinter import N
    import speech_recognition as sr
    import datetime
    import wikipedia
    import pyjokes
    import os
    import random
    from requests import get
    import webbrowser
    import pyttsx3
    import win32gui
    import win32con
    from pywinauto.application import Application
    import rotatescreen
    import requests
    from bs4 import BeautifulSoup
    # from selenium import webdriver
    # from selenium.webdriver.common.keys import Keys
    import ctypes
    import psutil   
    import openai

    listener = sr.Recognizer()
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    voices = engine.getProperty("rate")
    engine.setProperty('rate', 200)
    voices = engine.getProperty("volume")
    engine.setProperty('volume', 100)

    deg = 0
    screen = rotatescreen.get_primary_display()
    screen.rotate_to(deg)

    def speak(text):
        engine.say(text)
        engine.runAndWait()

    def user_commands():
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("listening...")
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source)
                # voice = listener.listen(source)
                voice = r.listen(source, timeout = 0, phrase_time_limit = 5)
                print ("Recognising...")
                command = r.recognize_google(voice, language = "en")
                # command = listener.recognize_google(voice)
                print ("Processing...")
        except:
            pass
            command = None
        return command

    def google():
        webbrowser.open("https://www.google.com/search?q=")
        pyautogui.moveTo(1239, 453, duration=0, tween=pyautogui.easeInOutQuad)
        pyautogui.sleep(5)
        pyautogui.click()
        while True:
            # print("google looop...")
            command = user_commands()
            print(command)
            if command == None:
                continue
            elif "google" in command.lower():
                pyautogui.moveTo(945, 190, duration=0, tween=pyautogui.easeInOutQuad)
                pyautogui.click()
                pyautogui.moveTo(710, 333, duration=0, tween=pyautogui.easeInOutQuad)
            elif "alexa" in command.lower():
                print("Present Sir!")
                speak("Present Sir!")
                # pyautogui.hotkey('ctrl', 'w')
                break
            elif "get lost" in command or "bye" in command:
                print("Bye-bye! Take Care!")
                speak("Bye-bye! Take Care!")
                sys.exit()
    
    def bing():
        webbrowser.open("https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx")
        pyautogui.moveTo(1239, 453, duration=0, tween=pyautogui.easeInOutQuad)
        pyautogui.sleep(5)
        pyautogui.press("tab")
        while True:
            # print("google looop...")
            command = user_commands()
            print(command)
            if command == None:
                continue
            elif "bing" in command.lower():
                pyautogui.press("space")
            elif "alexa" in command.lower():
                print("Present Sir!")
                speak("Present Sir!")
                # pyautogui.hotkey('ctrl', 'w')
                break
            elif "get lost" in command or "bye" in command:
                print("Bye-bye! Take Care!")
                speak("Bye-bye! Take Care!")
                sys.exit()

        # pyautogui.sleep(3)

    try:
        import pywhatkit
    except:
        speak("I have a headache. Better talk to google.")
        print("I have a headache. Better talk to google.")
        bing()
        # google()

    hour = int(datetime.datetime.now().hour)
    if (hour > 0 and hour < 12):
        speak("good morning sir!")
    elif (hour >= 12 and hour < 16):
        speak("good afternoon sir!")
    else:
        speak("good evening sir!")
    speak("How can I help you?")

    # preparing chatbot
    openai.api_key = "Use API key here"

    messages = []
    system_msg = "Alexa the chat bot"
    messages.append({"role": "system", "content": system_msg})
    # print("Your new assistant is ready!")
    # while input != "quit()":

    while True:
        # print("main loop...")
        # currentMouseX, currentMouseY = pyautogui.position()
        # print(currentMouseX)
        # print(currentMouseY)

        command = user_commands()
        command_0 = command
        if command == None:
            # print("listening2...")
            continue
        
        print(command)

        
        if "type" in command:
            command = command.replace("type", "")
            print("Typing " + command)
            speak("Typing " + command)
            pyautogui.typewrite(command)
        else:
            command = command.lower()
            if command == "alexa":
                print("Present Sir!")
                speak("Present Sir!")
                continue
            elif " alexa " in command:
                command = command.replace("alexa", "")
            elif " a " in command:
                command = command.replace("a ", "")
            elif " in " in command:
                command = command.replace("in ", "")
            elif " on " in command:
                command = command.replace("on ", "")
            elif " the " in command:
                command = command.replace("the ", "")
            elif " is " in command:
                command = command.replace("is ", "")
            elif " was " in command:
                command = command.replace("was ", "")
            elif " this " in command:
                command = command.replace("this ", "")

            print("Fetching Results...")


            if "notepad" in command:
                npath = "C:\\Windows\\system32\\notepad.exe"
                print("Opening NotePad.")
                speak("Opening NotePad.")
                os.startfile(npath)
                        
            elif "resume" in command:
                print("Resuming")
                speak("Resuming")
                # pyautogui.press("space")
                pyautogui.press("playpause")
            elif "pause" in command:
                print("Pausing")
                speak("Pausing")
                # pyautogui.press("space")
                pyautogui.press("playpause")

            elif "whatsapp" in command:
                print("Opening WhatsApp")
                speak("Opening WhatsApp")
                webbrowser.open("https://web.whatsapp.com/")
            elif "chat" in command:
                print("Opening WhatsApp")
                speak("Opening WhatsApp")
                webbrowser.open("https://web.whatsapp.com/")

            elif "search" in command:
                cm = command.replace("search", "")
                # speak("what are you searching for:")
                # cm = user_commands().lower()
                print("searching " + cm)
                speak("searching " + cm)
                cm = "https://www.google.com/search?q=" + cm
                webbrowser.open(f"{cm}")

            elif "send email" in command:
                print("To whom do you want to send?")
                speak("To whom do you want to send?")
                id = user_commands().lower()
                if id == None:
                    id = "adarsh08062003@gmail.com"
                elif "college" in id:
                    print("what is the roll number?")
                    speak("what is the roll number?")
                    roll = user_commands()
                    if roll == None:
                        roll = "033"
                    id = "2021ugce" + roll + "@nitjsr.ac.in"
                else:
                    email_list = {
                    'adarsh' : 'adarsh08062003@gmail.com',
                    'aadarsh' : 'adarsh08062003@gmail.com',
                    'karan' : 'rajkaran2093@gmail.com'
                    }
                    id = email_list[id]
                print(id)
                print("What is the subject?")
                speak("What is the subject?")
                sub = user_commands()
                print(sub)

                if(sub == None):
                    sub = ""
                print("What message do you want to send?")
                speak("What message do you want to send?")
                msg = user_commands()
                if msg == None:
                    msg = ""
                print(msg)

                # # less secure app access required
                # server = smtplib.SMTP('smtp.gamil.com', 587)
                # server.ehlo()
                # server.starttls()
                # print("test 0")
                # server.login('mail.automated.bot@gmail.com', '7352601381')
                # print("test 1")
                # server.sendmail('mail.automated.bot@gmail.com',id, msg)
                # server.close()

                webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")
                pyautogui.sleep(18)
                pyautogui.typewrite(id)
                pyautogui.press('enter')
                pyautogui.press('tab')
                pyautogui.typewrite(sub)
                pyautogui.press('enter')
                pyautogui.press('tab')
                pyautogui.typewrite(msg)
                pyautogui.press('enter')
                pyautogui.hotkey('ctrl', 'enter')
                print("Email sent successfully")
                speak("Email sent successfully")

            elif "text" in command:
                print("To whom do you want to text?")
                speak("To whom do you want to text?")
                receiver = user_commands()
                if receiver == None:
                    no = "9430759655"
                elif "number" in receiver:
                    print("To which number?")
                    speak("To which number?")
                    no = user_commands()
                else:
                    no_list = {
                        'adarsh' : '9430759655',
                    }
                    no = no_list[receiver.lower()]
                pno = "+91" + no
                print(pno)
                print("What message do you want to send?")
                speak("What message do you want to send?")
                msg = user_commands()
                print(msg)

                ## After time format:
                # print("After how many minutes from now do you want to send the message?")
                # speak("After how many minutes from now do you want to send the message?")
                # time = user_commands()
                # time = time.replace("minutes", "")
                # hour = int(datetime.datetime.now().hour) + time / 60
                # minut = datetime.datetime.now().minute + time % 60

                print("Do you want to send it now?")
                speak("Do you want to send it now?")

                confirmation = user_commands()

                if "yes" in confirmation.lower():
                    pywhatkit.sendwhatmsg(pno, msg, int(datetime.datetime.now().hour), int(datetime.datetime.now().minute) + int(1.5))
                else:
                    print("At what hour?")
                    speak("At what hour?")
                    hour = user_commands()
                    if hour == None:
                        hour = int(datetime.datetime.now().hour) 
                    elif hour.lower() == "now":
                        hour = int(datetime.datetime.now().hour) 
                    else:
                        hour = int(hour)
                    print(hour)
                    print("At what minute?")
                    speak("At what minute?")
                    minute = user_commands()
                    if minute == None:
                        minute = int(datetime.datetime.now().minute) + int(1.5)
                    elif minute.lower() == "now":
                        minute = int(datetime.datetime.now().minute) + int(1.5)
                    else:
                        minute = int(minute)
                    print(minute)
                    pywhatkit.sendwhatmsg(pno, msg, hour, minute)

            elif "press enter" in command:
                print("Pressing enter")
                speak("Pressing enter")
                pyautogui.press("enter")

            elif "rotate" in command or "note 8" in command or "rotation" in command:
                if "reset" in command:
                    print("Resetting screen rotation")
                    speak("Resetting screen rotation")
                    screen.rotate_to(0)
                else:
                    deg += 90
                    print(f"rotating screen {deg} degrees anti-clockwise")
                    speak(f"rotating screen {deg} degrees anti-clockwise")
                    if(deg == 360):
                        deg = 0
                    screen = rotatescreen.get_primary_display()
                    screen.rotate_to(deg)

            elif ("minimise") in command:
                print("Minimising Window")
                speak("Minimising Window")
                win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_MINIMIZE)

            elif ("maximize") in command or ("maximise") in command:
                print("Maximizing Window")
                speak("Maximizing Window")
                win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_MAXIMIZE)

            elif ("restore down") in command or ("store download") in command or ("restore window") in command:
                print("Restoring Down the Window")
                speak("Restoring Down the Window")
                pyautogui.moveTo(1297, 0, duration=0, tween=pyautogui.easeInOutQuad)
                pyautogui.click()

            elif ("desktop") in command:
                print("Going to Desktop")
                speak("Going to Desktop")
                # pyautogui.moveTo(1365, 767, duration=0.5, tween=pyautogui.easeInOutQuad)
                # pyautogui.click()
                pyautogui.hotkey("win", "d")


            elif "screenshot" in command or "shot" in command:
                print("Taking Screenshot")
                speak("Taking Screenshot")
                pyautogui.screenshot(f'ss{datetime.datetime.now().strftime("_%d-%m-%Y_%H-%M-%S")}.png')

            elif "double click here" in command:
                print("Double Clicking here")
                speak("Double Clicking here")
                pyautogui.doubleClick()

            elif "click here" in command:
                print("Clicking here")
                speak("Clicking here")
                pyautogui.click()

            elif "open task manager" in command:
                print("Opening Task Manager")
                speak("Opening Task Manager")
                pyautogui.hotkey('ctrl', 'shift', 'esc')
            
            elif "open run" in command:
                print("Opening run")
                speak("Opening run")
                pyautogui.hotkey('win', 'r')

            elif "incognito" in command:
                print("Opening new incognito window")
                speak("Opening new incognito window")
                pyautogui.hotkey('ctrl', 'shift', 'n')

            elif "open new window" in command:
                print("Opening new window")
                speak("Opening new window")
                pyautogui.hotkey('ctrl', 'n')

            elif "open new tab" in command:
                print("Opening new tab")
                speak("Opening new tab")
                pyautogui.hotkey('ctrl', 't')

            elif "close" in command and "tab" in command:
                print("Closing this tab")
                speak("Closing this tab")
                pyautogui.hotkey('ctrl', 'w')

            elif "app" in command or "tab" in command and "go" in command:
                if "one" in command or "1" in command or "first" in command:
                    print("Going to first tab")
                    speak("Going to first tab")
                    pyautogui.hotkey('ctrl', '1')
                elif "two" in command or "2" in command or "second" in command:
                    print("Going to second tab")
                    speak("Going to second tab")
                    pyautogui.hotkey('ctrl', '2')
                elif "three" in command or "3" in command or "third" in command:
                    print("Going to third tab")
                    speak("Going to third tab")
                    pyautogui.hotkey('ctrl', '3')
                elif "four" in command or "4" in command or "fourth" in command:
                    print("Going to fourth tab")
                    speak("Going to fourth tab")
                    pyautogui.hotkey('ctrl', '4')
                elif "five" in command or "5" in command or "fifth" in command:
                    print("Going to fifth tab")
                    speak("Going to fifth tab")
                    pyautogui.hotkey('ctrl', '5')
                elif "six" in command or "6" in command or "sixth" in command:
                    print("Going to sixth tab")
                    speak("Going to sixth tab")
                    pyautogui.hotkey('ctrl', '6')
                elif "seven" in command or "7" in command or "seventh" in command:
                    print("Going to seventh tab")
                    speak("Going to seventh tab")
                    pyautogui.hotkey('ctrl', '7')
                elif "eight" in command or "8" in command or "eighth" in command:
                    print("Going to eighth tab")
                    speak("Going to eighth tab")
                    pyautogui.hotkey('ctrl', '8')
                elif "nine" in command or "9" in command or "last" in command or "ninth" in command:
                    print("Going to last tab")
                    speak("Going to last tab")
                    pyautogui.hotkey('ctrl', '9')

            elif ("switch this window") in command or ("switch window") in command or ("which window") in command:
                print("Switching window")
                speak("Switching window")
                pyautogui.hotkey('alt', 'tab', interval = 0.5)

            elif ("switch this tab") in command or ("switch tab") in command or ("which tab") in command:
                print("Switching tab")
                speak("Switching tab")
                pyautogui.hotkey('ctrl', 'tab', interval = 0.5)

            elif ("close window") in command:
                print("Closing this window")
                speak("Closing this window")
                pyautogui.hotkey('alt', 'f4')


            # elif "select" in command:
            #     print("How many items do you want to select?")
            #     speak("How many items do you want to select?")
            #     try:
            #         # no = user_commands()
            #         no = 4
            #         print(no)
            #         print("Left or Right or Up or Down?")
            #         speak("Left or Right or Up or Down?")
            #         try:
            #             # cmd = user_commands()
            #             cmd = "left"
            #             pyautogui.keyDown('shift')
            #             while True:
            #                 pyautogui.write([cmd])
            #                 pyautogui.keyUp('shift')
            #                 no -= 1
            #                 if no == 0:
            #                     break
            #         except:
            #             print("Could not get that direction")
            #             speak("Could not get that direction")
            #     except:
            #         print("Could not get that")
            #         speak("Could not get that")

            elif "select all" in command:
                print("selecting all of the elements.")
                speak("selecting all of the elements.")
                pyautogui.hotkey('ctrl', 'a')
            
            elif "save" in command:
                print("Saving.")
                speak("Saving.")
                pyautogui.hotkey('ctrl', 's')

            elif "copy" in command:
                print("Copying!")
                speak("Copying!")
                pyautogui.hotkey('ctrl', 'c')

            elif "paste" in command:
                print("Pasting!")
                speak("Pasting!")
                pyautogui.hotkey('ctrl', 'v')

            elif "cut" in command:
                print("Cutting!")
                speak("Cutting!")
                pyautogui.hotkey('ctrl', 'x')

            elif "old write ati" in command:
                print("Holding right alt Key")
                speak("Holding right alt Key")
                pyautogui.keyDown("alt right")    

            elif "hold alt" in command or "old left airtel" in command:
                print("Holding alt Key")
                speak("Holding alt Key")
                pyautogui.keyDown("alt")      

            elif "hold shift" in command or "old swift" in command or "hold shift" in command:
                print("Holding Shift Key")
                speak("Holding Shift Key")
                pyautogui.keyDown("shift")

            elif ("hold ctrl") in command or ("hold control") in command:
                print("Holding controll Key")
                speak("Holding controll Key")
                pyautogui.keyDown("ctrl")

            elif ("press esc") in command or ("press escape") in command:
                print("Pressing escape Key")
                speak("Pressing escape Key")
                pyautogui.keyDown("esc")

            elif "press left arrow" in command:
                print("Pressing left arrow key")
                speak("Pressing left arrow key")
                pyautogui.press("left")

            elif "press tab" in command:
                print("Pressing tab key")
                speak("Pressing tab key")
                pyautogui.press("tab")

            elif "press right arrow" in command:
                print("Pressing right arrow key")
                speak("Pressing right arrow key")
                pyautogui.press("right")

            elif "press up arrow" in command:
                print("Pressing up arrow key")
                speak("Pressing up arrow key")
                pyautogui.press("up")

            elif "press down arrow" in command:
                print("Pressing down arrow key")
                speak("Pressing down arrow key")
                pyautogui.press("down")

            elif "press f1" in command:
                print("Pressing f1 key")
                speak("Pressing f1 key")
                pyautogui.press("f1")

            elif "press f2" in command:
                print("Pressing f2 key")
                speak("Pressing f2 key")
                pyautogui.press("f2")

            elif "press f3" in command:
                print("Pressing f3 key")
                speak("Pressing f3 key")
                pyautogui.press("f3")

            elif "press f4" in command:
                print("Pressing f4 key")
                speak("Pressing f4 key")
                pyautogui.press("f4")

            elif "press f5" in command:
                print("Pressing f5 key")
                speak("Pressing f5 key")
                pyautogui.press("f5")

            elif "press f6" in command:
                print("Pressing f6 key")
                speak("Pressing f6 key")
                pyautogui.press("f6")

            elif "press f7" in command:
                print("Pressing f7 key")
                speak("Pressing f7 key")
                pyautogui.press("f7")

            elif "press f8" in command:
                print("Pressing f8 key")
                speak("Pressing f8 key")
                pyautogui.press("f8")

            elif "press f9" in command:
                print("Pressing f9 key")
                speak("Pressing f9 key")
                pyautogui.press("f9")

            elif "press f10" in command:
                print("Pressing f10 key")
                speak("Pressing f10 key")
                pyautogui.press("f10")

            elif "press f11" in command:
                print("Pressing f11 key")
                speak("Pressing f11 key")
                pyautogui.press("f11")

            elif "press f12" in command:
                print("Pressing f12 key")
                speak("Pressing f12 key")
                pyautogui.press("f12")

            elif "roll" in command or "call" in command:
                if("up") in command:
                    print("Scrolling Up")
                    speak("Scrolling Up")
                    pyautogui.scroll(100)
                else:
                    print("Scrolling Down")
                    speak("Scrolling Down")
                    pyautogui.scroll(-100)

            elif "press left mouse button" in command:
                print("Pressing left mouse button")
                speak("Pressing left mouse button")
                pyautogui.click(button='left')

            elif "press right mouse button" in command:
                print("Pressing right mouse button")
                speak("Pressing right mouse button")
                pyautogui.click(button='right')


            elif "mouse down" in command:
                print("Moving the mouse down")
                speak("Moving the mouse down")
                try:
                    print("How many pixcels?")
                    speak("How many pixcels?")
                    pix = user_commands()
                    if pix == None:
                        pix = 10
                    print(pix)
                    pyautogui.move(0, pix)
                except:
                    print("Could not get that")
                    speak("Could not get that")
            elif "mouse up" in command:
                print("Moving the mouse down")
                speak("Moving the mouse down")
                try:
                    print("How many pixcels?")
                    speak("How many pixcels?")
                    piy = user_commands()
                    if piy == None:
                        piy = 10
                    print(piy)
                    pyautogui.move(piy, 0)
                except:
                    print("Could not get that")
                    speak("Could not get that")

            elif "move" in command and "mouse" in command:
                print("Moving the mouse")
                speak("Moving the mouse")
                try:
                    print("Tell me the X coordinate")
                    speak("Tell me the X coordinate")
                    pix = user_commands()
                    if pix == None:
                        pix = 10
                    else:
                        pix = int(pix)
                    print(pix)
                    print("Tell me the Y coordinate")
                    speak("Tell me the Y coordinate")
                    piy = user_commands()
                    if piy == None:
                        piy = 10
                    else:
                        piy = int(piy)
                    print(piy)
                    print("final test")
                    pyautogui.moveTo(pix, piy, duration=0, tween=pyautogui.easeInOutQuad)
                except:
                    print("Could not get that")
                    speak("Could not get that")


            elif "press backspace" in command:
                print("Pressing backspace")
                speak("Pressing backspace")
                pyautogui.press("backspace")

            elif "space bar" in command:
                print("Pressing space bar")
                speak("Pressing space bar")
                pyautogui.press("space")

            elif "command prompt" in command:
                print("Opening Command Prompt")
                speak("Opening Command Prompt")
                os.startfile("cmd")

            elif "brave" in command:
                print("Opening Brave Browser")
                speak("Opening Brave Browser")
                os.startfile("brave")

            elif "code" in command:
                print("Opening Visual Studio Code")
                speak("Opening Visual Studio Code")
                os.startfile("code")

            elif "chrome"in command or "crome" in command:
                print("Opening Google Chrome Web Browser")
                speak("Opening Google Chrome Web Browser")
                # os.startfile("chrome")
                app = Application().start(cmd_line = u'"C:\Program Files\Google\Chrome\Application\chrome.exe"--force-dark-mode ')

            elif "mozilla" in command or "firefox" in command:
                print("Opening Mozilla Firefox")
                speak("Opening Mozilla Firefox")
                os.startfile("firefox")

            elif "email" in command:
                print("Opening default Email")
                speak("Opening default Email")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            elif "official email" in command:
                print("Opening official Email")
                speak("Opening official Email")
                webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
            elif "college mail" in command or "college email" in command:
                print("Opening Institute mail")
                speak("Opening Institute mail")
                webbrowser.open("https://mail.google.com/mail/u/2/#inbox")

            elif "discord" in command:
                print("Opening Discord")
                speak("Opening Discord")
                webbrowser.open("https://discord.com/channels/@me")

            elif "linkedin" in command:
                print("Opening LinkedIn")
                speak("Opening LinkedIn")
                webbrowser.open("https://www.linkedin.com/feed/?trk=nav_back_to_linkedin")

            elif "play" in command:
                    command = command.replace("play", "")
                    if "spotify" in command or  "45" in command:
                        webbrowser.open("https://open.spotify.com/search")
                        command = command.replace("spotify", "")
                        command = command.strip()
                        pyautogui.sleep(10)            
                        print("playing" + command + "on Spotify")
                        speak("playing" + command + "on Spotify")
                        pyautogui.moveTo(549, 132, duration=0, tween=pyautogui.easeInOutQuad)
                        pyautogui.click()
                        pyautogui.typewrite(command, interval = 0)
                        pyautogui.press("enter")
                        pyautogui.sleep(2)
                        pyautogui.moveTo(639, 467, duration=1, tween=pyautogui.easeInOutQuad)
                        pyautogui.click()

                    elif ("offline") in command:
                        music_dir = "F:\\ADARSH\\MUSIC\\Songs"
                        songs = os.listdir(music_dir)
                        rd = random.choice(songs)
                        print("Playing a music offline")
                        speak("Playing a music offline")
                        os.startfile(os.path.join(music_dir, rd))

                    else:
                        print("Playing " + command + " on YouTube")
                        speak("Playing " + command + " on YouTube")
                        pywhatkit.playonyt(command)

            elif "fast forward" in command:
                print("Increasing the speed.")
                speak("Increasing the speed.")
                pyautogui.keyDown('ctrl')
                pyautogui.moveTo(700, 383, duration=0, tween=pyautogui.easeInOutQuad)
                i = 5
                while i:
                    pyautogui.scroll(10)
                    pyautogui.sleep(0.1)
                    i -= 1
                pyautogui.keyUp('ctrl')
                pyautogui.moveTo(1365, 500, duration=0, tween=pyautogui.easeInOutQuad)
            elif "slow" in command:
                print("Decreasing the speed.")
                speak("Decreasing the speed.")
                pyautogui.keyDown('ctrl')
                pyautogui.moveTo(700, 383, duration=0, tween=pyautogui.easeInOutQuad)
                i = 5
                while i:
                    pyautogui.scroll(-10)
                    pyautogui.sleep(0.1)
                    i -= 1
                pyautogui.keyUp('ctrl')
                pyautogui.moveTo(1365, 500, duration=0, tween=pyautogui.easeInOutQuad)

            elif "speed" in command:
                if "inc" in command:
                    print("Increasing the speed.")
                    speak("Increasing the speed.")
                    pyautogui.keyDown('ctrl')
                    pyautogui.moveTo(700, 383, duration=0, tween=pyautogui.easeInOutQuad)
                    for _ in range(5):
                        pyautogui.scroll(10)
                        pyautogui.sleep(0.1)
                    pyautogui.keyUp('ctrl')
                    pyautogui.moveTo(1365, 500, duration=0, tween=pyautogui.easeInOutQuad)
                elif "reset" in command:
                    print("Resetting the speed.")
                    speak("Resetting the speed.")
                    pyautogui.moveTo(375, 677, duration=0, tween=pyautogui.easeInOutQuad)
                    pyautogui.click()
                    pyautogui.moveTo(1365, 500, duration=0, tween=pyautogui.easeInOutQuad)
                else:
                    print("Decreasing the speed.")
                    speak("Decreasing the speed.")
                    pyautogui.keyDown('ctrl')
                    pyautogui.moveTo(700, 383, duration=0, tween=pyautogui.easeInOutQuad)
                    for _ in range(5):
                        pyautogui.scroll(-10)
                        pyautogui.sleep(0.1)
                    pyautogui.keyUp('ctrl')
                    pyautogui.moveTo(1365, 500, duration=0, tween=pyautogui.easeInOutQuad)


            elif "youtube" in command:
                print("Opening Youtube")
                speak("Opening Youtube")
                webbrowser.open("https://www.youtube.com/feed/subscriptions")

            elif "fast" in command:
                print("Openeng Fast.com")
                speak("Opening Fast.com")
                webbrowser.open("https://fast.com/#")

            elif "spotify" in command:
                print("Openeng Spotify")
                speak("Opening Spotify")
                webbrowser.open("https://open.spotify.com/")

            elif "telegram" in command or "tele" in command:
                print("Opening Telegram")
                speak("Opening Telegram")
                webbrowser.open("https://web.telegram.org/z/#777000")

            elif "facebook" in command or  "fb" in command:
                print("Opening FaceBook")
                speak("Opening FaceBook")
                webbrowser.open("https://www.facebook.com/")

            elif "instagram" in command or "insta" in command:
                print("Opening Instagram")
                speak("Opening Instagram")
                webbrowser.open("https://www.instagram.com/?theme=dark")

            elif "my ip address" in command:
                ip = get("https://api.ipify.org").text
                print("Your IP Address is " + ip)
                speak("Your IP Address is " + ip)    


            elif "time" in command:
                if "set" in command:
                    cm = command.replace("set", "")
                    print("setting " + cm)
                    speak("setting " + cm)
                    cm = "https://www.google.com/search?q=" + cm
                    webbrowser.open(f"{cm}")
                    pyautogui.sleep(3)
                    pyautogui.moveTo(796, 512, duration=0, tween=pyautogui.easeInOutQuad)
                    pyautogui.click()
                    pyautogui.moveTo(1365 , 512, duration=0, tween=pyautogui.easeInOutQuad)
                else:
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    print(time)
                    speak("The current time is " + time)

            elif "search" in command and "wikipedia" in command:
                search = command.replace("who", "")
                print(search)
                try:
                    info = wikipedia.summary(search, 1)
                    print(info)
                    speak(info)
                except:
                    print("Could not find this guy.")
                    speak("Could not find this guy.")

            elif "volume" in command:
                if "up" in command or "increase" in command:
                    print("Increasing the Volume.")
                    speak("Increasing the Volume.")
                    # # Works only in windows 7.
                    # pyautogui.moveTo(1197, 767, duration=0, tween=pyautogui.easeInOutQuad)
                    # pyautogui.sleep(.5)
                    # pyautogui.click()
                    # pyautogui.sleep(.5)
                    # pyautogui.scroll(500)
                    # pyautogui.moveTo(1365, 500, duration=0, tween=pyautogui.easeInOutQuad)
                    # pyautogui.click()
                    if "max" in command:
                        vol = 10
                    else: 
                        vol = 1
                    for _  in range(vol * 10):
                        pyautogui.press('volumeup')
                elif "down" in command or "decrease" in command:
                    print("Decreasing the Volume.")
                    speak("Decreasing the Volume.")
                    # # Works only in windows 7.
                    # pyautogui.moveTo(1197, 767, duration=0, tween=pyautogui.easeInOutQuad)
                    # pyautogui.sleep(.5)
                    # pyautogui.click()
                    # pyautogui.sleep(.5)
                    # pyautogui.scroll(-500)
                    # pyautogui.moveTo(1365, 500, duration=0, tween=pyautogui.easeInOutQuad)
                    # pyautogui.click()
                    for _  in range(10):
                        pyautogui.press('volumedown')

                else:
                    print("Could not get the command")
                    speak("Could not get the command")

            elif "mute" in command or "nud" in command:
                    print("Ok!")
                    speak("Ok!")
                    # # Works only in windows 7.
                    # pyautogui.moveTo(1197, 767, duration=0, tween=pyautogui.easeInOutQuad)
                    # pyautogui.sleep(.5)
                    # pyautogui.click()
                    # pyautogui.sleep(.5)
                    # pyautogui.moveTo(1201, 636, duration=0, tween=pyautogui.easeInOutQuad)
                    # pyautogui.click()    
                    # pyautogui.moveTo(1366, 500, duration=0, tween=pyautogui.easeInOutQuad)
                    # pyautogui.click()
                    pyautogui.press('volumemute')

            elif "shutdown" in command or "shut down" in command:
                print("Shutting Down the computer")
                speak("Shutting Down the computer")
                os.system("shutdown /s")
                sys.exit()
            
            elif "restart" in command:
                print("Restarting the computer")
                speak("Restarting the computer")
                os.system("shutdown /r")
                sys.exit()

            elif "start" in command:
                print("Pressing start")
                speak("Pressing start")
                pyautogui.press("win")
                # screenWidth, screenHeight = pyautogui.size()
                # pyautogui.moveTo(0, screenHeight, duration=0, tween=pyautogui.easeInOutQuad)
                # pyautogui.click()
            
            elif "log off" in command:
                print("Logging off")
                speak("Logging off")
                os.system("shutdown /l")
                sys.exit()
            
            elif "lock" in command:
                print("Locking the computer.")
                speak("Locking the computer.")
                ctypes.windll.user32.LockWorkStation()

            elif "joke" in command:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)


            # elif "love" in command:
            #     print("Love is a game of emotions and I lack that.")
            #     speak("Love is a game of emotions and I lack that.")

            elif "get lost" in command or "bye" in command:
                print("Bye-bye! Take Care!")
                speak("Bye-bye! Take Care!")
                sys.exit()

            elif "google" in command:
                google()
            elif "bing" in command:
                bing()
            
            elif "news" in command:
                # url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=83263a48521a48a797182dbc3926e513"
                url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=83263a48521a48a797182dbc3926e513"
                page = requests.get(url).json()
                articles = page["articles"]
                head = []
                for a in articles:
                    head.append(a["title"])
                for i in range(5):
                    head[i] = head[i].replace("- The Wall Street Journal", "")
                    head[i] = head[i].replace("- Wall Street Journal", "")
                    print(head[i])
                    speak(head[i])
            
            elif "temperature" in command or "weather" in command:
                try:
                    URL = "https://www.google.com/search?q=" + command
                    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
                    page = requests.get(URL, headers = headers)
                    soup = BeautifulSoup(page.content, 'html.parser')
                    temp = soup.find(class_="wob_t").get_text()
                    condition = soup.find(class_="wob_dcp").get_text()
                    location = soup.find(class_="BBwThe").get_text()
                    print(f"It's {temp} degrees centigrade in {location} and weather condition is {condition}")
                    speak(f"It's {temp} degrees centigrade in {location} and weather condition is {condition}")
                except:
                    print("Could not fetch the results.")
                    speak("Could not fetch the results.")
            
            elif "battery" in command:
                try:
                    percent = psutil.sensors_battery().percent
                    print(f"Currently the battery is having {percent} percent charge.")
                    speak(f"Currently the battery is having {percent} percent charge.")
                except:
                    print("Don't be silly. You are using a desktop.")
                    speak("Don't be silly. You are using a desktop.")

            
            else:
                print(command_0)
                # print("Let me think.")
                # speak("Let me think.")
                try:
                    # openai.api_key = "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"

                    # messages = []
                    # system_msg = "Alexa the chat bot"
                    # messages.append({"role": "system", "content": system_msg})
                    # # print("Your new assistant is ready!")
                    # # while input != "quit()":
                    # message = command_0
                    # messages.append({"role": "user", "content": message})
                    # response = openai.ChatCompletion.create(
                    #     model="gpt-3.5-turbo",
                    #     messages=messages)
                    # reply = response["choices"][0]["message"]["content"]
                    # messages.append({"role": "assistant", "content": reply})
                    # print("\n" + reply + "\n")

                    api_endpoint = "https://free.churchless.tech/v1/chat/completions"  # Replace with the appropriate API endpoint URL

                    headers = {
                        "Authorization": "Bearer ",  # Replace YOUR_API_KEY with your actual API key
                        "Content-Type": "application/json"
                    }

                    messages = []
                    system_msg = "Alexa by ADARSH"
                    messages.append({"role": "system", "content": system_msg})

                    # print("Your new assistant is ready!")

                    user_input = command_0
                    messages.append({"role": "user", "content": user_input})
                    payload = {
                        "model": "gpt-4",
                        "messages": messages
                    }
                    response = requests.post(api_endpoint, headers=headers, json=payload)
                    data = response.json()
                    reply = data["choices"][0]["message"]["content"]
                    messages.append({"role": "assistant", "content": reply})
                    print("\n" + reply + "\n")
                    speak(reply)

                except:
                    # try:
                    #     print("Would you like to hear Wikipedia summary?")
                    #     speak("Would you like to hear Wikipedia summary?")
                    #     confirmation = user_commands()
                    #     print(confirmation)
                    #     if "yes" in confirmation.lower():
                    #         info = wikipedia.summary(command, 1)
                    #         info = "According to wikipedia " + info
                    #         print(info)
                    #         speak(info)
                    #     else:
                    #         print("Ok!")
                    #         speak("Ok!")
                    # except:
                    #     print("Sorry! I didn't get that. Probably google may answer you.")
                    #     speak("Sorry! I didn't get that. Probably google may answer you.")
                    #     cm = "https://www.google.com/search?q=" + command
                    #     webbrowser.open(f"{cm}")

                    try:
                        URL = "https://www.google.com/search?q=" + command

                        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

                        page = requests.get(URL, headers = headers)
                        soup = BeautifulSoup(page.content, 'html.parser')
                        result = soup.find(class_="Z0LcW t2b5Cf CfV8xf").get_text()
                        print(result)
                        speak(result)
                        
                    except:
                        try:
                            URL = "https://www.bing.com/search?q=Bing+AI&showconv=1&FORM=hpcodx" + command

                            headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

                            page = requests.get(URL, headers = headers)
                            soup = BeautifulSoup(page.content, 'html.parser')
                            result = soup.find(class_="Z0LcW t2b5Cf CfV8xf").get_text()
                            print(result)
                            speak(result)
                            
                        except:
                            # print("Sorry! I didn't get that. Probably google may answer you.")
                            # speak("Sorry! I didn't get that. Probably google may answer you.")
                            # cm = "https://www.google.com/search?q=" + command
                            # webbrowser.open(f"{cm}")
                        
                            print("Sorry! I didn't get that.")
                            speak("Sorry! I didn't get that.")

        print("\n")
else:
    print("Better luck next time!!!")
    time.sleep(3)
    sys.exit()