#
# Ultimate Election Simulator
# by EuroNutella
# last updated: 18/01/2024
#
import os
import random
import pyfiglet
from colorama import init, Fore, Style

# Initialises colorama
init()

# Creates the ascii colors
figlet = pyfiglet.Figlet(font='basic')

ultimate = figlet.renderText("ULTIMATE")
election = figlet.renderText("ELECTION")
simulator = figlet.renderText("SIMULATOR")

# Define the colors
YELLOW = Fore.YELLOW + Style.BRIGHT
GREEN = Fore.GREEN + Style.BRIGHT
RED = Fore.RED + Style.BRIGHT
BLUE = Fore.BLUE + Style.BRIGHT
RESET = Style.RESET_ALL

# Prints out the ascii title
os.system('clear')
print(YELLOW)
print(ultimate)
print(election)
print(simulator)
print(RESET)

# Generate a list of parties
parties = []

max_parties = int(input('How many parties do you want to simulate? '))

# Assign a name to each party
for i in range(max_parties):
    party = input('Insert name of a party: ')
    parties.append(party)
print(GREEN +'Parties:',", ".join(parties),RESET)

# Function to define minimum and maximum turnout
def turnout():
    global minTurn
    global maxTurn
    minTurn = int(input('Minimum turnout: '))
    maxTurn = int(input('Maximum turnout: '))
    print(f"{GREEN}Minimum turnout set to {minTurn}")
    print(f"Maximum turnout set to {maxTurn}{RESET}")

# Functions to display the results
def display_1(votes):
    for i in range(len(parties)):
        print(f"{BLUE}{parties[i]}: {votes[i]}%{RESET}")
    print(f"{BLUE}Turnout: {random.randint(minTurn,maxTurn)}%{RESET}")

def display_2(percentages, passed_percents, seat_number):
    for i in range(len(parties)):
        passed_percent = passed_percents[i]*100/sum(passed_percents)
        print(f"{BLUE}{parties[i]} percentage: {percentages[i]}% | Seats: {round(seat_number*passed_percent/100, 0)}{RESET}")
    print(f"{BLUE}Turnout: {random.randint(minTurn,maxTurn)}%{RESET}")


# Random percentages mode
def r_vote():
    print(f"{GREEN}You have selected random percentages{RESET}")
    turnout()
    percentages = []
    tot_percent = 0
    for i in range(max_parties-1): # Randomly generates enough percentages for all parties minus one
        max_percent = 100-tot_percent-(len(parties)-i-1)*1
        percentage = random.randint(0,max_percent)
        percentages.append(percentage)
        tot_percent += percentage
    percentages.append(100-tot_percent) # Adds the remaining percentage to the list of percentages
    random.shuffle(percentages) # Shuffles the percentages to ensure they're assigned randomly and not affected by order
    display_1(percentages)

# Adjusted percentages mode
def a_vote():
    print(f"{GREEN}You have selected adjusted percentages{RESET}")
    turnout()
    votes = [] # This one stores the votes to modify
    percentages = [0] *max_parties
    for i in range(max_parties): # Asks user what percentage the party originally had
        vote = int(input(f'What percentage does {parties[i]} currently have? '))
        votes.append(vote)
    ranChange = int(input('Maximum change: ')) # Asks user how much the parties can change at most 
    while sum(percentages) != 100: # Makes sure to run as long as the percentages add up to 100
        for i in range(max_parties): # Changes the original percentages to generate new ones
            percent = random.randint(max(0,votes[i]-ranChange),min(100,votes[i]+ranChange))
            percentages[i] = percent
    display_1(percentages)

# Population votes (random turnout) mode
def v_vote():
    print(f"{GREEN}You have selected population votes (random turnout){RESET}")
    turnout()
    votes = []
    total_votes = 0 # Makes sure to track how many people have voted so far
    max_pop = int(input('What is the population? ')) # Asks what the maximum population is
    for i in range(len(parties)-1): # Generates the amount of votes for all parties except one
        max_vote = max_pop - total_votes - (len(parties)-i-1)*1
        vote = random.randint(0,max_vote)
        total_votes += vote
        votes.append(vote)
    votes.append(max_pop - total_votes) # Adds the remaining votes to the last party
    random.shuffle(votes) # Shuffles votes to ensure random results without influence from order
    for i in range(len(parties)): # Prints results
        print(f"{BLUE}{parties[i]}: {round(votes[i]/max_pop*100, 2)}% | Number of votes: {votes[i]}{RESET}")
    print(f"{BLUE}Turnout: {random.randint(minTurn,maxTurn)}%{RESET}")

