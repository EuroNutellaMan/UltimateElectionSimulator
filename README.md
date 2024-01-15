# Ultimate Election Simulator

This is a CLI tool designed to help you generate random percentages for as many parties as you want. It can be used via the internet or installed locally for offline use.

## Requirements

- Linux operating system (see [this repo](https://github.com/EuroNutellaMan/UltimateElectionSimulator-Windows) for Windows or use [WSL](https://learn.microsoft.com/en-us/windows/wsl/install))
- Colorama 0.4.6 or newer
- Pyfiglet 1.0.2 or newer
- Python 3.11 or newer

## Installation

You can skip this if you want to use the web interface.

0. Clone this repository and navigate to it

```
git clone https://github.com/EuroNutellaMan/UltimateElectionSimulator.git && cd UltimateElectionSimulator
```

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Set up an alias for your shell for convenience (optional):

On bash shells, add this to your **.bashrc**:

```
alias UltimateElectionSimulator='python3 /path/to/UltimateElectionSimulator/UltimateElectionSimulator.py'
```

On zsh shells, add this to your **.zshrc**:

```
alias UltimateElectionSimulator="python3 /path/to/UltimateElectionSimulator/UltimateElectionSimulator.py"
```

On fish shells, add this in your **~/.config/fish/config.fish**:

```
alias UltimateElectionSimulator="python3 /path/to/UltimateElectionSimulator/UltimateElectionSimulator.py"
```

Replace /path/to with the path you cloned the repo in. You can choose any command you prefer instead of UltimateElectionSimulaor.

Restart the terminal afterwards.

## Usage

Go to the [web interface](https://colab.research.google.com/drive/1WwpImIunKsc9tQEHjfGVLWsn13lvhTKb?usp=sharing#scrollTo=xGNXeLJI3mDI) or run the installed program using a terminal and either the alias or the following command:

```
python3 /path/to/UltimateElectionSimulator/UltimateElectionSimulator.py
```

Insert the amount of parties you want to simulate and name them.

Choose one of 5 modes:

- **random percentages (r like random)**: will generate random integers that sum up to 100 and randomly assign them to each party. Turnout is a random number between the minimum and maximum turnout you set up. You may add a mode with electoral thresholds that tells you if a party passed or not.

- **adjusted percentages (a like adjusted)**: will ask you to input some integers that indicate what percentages does each party already have (or whichever percentage you want it to have) and will generate random percentages that can be at most x points less or x points more than the current one, where x is the range you provided it. Percentages will sum to 100. This is useful if you want parties that don't deviate too much from a certain value or from previous elections. Turnout is a random number between the minimum and maximum turnout you set up. You may add a mode with electoral thresholds that tells you if a party passed or not.

- **population votes (random turnout) (v like votes)**: will ask you to input an integer representing your population. The program will then generate random numbers up to that integer, then divide them by the max population to get the percentages (rounded to 2 decimals). All the votes will sum to the max population. Turnout is a random number between the minimum and maximum turnout you set up.

- **population votes (true turnout) (t like turnout)**: works similiarly to pop votes (random turnout) but instead of all the generated votes summing up to the max population there could be people that didn't vote. Turnout is the total votes divided by the max population, then multiplied by 100 and rounded to 2 decimals.

- **Approval influenced (i like influenced)**: works a lot like adjusted percentages mode but it takes into account the approval rating (rounded to an integer you'd like). Essentially approval rating is used as the chance for the governing parties to increase their popularity, this means a high approval rating will mean a higher chance the governing parties will have a bigger percentage, while on the contrary a low approval rating will mean they have a higher chance of losing percentage points.

You will then be asked to choose if you want to put a threshold. Choosing (y)es will automatically calculate the number of seats each party gets based on a given total and whether or not those parties reach the specified percentage of votes.

You will be asked to imput a minimum and a maximum turnout.

If you selected the threshold method you will be asked to insert the total amount of seats and the threshold.

You will be displayed with the results, then you can choose to restart.

If you choose (y)es to restart you will repeat from the mode selection.

## Notes

This is the official version I'll keep supporting from now on and the most up to date one. Therefore I strongly recommend using this.

This project is licensed via the MIT license.
