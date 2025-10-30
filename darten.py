from time import sleep

score = 501
beurt = 1
kopieScore = score
scoreLijst = []

def vraagScore(pijlNummer):
    while True:
        global scoreLijst
        scoreLijst.clear()
        score = str(input("Score van pijl " + str(pijlNummer) + ": "))
        if score.upper() == "BULL":
            score = 50
            scoreLijst.append("BULL")
            return score
        elif score.upper() == "KLEINE BULL":
            score = 25
            scoreLijst.append("KLEINEBULL")
            return score
        for tekens in score:
            scoreLijst.append(tekens)
        
def valideerScore(score):
    while True:
        if len(scoreLijst) > 3:
            print("Deze score is niet valide, probeer het opneiuw:")
            continue
        if len(scoreLijst) == 2:
            if scoreLijst[0] == 'd' or scoreLijst[0] == 't' or scoreLijst[0] == 'e':
                scoreLijst.insert(1,'0')
            elif scoreLijst[0].isdigit():
                scoreLijst.insert(0,'e') 
            else:
                print("Deze score is niet valide, probeer het opneiuw:")
                continue
        if len(scoreLijst) == 1:
            scoreLijst.insert(0,'e')
            scoreLijst.insert(1,'0')
        if int(scoreLijst[1] + scoreLijst[2]) > 20:
            print("Deze score is niet valide, probeer het opneiuw:")
            continue
        if scoreLijst[0] == 'd':
            score = int(scoreLijst[1] + scoreLijst[2]) * 2
        elif scoreLijst[0] == 't':
            score = int(scoreLijst[1] + scoreLijst[2]) * 3
        elif scoreLijst[0] == 'e':
            score = int(scoreLijst[1] + scoreLijst[2])
        return score

def beurtInvoeren():
    score1 = vraagScore("#1")
    checkFinish(score1)
    score2 = vraagScore("#2")
    checkFinish(score2)
    score3 = vraagScore("#3")
    checkFinish(score3)
    berekenScore(score1, score2, score3)
    return score

def berekenScore(score1, score2, score3):
    global score
    score -= (score1 + score2 + score3)

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

def startBeurt():
    global beurt
    global score
    global kopieScore
    kopieScore = score
    print("\n")
    print("Beurt",beurt,'\n'+"Aantal punten:",score,'\n')
    beurtInvoeren()
    beurt += 1


while score > 0:
    startBeurt()
    
 

