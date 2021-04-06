import os
import time

user_start = input("Start program? (y/n): ")

if user_start == "y":
    run_num = 0
    
    def startprog():
        os.system("shutdown /s /t 0") 

    while run_num < 256:
        print(f"Running proq {run_num}")
        run_num = run_num + 1
    
    print("done")
    time.sleep(1)
    startprog()

elif user_start == "n":
    print("Exiting program...")

else:
    print("Invalid input; exiting program...")
