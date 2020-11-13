from flask import Flask, render_template, request
import sys, random, csv, os
from csv import *

app = Flask(__name__)

    
#init + variables
round = 0
qround = 0
questionAmount = 11
question = ''
answer = ''
picture = ''
cash = 0

#create a player
class Player:
    def __init__(self,name,score,cart):
            self.name = 'name'
            self.score = 0
            self.cart = 0
    def pluscart(self,cash):
            self.cart += cash
    def plusscore(self):
            self.score += 1

class SweepItem:
    def __init__(self,name,price,pic):
        self.name = 'name'
        self.price = 0
        self.pic = ''

#init sweep items
si1 = SweepItem('name',0,'x')
si2 = SweepItem('name',0,'x')
si3 = SweepItem('name',0,'x')
si4 = SweepItem('name',0,'x')
si5 = SweepItem('name',0,'x')
si6 = SweepItem('name',0,'x')
si7 = SweepItem('name',0,'x')
si8 = SweepItem('name',0,'x')
si9 = SweepItem('name',0,'x')

#initialize initial players
p1 = Player('Green',0,0)
p2 = Player('Red',0,0)
p3 = Player('Blue',0,0)
p4 = Player('Purple',0,0)

#questions database
datafile = 'questions.csv'
questions = list(csv.reader(open(datafile,encoding='utf-8')))
gameQuestions = []

#sweepDB
sweepfile = 'sweeps.csv'
sweeps = list(csv.reader(open(sweepfile,encoding='utf-8')))

#prizeDB
prizefile = 'prizes.csv'
prizes = list(csv.reader(open(prizefile)))

#creates the sweep
#what a bad way to do this, I could have used a loop instead, but I don't feel like thinking right now
def generateSweep():
    random.shuffle(sweeps)
    global si1
    global si2
    global si3
    global si4
    global si5
    global si6
    global si7
    global si8
    global si9

    si1.name = sweeps[0][0]
    si2.name = sweeps[1][0]
    si3.name = sweeps[2][0]
    si4.name = sweeps[3][0]
    si5.name = sweeps[4][0]
    si6.name = sweeps[5][0]
    si7.name = sweeps[6][0]
    si8.name = sweeps[7][0]
    si9.name = sweeps[8][0]

    si1.pic = sweeps[0][2]
    si2.pic = sweeps[1][2]
    si3.pic = sweeps[2][2]
    si4.pic = sweeps[3][2]
    si5.pic = sweeps[4][2]
    si6.pic = sweeps[5][2]
    si7.pic = sweeps[6][2]
    si8.pic = sweeps[7][2]
    si9.pic = sweeps[8][2]

    si1.price = sweeps[0][1]
    si2.price = sweeps[1][1]
    si3.price = sweeps[2][1]
    si4.price = sweeps[3][1]
    si5.price = sweeps[4][1]
    si6.price = sweeps[5][1]
    si7.price = sweeps[6][1]
    si8.price = sweeps[7][1]
    si9.price = sweeps[8][1]

    return si1, si2, si3, si4, si5, si6, si7, si8, si9

   

#shuffles prizes and selects one
def getPrize():
    random.shuffle(prizes)
    global prize
    global prizepic
    prize = prizes[1][0]
    prizepic = prizes[1][1]
    return prize
    return prizepic    

#shuffles the question list, slices the first amount of questions, and appends them to gameQuestions[]
def GenerateQuestion(questionAmount):
    random.shuffle(questions)
    gameQuestions.append(questions[1:questionAmount+1:1])

#next few things do what they say on the box.

def getQuestion():
    global round
    global qround
    global question
    question = gameQuestions[0][round][0]
    return question
    
  

def getAnswer():
    global round
    global answer
    global qround
    answer = gameQuestions[0][round][1]
    return round
    return qround
    return answer
  


def getPicture():
    global round
    global picture
    picture = gameQuestions[0][round][2]
    return picture


#routing index
@app.route('/prize.html')
def prizeshow():
    GenerateQuestion(questionAmount)
    getPrize()
    generateSweep()
    return render_template('prize.html', variable=prize, variable2=prizepic)

@app.route('/question.html')
def ask():
    getQuestion()
    getPicture()
    global p1
    global p2
    global p3
    global p4
    return render_template('question.html', variable=question, variable2=picture, variable5=p1.name, variable6=p2.name, variable7=p3.name, variable8=p4.name)

