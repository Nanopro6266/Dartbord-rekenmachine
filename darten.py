from time import sleep

# Globals

score = 501
beurt = 1
kopieScore = score

# Functies

def vraagScore(pijlNummer):
    while True:
        scoreLijstFout = []
        scoreLijstFout.clear()
        score = str(input("Score van pijl " + str(pijlNummer) + ": "))
        if score.upper() == "BULL" or score.upper() == "B" or score.upper() == "KLEINE BULL" or score.upper() == "KB":
            scoreLijstFout.append(score.upper())
        else:
            for tekens in score:
                scoreLijstFout.append(tekens)
        return scoreLijstFout
       
def valideerScore(scoreLijstFout):
    scoreLijstGoed = []
    scoreLijstGoed = scoreLijstFout
    if scoreLijstFout[0] == "BULL" or scoreLijstFout[0] == "B" or scoreLijstFout[0] == "KLEINE BULL" or scoreLijstFout[0] == "KB":
        return scoreLijstFout
    if len(scoreLijstFout) > 3:
        print("Deze score is niet valide, probeer het opneiuw:(score > 3)")
        scoreLijstFout = vraagScore("")
    elif len(scoreLijstFout) == 2:
        if scoreLijstFout[0] == 'd' or scoreLijstFout[0] == 't' or scoreLijstFout[0] == 'e':
            scoreLijstGoed.insert(1,'0')
        elif scoreLijstFout[0].isdigit():
            scoreLijstGoed.insert(0,'e') 
        else:
            print("Deze score is niet valide, probeer het opneiuw:(score 2)")
            scoreLijstFout = vraagScore("")
    elif len(scoreLijstFout) == 1:
        scoreLijstGoed.insert(0,'e')
        scoreLijstGoed.insert(1,'0')
    else:
        if scoreLijstGoed[0] != 'e' and scoreLijstGoed[0] != 'd' and scoreLijstGoed[0] != 't':
            print("Deze score is niet valide, probeer het opneiuw (edt):")
            scoreLijstGoed = vraagScore("")
        if int(scoreLijstGoed[1] + scoreLijstGoed[2]) > 20:
            print("Deze score is niet valide, probeer het opneiuw (te hoog):")
            scoreLijstGoed = vraagScore("")
    return scoreLijstGoed
        
def berekenScorePijl(scoreLijstGoed):
    while True:
        if scoreLijstGoed[0] == "BULL" or scoreLijstGoed[0] == "B":
            score = 50
        elif scoreLijstGoed[0] == "KLEINE BULL" or scoreLijstGoed[0] == "KB":
            score = 25
        elif scoreLijstGoed[0] == 'd':
            score = int(scoreLijstGoed[1] + scoreLijstGoed[2]) * 2
        elif scoreLijstGoed[0] == 't':
            score = int(scoreLijstGoed[1] + scoreLijstGoed[2]) * 3
        elif scoreLijstGoed[0] == 'e':
            score = int(scoreLijstGoed[1] + scoreLijstGoed[2])
        return score

def checkFinish(Pijlscore, scoreLijst):
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
            sleep(1)
            print("\n")
            herstartSpel()
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
    checkFinish(score1, scoreLijstGoed1)
    scoreLijstFout2 = vraagScore("#2")
    scoreLijstGoed2 = valideerScore(scoreLijstFout2)
    score2 = berekenScorePijl(scoreLijstGoed2)
    checkFinish(score2, scoreLijstGoed2)
    scoreLijstFout3 = vraagScore("#3")
    scoreLijstGoed3 = valideerScore(scoreLijstFout3)
    score3 = berekenScorePijl(scoreLijstGoed3)
    checkFinish(score3, scoreLijstGoed3)
    berekenScoreBeurt(score1, score2, score3)
    return score

def startBeurt():
    global beurt
    global score
    global kopieScore
    kopieScore = score
    print("\n")
    print("Beurt",beurt,'\n'+"Aantal punten nog te gooien:",score,'\n')
    beurtUitvoeren()
    beurt += 1

def startSpel():
    global score
    global beurt
    score = int(input("Met hoeveel punten wil je spelen? "))
    beurt = 1
    while score > 0:
        startBeurt()

def herstartSpel():
    opnieuw = input("Wil je opnieuw spelen? (ja/nee): ").lower()
    if opnieuw == 'ja':
        startSpel()
    else:
        print("Bedankt voor het spelen!")
        exit()


# Hoofdprogramma
print("\n")
print("Welkom bij deze dartbord rekenmachine! Begin direct met spelen:")
sleep(1)
startSpel()
    
 

