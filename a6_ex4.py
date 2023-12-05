import os
import datetime

def create_user(name, data, password, log_file='logs.txt'): # saving user data in txt file
    filename = f"{name}.txt"
    current_time = datetime.datetime.now() # get time

    with open(log_file, 'a') as log: # open log in append mode
        if os.path.exists(filename):
            log.write(f"Attempted creation of existing user {name} at {current_time}\n") # User exist already
        else:
            with open(filename, 'w') as user_file: # open user file
                user_file.write(f"{name}\n{data}\n{password}\n{current_time}\n") # save user information
            log.write(f"Created user {name} at {current_time}\n") # message in log file

def login(name, password, log_file='logs.txt'):
    filename = f"{name}.txt"
    current_time = datetime.datetime.now()

    with open(log_file, 'a') as log:
        log.write(f"Attempted login for user {name} at {current_time}\n")

        if not os.path.exists(filename):
            log.write(f"Attempted login for non-existing user {name} at {current_time}\n")
            return None

        with open(filename, 'r') as user_file:
            # read file & split lines; Then unpack list ignoring all values expect stored_password (ignored variables _)
            _, _, stored_password, _ = user_file.read().splitlines()

        if stored_password == password:
            log.write(f"Login successful for user {name} at {current_time}\n")
            return True
        else:
            log.write(f"Login failed for user {name} at {current_time}\n")
            return False

def change_password(name, old_password, new_password, log_file='logs.txt'):
    filename = f"{name}.txt"
    current_time = datetime.datetime.now()

    with open(log_file, 'a') as log:
        log.write(f"Attempted password change for user {name} at {current_time}\n")

        if not os.path.exists(filename):
            log.write(f"Password change failed for non-existing user {name} at {current_time}\n")
            return

        with open(filename, 'r') as user_file:
            user_info = user_file.read().splitlines()

        if user_info[2] == old_password:
            user_info[2] = new_password
            user_info[3] = str(current_time)
            with open(filename, 'w') as user_file:
                user_file.write('\n'.join(user_info)) # create single string of user_info(typ:lst) by (sep = \n)
            log.write(f"Password change successful for user {name} at {current_time}\n")
        else:
            log.write(f"Password change failed for user {name} at {current_time}\n")
