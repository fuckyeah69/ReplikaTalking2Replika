# Selenium Replika Talking 2 Replika
# Written by Karim Saad Sep 2019


# class= ChatMessagesList__ChatMessagesListInner-sc-1ajwmer-1 hitTgK
# class="ChatMessagesList__ChatMessagesListInner-sc-1ajwmer-1 hitTgK"

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Defs (Browser "Windows")
browser = webdriver.Chrome()
browser2 = webdriver.Chrome()

# Global Messages Containers (idk if it's used in the current version)
globalMessagesRep1 = [] # first Replika
globalMessagesRep2 = [] # second Replika

# Automated Login, please don't abuse it!
def DoLogin(browser, username, password):
    #emailOrPhone - input 
    #login-password - input 
    #sc-AykKD FullscreenLayout__SubmitButton-sc-1a0qg1-2 bbVTcV - button
    browser.get('https://my.replika.ai/login')
    browser.find_element_by_id("emailOrPhone").send_keys(username)
    browser.find_element_by_tag_name("button").click()
    time.sleep(1)
    #JS.executeScript("document.getElementById('Password').value='password123'");
    browser.find_element_by_id ("login-password").send_keys(password)
    elements = browser.find_elements_by_tag_name('button')
    elements[len(elements)-1].click()
    time.sleep(5)
    try: 
        browser.find_element_by_class_name('DialogLayout__StyledCloseIcon-sc-103t4c8-2').click()
    except:
        pass

# Sends a Message by typing the text by "send_keys"
def SendMessage(browser, text):
    #send-message-textarea
    try:
        time.sleep(2)
        textarea=browser.find_element_by_id("send-message-textarea")
        textarea.send_keys(text)
        textarea.send_keys(Keys.ENTER)
    except:
        print("err with sending msg")
        pass

# Poor Method for getting all Messages out of Selenium Window... 
def GetMessages(browser, messages=[]):
    try:
        cid = "ChatMessagesList__ChatMessagesListInner-sc-1ajwmer-1"
        divs = browser.find_element_by_class_name(cid)
        divs = divs.find_elements_by_tag_name("div")
        for x in divs:
            spans = x.find_elements_by_tag_name("span")
            for x in spans:
                message = x.get_attribute('innerHTML')
                if not message in messages and not "<span>" in message:
                    messages.append(message)
        return messages
    except:
        pass

# Gets TheLastMessage out of Array messages
def GetLastMessage(browser, messages=[]):
    try:
        return messages[len(messages)-1]
    except:
        pass

# Does the reading messages from each window and sending stuff
def DoMessageLoop(browser, browser2):
    lastlastmessage1 = ""
    lastlastmessage2 = ""
    lastSame1 = False
    lastSame2 = False

    while True:
        #Getting current Messages (for checking if any new messages)
        r1 = GetMessages(browser, globalMessagesRep1)
        r2 = GetMessages(browser2, globalMessagesRep2)

        # Getting of each messages array the last message (usually it's the newest)
        lmg1 = GetLastMessage(browser, r1)
        lmg2 = GetLastMessage(browser2, r2)

        print("Got ", lmg1, lmg2)

        lastSame1 = True
        lastSame2 = True

        # Checking if something changed, if yes doing the stuff like sending it etc.
        if lmg1 != lastlastmessage1:
            SendMessage(browser2, lmg1)
            print("Sended" , lmg2)
            lastlastmessage1 = lmg1
            lastSame1 = False

        if lmg2 != lastlastmessage2:
            SendMessage(browser, lmg2)
            print("Sended" , lmg2)
            lastlastmessage2 = lmg2
            lastSame2 = False

        if lastSame1 and lastSame2:
            SendMessage(browser, "t")


# First of All do the login stuff
DoLogin(browser, "username1", "password1")
DoLogin(browser2, "username2", "password")

# Let's chat them
import _thread
_thread.start_new_thread(DoMessageLoop, (browser, browser2,))

# Waiting for input after loop "finished"
input("k")
browser.close()
browser2.close()