# Population votes (true turnout) mode
def t_vote():
    print(f"{GREEN}You have selected population votes (true turnout){RESET}")
    votes = []
    total_votes = 0 # Same as previous mode but also helps with calculating result and track turnout
    max_pop = int(input('What is the population? '))
    for i in range(len(parties)): # Calculates votes for all parties
        max_vote = max_pop - total_votes - (len(parties)-i)*1
        vote = random.randint(0,max_vote)
        total_votes += vote
        votes.append(vote)
    random.shuffle(votes)
    for i in range(len(parties)): # Calculates and prints out results
        print(f"{BLUE}{parties[i]}: {round(votes[i]/total_votes*100, 2)}% | Number of votes: {votes[i]}{RESET}")
    print(f"{BLUE}Turnout: {round(total_votes/max_pop*100, 2)}% | Total number of votes: {total_votes}{RESET}")

# Random + threshold mode
def rt_vote():
    print(f"{GREEN}You have selected random percentages{RESET}")
    turnout()
    percentages = []
    tot_percent = 0
    for i in range(max_parties-1): # See random percentages mode
        max_percent = 100-tot_percent-(len(parties)-i-1)*1
        percentage = random.randint(0,max_percent)
        percentages.append(percentage)
        tot_percent = tot_percent + percentage
    percentages.append(100-tot_percent)
    random.shuffle(percentages)
    threshold = int(input('Electoral Threshold: ')) # Asks for the threshold
    numSeats = int(input('Total number of Seats: ')) # Asks for the total amount of seats
    sPerc = 0
    sPercs = [] # Percentages above the threshold
    for i in percentages: # Checks if a percentage is less than threshold, stores the ones that are above or equal to it
        if i < threshold:
            sPercs.append(0)
        else:
            sPercs.append(i)
    display_2(percentages, sPercs, numSeats)

# Adjusted + threshold mode
def at_vote():
    print(f"{GREEN}You have selected adjusted percentages + threshold{RESET}")
    turnout()
    votes = []
    percentages = [0] *max_parties
    for i in range(max_parties): # See adjusted mode
        vote = int(input(f'What percentage does {parties[i]} currently have? '))
        votes.append(vote)
    ranChange = int(input('Maximum change: '))
    while sum(percentages) != 100:
        for i in range(max_parties):
            percent = random.randint(max(0,votes[i]-ranChange),min(100,votes[i]+ranChange))
            percentages[i] = percent
    threshold = int(input('Electoral Threshold: ')) # See mode above
    numSeats = int(input('Total number of Seats: '))
    sPerc = 0
    sPercs = []
    for i in percentages:
        if i < threshold:
            sPercs.append(0)
        else:
            sPercs.append(i)
    display_2(percentages, sPercs, numSeats)

# Approval influenced mode
def i_vote():
    print(f"{GREEN}You have selected approval influenced{RESET}")
    turnout()
    GovParties = []
    votes = []
    GovNum = int(input('How many parties are in the government? ')) # Asks for parties of the current government
    for i in range(GovNum): # Asks for the name of the party in the government
        GovParty = input('Government party: ')
        GovParties.append(GovParty)
    for i in range(max_parties): # Asks about current percentages to modify
        vote = int(input(f'What percentage does {parties[i]} currently have? '))
        votes.append(vote)
    ranChange = int(input('Maximum change: ')) # Asks how much can parties change
    percentages = [0] *max_parties
    appRat = int(input('Approval Rating (round to integer): ')) # Asks for the approval rating
    decider = random.randint(0,100) # Randomly chooses a number
    while sum(percentages) != 100:
        for i in range(max_parties):
            if parties[i] in GovParties: # If the party is in the government it will go through the conditions
                if decider < appRat: # Party will increase in popularity or stay the same
                    percent = random.randint(votes[i],min(100,votes[i]+ranChange))
                elif decider == appRat: # Same as adjusted mode
                    percent = random.randint(max(0,votes[i]-ranChage),min(100,votes[i]+ranChange))
                else: # Party will decrease in popularity or stay the same
                    percent = random.randint(max(0,votes[i]-ranChange),votes[i])
            else: # Same as adjusted mode
                percent = random.randint(max(0,votes[i]-ranChange),min(100,votes[i]+ranChange))
            percentages[i] = percent
    display_1(percentages)

# Asks user if it wants to restart
def restart():
    running = input('Do you want to restart? (y/n) ')
    if running == 'y' or running == 'n':
        return running
    else:
        print(f"{RED}Invalid input, try again!{RESET}")
        restart()

# Display modes for the user to select
print(f"{YELLOW}r = random percentages")
print('a = adjusted percentages')
print('v = population votes (random turnout)')
print('t = population votes (true turnout)')
print(f"i = approval influenced{RESET}")

running = 'y' # Necessary to run things multiple times

# Allows user to choose a mode as long as running is 'y'
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
        print(f"{RED}Invalid input!{RESET}")
        running = restart()

print(f"{GREEN}Finished! Goodbye!{RESET}")
