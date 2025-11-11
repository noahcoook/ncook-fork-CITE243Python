# A simple stopwatch program
import time, pyperclip

# Display the program's instructions.
print('Press ENTER to begin and to mark laps. Ctrl-C quits.')
input() # Press Enter to begin.
print('Started.')
start_time = time.time() # Get the first lap's start time.
last_time = start_time
lap_number = 1

#sets all_laps variable to be used
all_laps = ''

# Start tracking the lap times.
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        #sets rjust so I can use it in the parentheses
        lap_time = f'{lap_time}'.rjust(6)

        #print(F'Lap # {lap_number}: {total_time} ({lap_time})', end='')
        timeData = (f'Lap # {lap_number}:'.rjust(8) + f'{total_time} '.rjust(8) + f'({lap_time})')

        print(timeData)
        
        #adds all lap data together so you can view it after stopwatch is done
        all_laps += timeData + '\n' + '\n'

        lap_number += 1
        last_time = time.time() # Reset the last lap time.

except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.\n')
    #copies to clipboard
    pyperclip.copy(all_laps)
    print('Output copied to clipboard')
