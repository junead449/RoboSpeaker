import os

if __name__ == "__main__": 
    print("Welcome to RoboSpeaker Version 1.1: ")
    while True:
        x=input("Enter the Word that you want to speak: ")
        if x=='q':
            break
        command = f"say {x}"
        os.system(command)
