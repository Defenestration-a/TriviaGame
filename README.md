# TriviaGame
This is a very simple, very rough, trivia game I made to learn some things.


Installation:

1)Extract the folder to your desktop. 

2)Install Python 3.8 - https://www.microsoft.com/en-us/p/python-38/9mssztt1n39l?activetab=pivot:overviewtab easiest way is through the windows store

3)Once python is installed, install the flask dependency for python. To do this open an elevated commandline window and type 'pip install flask'

4)Go to the install folder and select server.py, if done correctly you should get a console window that says" Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)", if you don't see anything that means it crashed meaning you didn't install flask or python correctly.

5)open a web browser(chrome) and navigate to http://localhost:5000/index.html

And there you go, the thing should work.




Usage: We will go page by page

Step 1: You should see a player enrollment form. Fill it out and press Enroll Players. This will set player names, the form will blank out when it has accepted the user name.
Step 2: Hit lets see what they're playing for!
Step 3: You'll be shown what the prize they're playing for is, right click on the Host Special area and "open as new window" NOTE: if you're streaming you'll want to hide this window as it contains answers as well as customizeable buttons
Step 4: Hit Lets see the questions, you'll have the question displayed, a picture that goes with the question and a "Who got it right window". When someone gets the question right bop their name
step 5: You'll get the score board which will increment by one depending on the last button you hit. 
Step 6: hit Lets get back to the game
Step 7: you'll have another question/picture displayed. Hit refresh on the host ui. If you lose the host ui you can get back by going directly to http://localhost:5000/answer.html

and that's it, the game is setup for ten questions, any more and the game will break(more on that in customization). To quit close the console window, to restart the quiz, close the console window and open server.py again. 



Customization:

Want to make the GUI classier?: Modify the HTML files located in templates directly. Everything should work fine so long as you don't edit integral code.

Want to edit/add/delete questions?: Modify questions.csv, should be self explanatory just follow the pattern, remember pictures go in main/static/images

Want to edit/add/delete prizes?: Modify prizes.csv, should be self explanatory just follow the pattern, remember pictures go in main/static/images

Change sound buttons/delete them?: Go to https://www.myinstants.com/index/us/ find a button you want, copy the embedded code from the website and add it to answers.html

Want more rounds in your game? edit server.py and change questionAmount = 11 to what ever number. NOTE: If you change it to have more rounds than you have questions you'll get a crash.


Note:
Welcome this is my second large project ever, as such the algorithims themselves are probably not as sleek as they could be, but they do work and have been tested.
