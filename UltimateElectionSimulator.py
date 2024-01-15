#
# Ultimate Election Simulator
# by EuroNutella
# last updated: 28/07/2023
#
import random
import pyfiglet
from colorama import init, Fore, Style

init()

figlet = pyfiglet.Figlet(font='basic')

ultimate = figlet.renderText("ULTIMATE")
election = figlet.renderText("ELECTION")
simulator = figlet.renderText("SIMULATOR")

YELLOW = Fore.YELLOW + Style.BRIGHT
GREEN = Fore.GREEN + Style.BRIGHT
RED = Fore.RED + Style.BRIGHT
BLUE = Fore.BLUE + Style.BRIGHT
RESET = Style.RESET_ALL

print(YELLOW)
print(ultimate)
print(election)
print(simulator)
print(RESET)


parties = []

max_parties = input('How many parties do you want to simulate? ')
max_parties = int(max_parties)

for i in range(max_parties):
    party = input('Insert name of a party: ')
    parties.append(party)
print(GREEN +'Parties:',", ".join(parties),RESET)

def turnout():
    global minTurn
    global maxTurn
    minTurn = input('Minimum turnout: ')
    minTurn = int(minTurn)
    maxTurn = input('Maximum turnout: ')
    maxTurn = int(maxTurn)
    print(GREEN+'Minimum turnout set to '+str(minTurn)+RESET)
    print(GREEN+'Maximum turnout set to '+str(maxTurn)+RESET)

running = 'y'

def r_vote():
    print(GREEN + 'You have selected random percentages' + RESET)
    turnout()
    percentages = []
    tot_percent = 0
    for i in range(max_parties-1):
        max_percent = 100-tot_percent-(len(parties)-i-1)*1
        percentage = random.randint(0,max_percent)
        percentages.append(percentage)
        tot_percent = tot_percent + percentage
    percentages.append(100-tot_percent)
    random.shuffle(percentages)
    for i in range(len(parties)):
        print(BLUE,parties[i],':',percentages[i],'%',RESET)
    print(BLUE,'Turnout:',random.randint(minTurn,maxTurn),'%',RESET)

def a_vote():
    print(GREEN + 'You have selected adjusted percentages' + RESET)
    turnout()
    votes = []
    percentages = [0] *max_parties
    for i in range(max_parties):
        vote = input(f'What percentage does {parties[i]} currently have? ')
        vote = int(vote)
        votes.append(vote)
    ranChange = input('Maximum change: ')
    ranChange = int(ranChange)
    while sum(percentages) != 100:
        for i in range(max_parties):
            percent = random.randint(max(0,votes[i]-ranChange),min(100,votes[i]+ranChange))
            percentages[i] = percent
    for i in range(len(parties)):
        print(BLUE,parties[i],':',percentages[i],'%',RESET)
    print(BLUE,'Turnout:',random.randint(minTurn,maxTurn),'%',RESET)

def v_vote():
    print(GREEN + 'You have selected population votes (random turnout)' + RESET)
    turnout()
    votes = []
    total_votes = 0
    max_pop = input('What is the population? ')
    max_pop = int(max_pop)
    for i in range(len(parties)-1):
        max_vote = max_pop - total_votes - (len(parties)-i-1)*1
        vote = random.randint(0,max_vote)
        total_votes += vote
        votes.append(vote)
    votes.append(max_pop - total_votes)
    random.shuffle(votes)
    for i in range(len(parties)):
        print(BLUE,parties[i] + ': ' + str(round(votes[i]/max_pop*100, 2)) + '%','Number of votes:',votes[i],RESET)
    print(BLUE,'Turnout:',random.randint(minTurn,maxTurn),'%',RESET)

def t_vote():
    print(GREEN + 'You have selected population votes (true turnout)' + RESET)
    votes = []
    total_votes = 0
    max_pop = input('What is the population? ')
    max_pop = int(max_pop)
    for i in range(len(parties)):
        max_vote = max_pop - total_votes - (len(parties)-i)*1
        vote = random.randint(0,max_vote)
        total_votes += vote
        votes.append(vote)
    random.shuffle(votes)
    for i in range(len(parties)):
        print(BLUE,parties[i] + ': ' + str(round(votes[i]/total_votes*100, 2)) + '%','Number of votes:',votes[i],RESET)
    print(BLUE,'Turnout: ' + str(round(total_votes/max_pop*100, 2)) + '%','Total number of votes:',total_votes,RESET)

