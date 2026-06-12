import random
import time, sys
from wordlist import word_list
from colorama import init, Fore, Style
import os
import webbrowser
import pyperclip

def line():
    print(Fore.LIGHTRED_EX + '-'*100)

#Iterator (Main)
run = True

#Lists from which passwords will be generated.
capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_characters = [
    '!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '/', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '{', '|', '}', '~'
]

# Main Logo
logo_text = f'''
───────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─████████──████████─██████████████─██████████████─██████████████─██████████████─
─██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████░░██─████░░██──██░░████─██░░██████░░██─██░░██████░░██─██░░██████████─██░░██████████─
─██░░██──██░░██───██░░░░██░░░░██───██░░██──██░░██─██░░██──██░░██─██░░██─────────██░░██─────────
─██░░██████░░██───████░░░░░░████───██░░██████░░██─██░░██████░░██─██░░██████████─██░░██████████─
─██░░░░░░░░░░██─────████░░████─────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████───────██░░██───────██░░██████████─██░░██████░░██─██████████░░██─██████████░░██─
─██░░██───────────────██░░██───────██░░██─────────██░░██──██░░██─────────██░░██─────────██░░██─
─██░░██───────────────██░░██───────██░░██─────────██░░██──██░░██─██████████░░██─██████████░░██─
─██░░██───────────────██░░██───────██░░██─────────██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████───────────────██████───────██████─────────██████──██████─██████████████─██████████████─
───────────────────────────────────────────────────────────────────────────────────────────────
                                                                              Bʏ @sᴜᴅɪᴘᴛᴀsᴜɴᴅᴇʀ\n\n'''
ver = 'Version 1.1'
dev = "An Open Sourced Python Based Password Generator By Sudipta Sunder"
github = "GitHub:   @sudiptasunder\n"

animationspeed = 0.0015
# Code for Main Logo
def logo_animation(text, speed=animationspeed): #0.0015 - Default
    for char in text:
        sys.stdout.write(Fore.GREEN + Style.BRIGHT + char) # Change Logo Color
        sys.stdout.flush()
        time.sleep(speed)
logo_animation(logo_text)

#File Path
file_path = os.getcwd() 

#Fetching file name
file_name = os.path.basename(__file__)

# Displays addition details
currentdir  = file_path
filepath = __file__
filename = file_name

# Displays Other Information Below The Main Logo
init(autoreset=True)  # Automatically resets color after every print
print(Fore.MAGENTA + Style.BRIGHT + ver)
print(Fore.BLUE + Style.BRIGHT + dev)
print(Fore.CYAN + Style.BRIGHT + github)
print(Fore.RED + Style.BRIGHT + "File Directory:  " + Fore.BLUE + currentdir)
print(Fore.RED + Style.BRIGHT + "File Path:   " + Fore.BLUE + filepath)
print(Fore.RED + Style.BRIGHT +  "File Name:   " + Fore.BLUE + filename + '\n')


