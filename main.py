

import time
import sys

def delay_print(*args):
    for arg in args:
        
        if arg != args[-1]:
            for char in arg:
                if char == arg[-1]:
                    sys.stdout.write(char + '\n')
                    sys.stdout.flush()
                else:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)


            
        else:
            for char in arg:
                if char == arg[-1]:
                    sys.stdout.write(char + '\n')
                    sys.stdout.flush()
                else:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)
              

        time.sleep(0.8)


def main():
    delay_print("Hello, I'm a computer program")
    delay_print("What's your name?")
    nombre = input(": ")

    delay_print("You must enter a name")
   

    delay_print('Just kidding', nombre, 'is a great name!')
 

    delay_print("I'm going to ask you a few questions", nombre)
    delay_print("Enter a number: \n ... not greater than 10: ")
   
    num1 = int(input(''))
    time.sleep(1.5)
    if num1 > 10:
        delay_print("I said not greater than 10!")
        delay_print('iF yOu DoNt FoLlOw InStRuCtIoNs, I wONT ASK aGaIn: ')
        num1 = int(input(''))
        if num1 > 10:
            exit()
 
    if num1 % 2 == 0:
        delay_print("Even number, yuu are boringgg as f** humannn...")
    else:
        delay_print("Odd number, you are interesting..., rahter odd i'd say")
   
    delay_print("I'm going to ask you another question", nombre,'dont think you are interesting, im just bored')
    
    delay_print('How would you call me? ... only cool names please')
    name = input(' :')
 
    if 'j' in name:
        delay_print('I like you', nombre, 'you know what is GOod')
    else:
        delay_print('I dont like you', nombre, 'you know what is bad')
  
    delay_print('I have to go now', nombre, 'I have a date with a toaster')

    delay_print(name, 'out')


if __name__ == '__main__':
    main()