def rt_vote():
    print(GREEN + 'You have selected random percentages' + RESET)
    turnout()
    percentages = []
    tot_percent = 0
    for i in range(max_parties-1):
        max_percent = 100-tot_percent-(len(parties)-i-1)*1
        percentage = random.randint(0,max_percent)
        percentages.append(percentage)
        tot_percent = tot_percent + percentage
    percentages.append(100-tot_percent)
    random.shuffle(percentages)
    threshold = input('Electoral Threshold: ')
    threshold = int(threshold)
    numSeats = int(input('Total number of Seats: '))
    sPerc = 0
    sPercs = []
    for i in percentages:
        if i < threshold:
            sPercs.append(0)
        else:
            sPercs.append(i)
    for i in range(len(parties)):
        sPerc = sPercs[i]*100/sum(sPercs)
        print(BLUE,parties[i],'Percentage:',percentages[i],'%','Seats:',round(numSeats*sPerc/100, 0),RESET)
    print(BLUE,'Turnout:',random.randint(minTurn,maxTurn),'%',RESET)

def at_vote():
    print(GREEN + 'You have selected adjusted percentages + threshold' + RESET)
    turnout()
    votes = []
    percentages = [0] *max_parties
    threshold = input('Electoral Threshold: ')
    threshold = int(threshold)
    for i in range(max_parties):
        vote = input(f'What percentage does {parties[i]} currently have? ')
        vote = int(vote)
        votes.append(vote)
    ranChange = input('Maximum change: ')
    ranChange = int(ranChange)
    while sum(percentages) != 100:
        for i in range(max_parties):
            percent = random.randint(max(0,votes[i]-ranChange),min(100,votes[i]+ranChange))
            percentages[i] = percent
    numSeats = int(input('Total number of Seats: '))
    sPerc = 0
    sPercs = []
    for i in percentages:
        if i < threshold:
            sPercs.append(0)
        else:
            sPercs.append(i)
    for i in range(len(parties)):
        sPerc = sPercs[i]*100/sum(sPercs)
        print(BLUE,parties[i],'Percentage:',percentages[i],'%','Seats:',round(numSeats*sPerc/100, 0),RESET)
    print(BLUE,'Turnout:',random.randint(minTurn,maxTurn),'%',RESET)

def i_vote():
    print(GREEN + 'You have selected approval influenced' + RESET)
    turnout()
    GovParties = []
    votes = []
    GovNum = input('How many parties are in the government? ')
    GovNum = int(GovNum)
    for i in range(GovNum):
        GovParty = input('Government party: ')
        GovParties.append(GovParty)
    for i in range(max_parties):
        vote = input(f'What percentage does {parties[i]} currently have? ')
        vote = int(vote)
        votes.append(vote)
    ranChange = input('Maximum change: ')
    ranChange = int(ranChange)
    percentages = [0] *max_parties
    appRat = input('Approval Rating (round to integer): ')
    appRat = int(appRat)
    decider = random.randint(0,100)
    while sum(percentages) != 100:
        for i in range(max_parties):
            if parties[i] in GovParties:
                if decider < appRat:
                    percent = random.randint(votes[i],min(100,votes[i]+ranChange))
                elif decider == appRat:
                    percent = random.randint(max(0,votes[i]-ranChage),min(100,votes[i]+ranChange))
                else:
                    percent = random.randint(max(0,votes[i]-ranChange),votes[i])
            else:
                percent = random.randint(max(0,votes[i]-ranChange),min(100,votes[i]+ranChange))
            percentages[i] = percent
    for i in range(len(parties)):
        print(BLUE,parties[i],':',percentages[i],'%',RESET)
    print(BLUE,'Turnout:',random.randint(minTurn,maxTurn),'%',RESET)

def restart():
    running = input('Do you want to restart? (y/n) ')
    return running

print(YELLOW + 'r = random percentages')
print('a = adjusted percentages')
print('v = population votes (random turnout)')
print('t = population votes (true turnout)')
print('i = approval influenced' + RESET)

while running == 'y':
    res = input('Choose your mode: ')
    if res == 'r':
        trs = input('Do you want to put an electoral threshold? (y/n) ')
        if trs == 'y':
            rt_vote()
        else:
            r_vote()
        running = restart()
    elif res == 'a':
        trs = input('Do you want to put an electoral threshold? (y/n) ')
        if trs == 'y':
            at_vote()
        else:
            a_vote()
        running = restart()
    elif res == 'v':
        v_vote()
        running = restart()
    elif res == 't':
        t_vote()
        running = restart()
    elif res == 'i':
        i_vote()
        running = restart()
    else:
        print(RED + 'Invalid input!' + RESET)
        running = restart()

print(GREEN+'Finished!'+RESET)