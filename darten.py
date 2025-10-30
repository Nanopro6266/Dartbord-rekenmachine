# @David: Ik heb 't nu in aparte functies, maar als de score niet valide is komt ie in een inf loop
# K ga dat zsm oplossen mr k moet alleen nu weg...

from time import sleep

score = 501
beurt = 1
kopieScore = score
scoreLijst = []

def vraagScore(pijlNummer):
    while True:
        global scoreLijst
        scoreLijstFout = []
        scoreLijstFout.clear()
        score = str(input("Score van pijl " + str(pijlNummer) + ": "))
        if score.upper() == "BULL" or score.upper() == "B" or score.upper() == "KLEINE BULL" or score.upper() == "KB":
            scoreLijstFout.append(score)
        else:
            for tekens in score:
                scoreLijstFout.append(tekens)
        return scoreLijstFout
        
def valideerScore(scoreLijstFout):
    scoreLijstGoed = []
    scoreLijstGoed = scoreLijstFout
    while True:
        if len(scoreLijstFout) > 3:
            print("Deze score is niet valide, probeer het opneiuw:")
            continue
        if len(scoreLijstFout) == 2:
            if scoreLijstFout[0] == 'd' or scoreLijstFout[0] == 't' or scoreLijstFout[0] == 'e':
                scoreLijstGoed.insert(1,'0')
            elif scoreLijstFout[0].isdigit():
                scoreLijstGoed.insert(0,'e') 
            else:
                print("Deze score is niet valide, probeer het opneiuw:")
                continue
        if len(scoreLijstFout) == 1:
            scoreLijstGoed.insert(0,'e')
            scoreLijstGoed.insert(1,'0')
        if int(scoreLijstGoed[1] + scoreLijstGoed[2]) > 20:
            print("Deze score is niet valide, probeer het opneiuw:")
            continue
        return scoreLijstGoed
        
def berekenScorePijl(scoreLijstGoed):
    while True:
        if scoreLijstGoed[0] == 'd':
            score = int(scoreLijstGoed[1] + scoreLijstGoed[2]) * 2
        elif scoreLijstGoed[0] == 't':
            score = int(scoreLijstGoed[1] + scoreLijstGoed[2]) * 3
        elif scoreLijst[0] == 'e':
            score = int(scoreLijstGoed[1] + scoreLijstGoed[2])
        return score

def checkFinish(Pijlscore):
    global beurt
    global score
    global kopieScore
    probeerScore = kopieScore - Pijlscore
    if probeerScore < 0:
        print("KAPOT! Deze score is onder de nul, gooi opnieuw!")
        beurt += 1
        sleep(1)
        startBeurt()
    elif probeerScore == 1:
        print("KAPOT! Deze score is niet uit te gooien met een dubbel, gooi opnieuw!")
        beurt += 1
        sleep(1)
        startBeurt()
    elif probeerScore == 0:
        if scoreLijst[0] == 'd' or Pijlscore == 50:
            print("Yes, uit!")
            exit()
        else:
            print("KAPOT! Je moet uit met een dubbel or Bull!")
            beurt += 1
            sleep(1)
            startBeurt()
    else:
        kopieScore -= Pijlscore
    return kopieScore

def berekenScoreBeurt(score1, score2, score3):
    global score
    score -= (score1 + score2 + score3)

def beurtUitvoeren():
    scoreLijstFout1 = vraagScore("#1")
    scoreLijstGoed1 = valideerScore(scoreLijstFout1)
    score1 = berekenScorePijl(scoreLijstGoed1)
    checkFinish(score1)
    scoreLijstFout2 = vraagScore("#2")
    scoreLijstGoed2 = valideerScore(scoreLijstFout2)
    score2 = berekenScorePijl(scoreLijstGoed2)
    checkFinish(score2)
    scoreLijstFout3 = vraagScore("#3")
    scoreLijstGoed3 = valideerScore(scoreLijstFout3)
    score3 = berekenScorePijl(scoreLijstGoed3)
    checkFinish(score3)
    berekenScoreBeurt(score1, score2, score3)
    return score








def startBeurt():
    global beurt
    global score
    global kopieScore
    kopieScore = score
    print("\n")
    print("Beurt",beurt,'\n'+"Aantal punten:",score,'\n')
    beurtUitvoeren()
    beurt += 1


while score > 0:
    startBeurt()
    
 