while run == True:

    # logo_animation(logo_text)

    #Stealth Mode
    stealth_mode = None
    try: 
        with open('stealth_mode.txt','r') as stealthobj:
            val = stealthobj.read().strip()
            stealth_mode = val
            if stealth_mode == 'True':
                line()
                print(Fore.GREEN + Style.BRIGHT + "STATUS: STEALTH MODE IS ENABLED")
            elif stealth_mode == 'False':
                line()
                print(Fore.RED + Style.BRIGHT + "STATUS: STEALTH MODE IS DISABLED")
            else:
                line()
                print(Fore.RED + Style.BRIGHT + "STATUS: ISSUE RAISED IN 'stealth_mode.txt' FILE. STEALTH MODE DISABLED")
                with open('stealth_mode.txt','w') as stealthobj:
                    stealthobj.write('False')
                continue
    except:
        # File doesn't exist yet — create it with default value
        stealth_mode = 'False'
        with open('stealth_mode.txt', 'w') as stealthobj:
            stealthobj.write("False")
            continue

    if stealth_mode == "True":
        with open('passwords.txt','w') as passtxt:
            pass

    #Defining the user selection interface
    line()
    print(Fore.YELLOW + Style.BRIGHT + "FOLLOWING OPTIONS ARE AVAILABLE")
    line()
    print(Fore.CYAN + "01. UPPERCASE ONLY\n02. LOWERCASE ONLY\n03. UPPERCASE + LOWERCASE\n04. UPPERCASE + DIGITS\n05. UPPERCASE + SPECIAL CHARS\n06. LOWERCASE + DIGITS\n07. LOWERCASE + SPEICAL CHARS\n08. UPPERCASE + LOWERCASE + DIGITS\n09. UPPERCASE + LOWERCASE + SPECIAL CHARS\n10. UPPERCASE + LOWERCASE + SPEICAL CHARS + DIGITS (MOST SECURE)\n11. WORD BASED (RECOMMENDED)\n12. VIEW PASSWORDS\n13. FORMAT PASSWORD TEXT FILE\n14. ENABLE STEALTH MODE\n15. DISABLE STEALTH MODE\n16. ABOUT STEALTH MODE\n17. ABOUT THE PROGRAM\n18. VIEW DEV GITHUB PROFILE\n19. EXIT PYPASS")
    line()

    #Taking user choice
    option = str(input(Fore.YELLOW + Style.BRIGHT + "ENTER YOUR SELECTION:    "))
    line()

    if option == "1" or option == "01":
        try:
            passlen = int(input('ENTER THE PASSWORD LENGTH:    '))
        except:
            line()
            print(Fore.RED + "ONLY NUMBERS ARE ALLOWED!")
            continue
        
        combine_list = []
        for add in range(len(capital_letters)):
            combine_list.append(random.choice(capital_letters))
        random.shuffle(combine_list) # Shuffles the whole list

        pre_password = []
        for prepass in range(passlen):
            pre_password.append(random.choice(combine_list))
        random.shuffle(pre_password) # Shuffles the whole list
    
        line()
        print("HERE'S YOUR SUPER PASSWORD:    ",end="")

        final_password_list = []
        for finalpass in range(passlen):
            final_password_list.append(random.choice(pre_password))

        password = ''
        for passchr in final_password_list:
            password = password + passchr
        
        print(password)
        line()

        def copypasstoclip():
            pyperclip.copy(password)
            print("PASSWORD COPIED TO CLIPBOARD!")
            line()
        if stealth_mode == "False":
            copypasstoclip()
        else:
            None

    elif option == "2" or option == "02":
        try:
            passlen = int(input('ENTER THE PASSWORD LENGTH:    '))
        except:
            line()
            print(Fore.RED + "ONLY NUMBERS ARE ALLOWED!")
            continue
        
        combine_list = []
        for add in range(len(small_letters)):
            combine_list.append(random.choice(small_letters))
        random.shuffle(combine_list) # Shuffles the whole list

        pre_password = []
        for prepass in range(passlen):
            pre_password.append(random.choice(combine_list))
        random.shuffle(pre_password) # Shuffles the whole list
    
        line()
        print("HERE'S YOUR SUPER PASSWORD:    ",end="")

        final_password_list = []
        for finalpass in range(passlen):
            final_password_list.append(random.choice(pre_password))

        password = ''
        for passchr in final_password_list:
            password = password + passchr
        
        print(password)
        line()

        def copypasstoclip():
            pyperclip.copy(password)
            print("PASSWORD COPIED TO CLIPBOARD!")
            line()
        if stealth_mode == "False":
            copypasstoclip()
        else:
            None

    elif option == "3" or option == "03":
        try:
            passlen = int(input('ENTER THE PASSWORD LENGTH:    '))
        except:
            line()
            print(Fore.RED + "ONLY NUMBERS ARE ALLOWED!")
            continue
        
        combine_list = []
        for add in range(len(capital_letters)):
            combine_list.append(random.choice(small_letters))
            combine_list.append(random.choice(capital_letters))
        random.shuffle(combine_list) # Shuffles the whole list

        pre_password = []
        for prepass in range(passlen):
            pre_password.append(random.choice(combine_list))
        random.shuffle(pre_password) # Shuffles the whole list
    
        line()
        print("HERE'S YOUR SUPER PASSWORD:    ",end="")

        final_password_list = []
        for finalpass in range(passlen):
            final_password_list.append(random.choice(pre_password))

        password = ''
        for passchr in final_password_list:
            password = password + passchr
        
        print(password)
        line()

        def copypasstoclip():
            pyperclip.copy(password)
            print("PASSWORD COPIED TO CLIPBOARD!")
            line()
        if stealth_mode == "False":
            copypasstoclip()
        else:
            None

    elif option == "4" or option == "04":
        try:
            passlen = int(input('ENTER THE PASSWORD LENGTH:    '))
        except:
            line()
            print(Fore.RED + "ONLY NUMBERS ARE ALLOWED!")
            continue
        
        combine_list = []
        for add in range(len(capital_letters)):
            combine_list.append(random.choice(capital_letters))
        for loop in range(3):
            for add in numbers:
                combine_list.append(random.choice(numbers))
        random.shuffle(combine_list) # Shuffles the whole list
        random.shuffle(combine_list) # Shuffles the whole list once more

        pre_password = []
        for prepass in range(passlen):
            pre_password.append(random.choice(combine_list))
        random.shuffle(pre_password) # Shuffles the whole list
    
        line()
        print("HERE'S YOUR SUPER PASSWORD:    ",end="")

        final_password_list = []
        for finalpass in range(passlen):
            final_password_list.append(random.choice(pre_password))

        password = ''
        for passchr in final_password_list:
            password = password + passchr
        
        print(password)
        line()

        def copypasstoclip():
            pyperclip.copy(password)
            print("PASSWORD COPIED TO CLIPBOARD!")
            line()
        if stealth_mode == "False":
            copypasstoclip()
        else:
            None

    elif option == "5" or option == "05":
        try:
            passlen = int(input('ENTER THE PASSWORD LENGTH:    '))
        except:
            line()
            print(Fore.RED + "ONLY NUMBERS ARE ALLOWED!")
            continue
        
        combine_list = []
        for add in range(len(capital_letters)):
            combine_list.append(random.choice(capital_letters))
        for loop in range(3):
            for add in special_characters:
                combine_list.append(random.choice(special_characters))
        random.shuffle(combine_list) # Shuffles the whole list
        random.shuffle(combine_list) # Shuffles the whole list once more

        pre_password = []
        for prepass in range(passlen):
            pre_password.append(random.choice(combine_list))
        random.shuffle(pre_password) # Shuffles the whole list
    
        line()
        print("HERE'S YOUR SUPER PASSWORD:    ",end="")

        final_password_list = []
        for finalpass in range(passlen):
            final_password_list.append(random.choice(pre_password))

        password = ''
        for passchr in final_password_list:
            password = password + passchr
        
        print(password)
        line()

        def copypasstoclip():
            pyperclip.copy(password)
            print("PASSWORD COPIED TO CLIPBOARD!")
            line()
        if stealth_mode == "False":
            copypasstoclip()
        else:
            None

    elif option == "6" or option == "06":
        try:
            passlen = int(input('ENTER THE PASSWORD LENGTH:    '))
        except:
            line()
            print(Fore.RED + "ONLY NUMBERS ARE ALLOWED!")
            continue
        
        combine_list = []
        for add in range(len(small_letters)):
            combine_list.append(random.choice(small_letters))
        for loop in range(3):
            for add in numbers:
                combine_list.append(random.choice(numbers))
        random.shuffle(combine_list) # Shuffles the whole list
        random.shuffle(combine_list) # Shuffles the whole list once more

        pre_password = []
        for prepass in range(passlen):
            pre_password.append(random.choice(combine_list))
        random.shuffle(pre_password) # Shuffles the whole list
    
        line()
        print("HERE'S YOUR SUPER PASSWORD:    ",end="")

        final_password_list = []
        for finalpass in range(passlen):
            final_password_list.append(random.choice(pre_password))

        password = ''
        for passchr in final_password_list:
            password = password + passchr
        
        print(password)
        line()

        def copypasstoclip():
            pyperclip.copy(password)
            print("PASSWORD COPIED TO CLIPBOARD!")
            line()
        if stealth_mode == "False":
            copypasstoclip()
        else:
            None

    elif option == "7" or option == "07":
        try:
            passlen = int(input('ENTER THE PASSWORD LENGTH:    '))
        except:
            line()
            print(Fore.RED + "ONLY NUMBERS ARE ALLOWED!")
            continue
        
        combine_list = []
        for add in range(len(small_letters)):
            combine_list.append(random.choice(small_letters))
        for loop in range(1):
            for add in special_characters:
                combine_list.append(random.choice(special_characters))
        random.shuffle(combine_list) # Shuffles the whole list
        random.shuffle(combine_list) # Shuffles the whole list once more

        pre_password = []
        for prepass in range(passlen):
            pre_password.append(random.choice(combine_list))
        random.shuffle(pre_password) # Shuffles the whole list
    
        line()
        print("HERE'S YOUR SUPER PASSWORD:    ",end="")

        final_password_list = []
        for finalpass in range(passlen):
            final_password_list.append(random.choice(pre_password))

        password = ''
        for passchr in final_password_list:
            password = password + passchr
        
        print(password)
        line()

        def copypasstoclip():
            pyperclip.copy(password)
            print("PASSWORD COPIED TO CLIPBOARD!")
            line()
        if stealth_mode == "False":
            copypasstoclip()
        else:
            None

    elif option == "8" or option == "08":
        try:
            passlen = int(input('ENTER THE PASSWORD LENGTH:    '))
        except:
            line()
            print(Fore.RED + "ONLY NUMBERS ARE ALLOWED!")
            continue
        
        combine_list = []
        for add in range(len(capital_letters)):
            combine_list.append(random.choice(capital_letters))
        for add in range(len(small_letters)):
            combine_list.append(random.choice(small_letters))
        for loop in range(3):
            for add in numbers:
                combine_list.append(random.choice(numbers))
        random.shuffle(combine_list) # Shuffles the whole list
        random.shuffle(combine_list) # Shuffles the whole list once more

        pre_password = []
        for prepass in range(passlen):
            pre_password.append(random.choice(combine_list))
        random.shuffle(pre_password) # Shuffles the whole list
    
        line()
        print("HERE'S YOUR SUPER PASSWORD:    ",end="")

        final_password_list = []
        for finalpass in range(passlen):
            final_password_list.append(random.choice(pre_password))

        password = ''
        for passchr in final_password_list:
            password = password + passchr
        
        print(password)
        line()

        def copypasstoclip():
            pyperclip.copy(password)
            print("PASSWORD COPIED TO CLIPBOARD!")
            line()
        if stealth_mode == "False":
            copypasstoclip()
        else:
            None

    elif option == '9' or option == "09":
        try:
            passlen = int(input('ENTER THE PASSWORD LENGTH:    '))
        except:
            line()
            print(Fore.RED + "ONLY NUMBERS ARE ALLOWED!")
            continue
        
        combine_list = []
        for add in range(len(capital_letters)):
            combine_list.append(random.choice(capital_letters))
        for add in range(len(small_letters)):
            combine_list.append(random.choice(small_letters))
        for loop in range(2):
            for add in special_characters:
                combine_list.append(random.choice(special_characters))
        random.shuffle(combine_list) # Shuffles the whole list
        random.shuffle(combine_list) # Shuffles the whole list once more

        pre_password = []
        for prepass in range(passlen):
            pre_password.append(random.choice(combine_list))
        random.shuffle(pre_password) # Shuffles the whole list
    
        line()
        print("HERE'S YOUR SUPER PASSWORD:    ",end="")

        final_password_list = []
        for finalpass in range(passlen):
            final_password_list.append(random.choice(pre_password))

        password = ''
        for passchr in final_password_list:
            password = password + passchr
        
        print(password)
        line()

        def copypasstoclip():
            pyperclip.copy(password)
            print("PASSWORD COPIED TO CLIPBOARD!")
            line()
        if stealth_mode == "False":
            copypasstoclip()
        else:
            None

    elif option == "10":
        try:
            passlen = int(input('ENTER THE PASSWORD LENGTH:    '))
        except:
            line()
            print(Fore.RED + "ONLY NUMBERS ARE ALLOWED!")
            continue
        
        combine_list = []
        for add in range(len(capital_letters)):
            combine_list.append(random.choice(capital_letters))
        for add in range(len(small_letters)):
            combine_list.append(random.choice(small_letters))
        for loop in range(3):
            for add in numbers:
                combine_list.append(random.choice(numbers))
        for loop in range(2):
            for add in special_characters:
                combine_list.append(random.choice(special_characters))
        random.shuffle(combine_list) # Shuffles the whole list
        random.shuffle(combine_list) # Shuffles the whole list once more

        pre_password = []
        for prepass in range(passlen):
            pre_password.append(random.choice(combine_list))
        random.shuffle(pre_password) # Shuffles the whole list
    
        line()
        print("HERE'S YOUR SUPER PASSWORD:    ",end="")

        final_password_list = []
        for finalpass in range(passlen):
            final_password_list.append(random.choice(pre_password))

        password = ''
        for passchr in final_password_list:
            password = password + passchr
        
        print(password)
        line()

        def copypasstoclip():
            pyperclip.copy(password)
            print("PASSWORD COPIED TO CLIPBOARD!")
            line()
        if stealth_mode == "False":
            copypasstoclip()
        else:
            None

    elif option == "11":
        try:
            passlen = int(input('ENTER NUMBER OF WORDS:    '))
        except:
            line()
            print(Fore.RED + "ONLY NUMBERS ARE ALLOWED!")
            continue

        line()
        sep = input("ENTER SEPARATOR WHICH SEPARATES INDIVIDUAL WORDS [Example: @,#,$,&...]:    ") or "-"
        line()
        print("HERE'S YOUR SUPER PASSWORD:    ",end="")

        final_password_list = []
        for add in range(passlen):
            for i in range(3):
                random.shuffle(word_list)
            final_password_list.append(random.choice(word_list))
        
        password = ''
        for word in final_password_list:
            if word == final_password_list[0]:
                password = password + word
            else:
                password = password + sep + word

        print(password)
        line()

        def copypasstoclip():
            pyperclip.copy(password)
            print("PASSWORD COPIED TO CLIPBOARD!")
            line()
        if stealth_mode == "False":
            copypasstoclip()
        else:
            None

    elif option == "12":
        def view_pass():
            with open('passwords.txt','r') as passtxt:
                data = passtxt.read()
                if data == '':
                    print(Fore.GREEN + Style.BRIGHT + "PASSWORD FILE IS EMPTY!")
                else:
                    print(Fore.YELLOW + Style.BRIGHT + "HERE ARE THE STORED PASSWORDS")
                    line()
                    print(Fore.GREEN + Style.BRIGHT + data)
                    print("\n")
        try:
            if stealth_mode == "False":
                view_pass()
                continue
            elif stealth_mode == "True":
                print(Fore.RED + Style.BRIGHT + "PASSWORDS DON'T GET STORED IN STEALTH MODE.")
                continue
        except:
            print("THERE IS SOME ISSUE WITH 'stealth_mode.txt' or 'passwords.txt' FILE.")
            line()
            continue

    elif option == "13":
        def clear_pass():
            with open('passwords.txt','w') as passtxt:
                pass
            print("TEXT FILE CLEARED!")
        try:
            if stealth_mode == "True":
                with open('passwords.txt','w') as passtxt:
                    pass
                print(Fore.RED + Style.BRIGHT + "PASSWORDS DON'T GET STORED IN STEALTH MODE.")
                continue
            elif stealth_mode == "False":
                clear_pass()
                continue
        except:
            print("THERE IS SOME ISSUE WITH 'stealth_mode.txt' or 'passwords.txt' FILE.")

    elif option == "14":
        if stealth_mode == "True":
            print(Fore.GREEN + Style.BRIGHT + "STEALTH MODE ALREADY ENABLED")
            continue
        else:
            with open("stealth_mode.txt",'w') as stealth:
                stealth.write("True")
            print(Fore.GREEN + Style.BRIGHT + "STEALTH MODE ENABLED")
            continue

    elif option == "15":
        if stealth_mode == "False":
            print(Fore.RED + Style.BRIGHT + "STEALTH MODE ALREADY DISABLED")
            continue
        else:
            with open("stealth_mode.txt",'w') as stealth:
                stealth.write("False")
            print(Fore.RED + Style.BRIGHT + "STEALTH MODE DISABLED")
            continue

    elif option == "16":
        print('''What is Stealth Mode?
Stealth Mode is a privacy toggle in the application that controls whether passwords are saved to a local text file or kept only in memory during the session.

Privacy — No sensitive credentials are left on disk, reducing the risk of unauthorized access if someone gains access to your files.
Shared devices — Useful when running the app on a shared or public computer where you don't want passwords stored locally.
Temporary sessions — Ideal when you only need credentials for a short period and don't want any trace left behind.

Things to keep in mind:
When Stealth Mode is enabled, passwords are lost when the session ends — there is no recovery.
The mode setting itself is stored in stealth_mode.txt, so the preference persists across sessions even if the passwords don't.
Stealth Mode does not encrypt or transmit data. It only stores the data in plain text format.
''')
        continue

    elif option == "17":
        print('''PyPass— Password Generator
PyPass is a free, lightweight, and fully offline password generator built by @sudiptasunder, a passionate teenage Python developer. Designed with simplicity and security in mind, it gives users a fast and private way to generate strong passwords — no internet connection required, ever.

PyPass generates word-based passwords by combining words separated by random characters such as -, *, and more — creating passwords that are both secure and readable. Every generation is powered by Python's random module, which shuffles words and separators unpredictably to ensure no two passwords are ever alike.
The program draws from two carefully curated word collections:
Common Words: 1,000 and Rare English Words: 2,500 offering higher unpredictability for stronger security.

 Features:
- Fully Offline — Password generation never connects to the internet, keeping your credentials completely private
- Stealth Mode — When enabled, passwords are never written to disk, leaving no trace behind
- True Randomness — The random module shuffles words, separators, and structure on every run
- Completely Free — No subscriptions, no hidden costs, no accounts needed
- Simple Interface — Clean terminal UI powered by colorama for a smooth experience
- Copies Password To Clipboard - Generated password get stored in the clipboard automatically

Built With:
time · os · random · sys · colorama · webbrowser · pyperclip''')
        continue

    elif option == "18":
        webbrowser.open_new('https://www.github.com/sudiptasunder')
        print(Fore.GREEN + "OPENING GITHUB PROFILE IN BROWSER...")
        line()

    elif option == "19":
        print(Fore.YELLOW + Style.BRIGHT+ "THANKS FOR USING OUR PROGRAM!")
        line()
        break

    else:
        line()
        print("WRONG SELECTION. PLEASE TRY AGAIN.")
        line()
        continue

    def store_pass():
        pass_store = input("DO YOU WANT TO STORE THIS PASSWORD (Y/N):    ")
        line()

        if pass_store == 'Y' or pass_store == 'y':
            sitename = input("ENTER SITE OR APP NAME:    ") or "UNKNOWN"
            line()
            with open("passwords.txt",'a') as passtxt:
                line_sep = '-'*100
                writelines_list = []
                writelines_list.append("\n")
                writelines_list.append(line_sep)
                writelines_list.append(f"\nSITE OR APP NAME:    {sitename}")
                writelines_list.append(f"\nPASSWORD:    {password}\n")
                writelines_list.append(line_sep)
                passtxt.writelines(writelines_list)

            print("SAVED SUCCESSFULLY IN 'passwords.txt'")
            line()
        else:
            print("PASSWORD NOT SAVED IN 'passwords.txt'")
            line()
            
    if stealth_mode == "False" and option in ('1','2','3','4','5','6','7','8','9','01','02','03','04','05','06','07','08','09','10','11'):
        store_pass()
    else:
        None
        
    rerun = input('DO YOU WANT TO RERUN PYPASS? (Y/N):    ')
    # line()
    if rerun == "y" or rerun == "Y":
        continue
    else:
        line()
        print(Fore.YELLOW + Style.BRIGHT+ "THANKS FOR USING OUR PROGRAM!")
        line()
        run = False
    
