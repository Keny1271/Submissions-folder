import os
import platform

def shutdown(user_input):
    cleaned_input = str(user_input).strip().lower()
    
    if cleaned_input == "yes":
        print("Shutdown initiated in 1 minute...")
        
        # Check if the computer is Windows or Mac/Linux
        if platform.system() == "Windows":
            os.system("shutdown /s /t 60")  # Shuts down Windows in 60 seconds
        else:
            os.system("sudo shutdown -h 60")  # Shuts down Mac/Linux in 60 seconds
            
    elif cleaned_input == "no":
        print("aborted shut down")
    else:
        print("sorry, unrecognized input")

# --- REPLACE THE BOTTOM OF YOUR FILE WITH THIS ---
# This prompts you in the console and waits for you to type yes or no
choice = input("Do you want to shut down the computer? (yes/no): ")
shutdown(choice)
 
