# Building a clock

import time
import os
from rich.console import Console
from rich.panel import Panel

# Function to initialize time
def initial_time(second=0, minute=0, hour=0):
    print('Do you want to adjust your clock?\n[y]es or [n]o?')
    
    user_answer = input('> ').strip().lower()

    if user_answer == 'y':
        try:
            hour = int(input('hour: '))
            minute = int(input('minute: '))
            second = int(input('second: '))
            return second, minute, hour

        except ValueError:
            print('Please enter valid numbers for hour, minutes, and seconds.')
    return second, minute, hour

def time_verification(second, minute, hour):
    if second > 59:
        minute += 1
        second = 0
        
    if minute > 59:
        hour += 1
        minute = 0
        second = 0
        
    if hour > 23:
        hour = 0
    
    return second, minute, hour

# Function to start the clock
def start_clock():
    second, minute, hour = initial_time()
    console = Console()

    while True:
        if os.name == 'nt':
            os.system('cls')  # For Windows (NT)
        else:
            os.system('clear')  # For Unix-like systems (Linux, macOS)

        # Format the current time
        current_time = f'{hour:02}:{minute:02}:{second:02}'
        box_width = len(current_time) + 6 # 2 for padding and 4 for the box borders
        
        # Create a panel for the current time
        panel = Panel(
            current_time.center(len(current_time) + 4), # Center the time inside the box
            title='Current Time',
            width=box_width,
            border_style='cyan', # Change the border color
            padding=(1, 2) # Adjust the padding inside the panel
        )
        
        # Print the panel
        console.print(panel)

        # Increment time and handle overflows
        second += 1
        second, minute, hour = time_verification(second, minute, hour)

        # Used to simulate a real clock
        time.sleep(1)

# Start the clock
start_clock()
