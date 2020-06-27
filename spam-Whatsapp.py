import time
import keyboard
import pyfiglet

title=pyfiglet.figlet_format("Whats-spam","graffiti")
print(title,'!!!WARNING!!! We are not responsible for your actions!!', sep="\n")

i=int(input('Insert number of messages: '))
text=input('Insert message: ')
letters=[]

for letter in text:
    letters.append(letter)

ok=input('Press enter when you are on your Whatsapp-web chat... ')
print('Wait a moment...')
time.sleep(7)
while (i>0):
    keyboard.press_and_release(letters)
    keyboard.press_and_release("enter")
    i=i-1