@app.route('/answer.html')
def answers():
    getAnswer()
    global round
    global p1
    global p2
    global p3
    global p4
    return render_template('answer.html', variable=answer, variable2=round, variable5=p1.name, variable6=p2.name, variable7=p3.name, variable8=p4.name)

@app.route('/index.html')
def index():
     return render_template('index.html')



#This is the most backwards way of doing this, maybe in a future release I'll figure out how to fix it, but it's like this because I couldn't figure out how to increment a score based on one button
@app.route('/score.html')
def scoreboard():
    global p1
    global p2
    global p3
    global p4
    global round
    round += 1
    return render_template('score.html', variable=p1.score, variable2=p2.score, variable3=p3.score, variable4=p4.score, variable5=p1.name, variable6=p2.name, variable7=p3.name, variable8=p4.name, variable10=round, variable11=p1.cart, variable12=p2.cart, variable13=p3.cart, variable14=p4.cart)

@app.route('/score1.html')
def scoreboard1():
    global p1
    global p2
    global p3
    global p4
    global round
    p1.plusscore()
    round += 1

    return render_template('score1.html', variable=p1.score, variable2=p2.score, variable3=p3.score, variable4=p4.score, variable5=p1.name, variable6=p2.name, variable7=p3.name, variable8=p4.name, variable10=round, variable11=p1.cart, variable12=p2.cart, variable13=p3.cart, variable14=p4.cart)


@app.route('/score2.html')
def scoreboard2():
    global p1
    global p2
    global p3
    global p4
    global round
    p2.plusscore()
    round += 1
    return render_template('score2.html', variable=p1.score, variable2=p2.score, variable3=p3.score, variable4=p4.score, variable5=p1.name, variable6=p2.name, variable7=p3.name, variable8=p4.name, variable10=round, variable11=p1.cart, variable12=p2.cart, variable13=p3.cart, variable14=p4.cart)

@app.route('/score3.html')
def scoreboard3():
    global p1
    global p2
    global p3
    global p4
    global round
    p3.plusscore()
    round += 1
    return render_template('score3.html', variable=p1.score, variable2=p2.score, variable3=p3.score, variable4=p4.score, variable5=p1.name, variable6=p2.name, variable7=p3.name, variable8=p4.name, variable10=round, variable11=p1.cart, variable12=p2.cart, variable13=p3.cart, variable14=p4.cart)
  
@app.route('/score4.html')
def scoreboard4():
    global p1
    global p2
    global p3
    global p4
    global round
    p4.plusscore()
    round += 1
    return render_template('score4.html', variable=p1.score, variable2=p2.score, variable3=p3.score, variable4=p4.score, variable5=p1.name, variable6=p2.name, variable7=p3.name, variable8=p4.name, variable10=round, variable11=p1.cart, variable12=p2.cart, variable13=p3.cart, variable14=p4.cart)

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":

        global p1
        global p2
        global p3
        global p4

        req = request.form

        player1 = request.form["Player1"]
        player2 = request.form["Player2"]
        player3 = request.form["Player3"]
        player4 = request.form["Player4"]

        p1.name = player1
        p2.name = player2
        p3.name = player3
        p4.name = player4
    
     
    return render_template("/index.html")      

#all this stuff below here is a theoretical sweeps game, I may or may not come back to this in a future release.

@app.route('/final.html')
def sweepz():
    global p1
    global p2
    global p3
    global p4
    global si1
    global si2
    global si3
    global si4
    global si5
    global si6
    global si7
    global si8
    global si9


    return render_template('final.html', variable1=p1.name, variable2=p2.name, variable3=p3.name, variable4=p4.name, sin = si1.name, si2n = si2.name,si3n = si3.name, si4n = si4.name, si5n = si5.name, si6n = si6.name, si7n = si7.name, si8n = si8.name, si9n = si9.name, sip1 = si1.pic, sip2 = si2.pic,sip3 = si3.pic,sip4 = si4.pic,sip5 = si5.pic,sip6 = si6.pic,sip7 = si7.pic,sip8 = si8.pic,sip9 = si9.pic,)

#this is also a backwards algorithim, but it works 
@app.route("/sweep", methods=["GET","POST"])
def sweep():
    global p1
    global p2
    global p3
    global p4
    global si1
    global si2
    global si3
    global si4
    global si5
    global si6
    global si7
    global si8
    global si9

    player = request.form["player"]

    cash = 1
    cash = .5
    cash = 2.23

    finalcash = cash+cash2+cash3

    player.plusscore(finalcash)

    return render_template("/final.html")
   

#brings up server, needs to be on the bottom
if __name__ == "__main__":
    app.run()
