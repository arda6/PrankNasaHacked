import time
import webbrowser
from gtts import gTTS
import os

print("""

M"""""""`YM                            M""MMMMM""MM                   dP       
M  mmmm.  M                            M  MMMMM  MM                   88       
M  MMMMM  M .d8888b. .d8888b. .d8888b. M         `M .d8888b. .d8888b. 88  .dP  
M  MMMMM  M 88'  `88 Y8ooooo. 88'  `88 M  MMMMM  MM 88'  `88 88'  `"" 88888"   
M  MMMMM  M 88.  .88       88 88.  .88 M  MMMMM  MM 88.  .88 88.  ... 88  `8b. 
M  MMMMM  M `88888P8 `88888P' `88888P8 M  MMMMM  MM `88888P8 `88888P' dP   `YP 
MMMMMMMMMMM                            MMMMMMMMMMMM                            """)

ques = str(input("Nasa Hacked Procces Start Y/n:"))
if ques == 'n':
    exit(print("bye"))
elif ques == 'y':
    print("Procces Start %0 ")
    tts = gTTS(text='Procces Started', lang='en')
    tts.save("1.mp3")
    os.system("1.mp3")
    time.sleep(10)
    print("#--------- %10")
    time.sleep(9)
    print("##-------- %20")
    time.sleep(7)
    print("###------- %30")
    time.sleep(8)
    print("####------ %40")
    time.sleep(4)
    print("#####----- %50")
    time.sleep(4)
    print("######---- %60")
    time.sleep(5)
    print("Waf Detecdet. Trying Waf Bypass Methods: %70")
    tts = gTTS(text='Waf Detecdet. Trying Waf Bypass Methods. %70 Complated', lang='en')
    tts.save("waf.mp3")
    os.system("waf.mp3")
    time.sleep(9)
    print("Succesful. Waf Bypassing.")
    tts = gTTS(text='Waf Bypassing. Getting Data İnformation. ', lang='en')
    tts.save("wafbypass.mp3")
    os.system("wafbypass.mp3")
    time.sleep(4)
    print("Getting Data Information and Creating a Report. ")
    time.sleep(4)
    print("#######--- %70")
    time.sleep(4)
    print("########-- %80")
    time.sleep(10)
    print("#########- %90")
    time.sleep(2)
    print("########## %100 Procces Complated.")
    print("Transaction Successful. ")
    tts = gTTS(text='Procces Complated.', lang='en')
    tts.save("succes.mp3")
    os.system("succes.mp3")
    time.sleep(2)
    print("Creating Report. Please Wait....")
    time.sleep(2)
    dosya = open("dumpednasa.txt", "a", encoding="utf-8")
    dosya.write("Nasa Hacked \n")
    dosya.write("https://geekprank.com/hacker/@https://www.hackednasadoc.org/private-documents/creditcartlist.txt")
    dosya.close()
    ques2 = str(input("All Information Uploaded to Data Center. You Want To Open Now ? Y/n:"))
    if ques2 == 'y':
        print("Hacking Successful. Information Opens...")
        time.sleep(2)
        os.system("start dumpednasa.txt")
        time.sleep(3)
        webbrowser.open("https://geekprank.com/hacker/@https://www.hackednasadoc.org/private-documents/creditcartlist.txt")
        print("Exiting The Program. Bye :)")
    else :
        exit("Exiting Program. Bye :)")