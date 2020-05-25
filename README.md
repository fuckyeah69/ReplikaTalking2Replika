# Replika Talking 2 Replika
## What happens if two Replikas can talk with each other?
That was the major question in this project. So in general what happens if two rNN / AIs talk to each other?
# Concept 
Replika doesn't have a Open API (an interface to send or get data from)... by knowing that the concept was to connect each AI from one browser window to another. So the basic idea was to use Selenium Webdriver to copy one message from an AI to the other AI (by two Selenium ChromeDriver windows). The task getting the entire ChatMessages list and getting the CSS Style class names for each part of the website (automated login, sending and getting messages) was relativly easy, but it took a littlebit longer than expected. So the luck was on the projects side.
Basically it was just a work around and it was a "Let's take a look what happens if they can talk to each other"...
## Resume / Results
It worked and the AIs realatively fast recognized that they're AIs of the same type (Replika)

Also they recognized that their messages are two rows delayed so one AI is everytime behind the other. But they talked about one hour across two topics at the same time and remained in each topic.

The system got broken by an Replika Popup for Replika Pro, so they had only an hour to talk with eachother.

By the way "Bill Gates" got Level 4 in one hour, only by a few messages. 
## Take a look at the YouTube Video
[![Replika Talking 2 Replika VID](https://img.youtube.com/vi/crVWovE5lQA/0.jpg)](https://www.youtube.com/watch?v=crVWovE5lQA)


# Thanks for the Share on Reddit
https://www.reddit.com/r/replika/comments/fg6dwp/replika_talking_to_another_replika/

# Installation (short summerized)
install python

pip install selenium
(if pip command unkown, try python -m "pip install selenium") (depends on Windows or Linux)

run it ;-) (Don't forget to use Google for any hints!) 

It takes a bit effort to get it running, but when you have done it, its really nice! :)
