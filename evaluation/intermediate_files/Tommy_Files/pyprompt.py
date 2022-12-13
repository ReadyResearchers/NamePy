# implement a command shell that provides all of the features
# that the course instructor described at the start of lab and are
# further described inside of the README.md file in this repository.
import os
import stat


def pwd():
    """Function to print the current working directory."""
    # os module call to get the CWD
    pwd = os.getcwd()
    print(pwd)
    return 0


def list_files():
    """Function to list the files of the current working directory."""
    # make a directory list from the cwd
    path = os.getcwd()
    dir_list = os.listdir(path)
    # print the cwd alongside each item in the list
    for item in dir_list:
        print(path ,item)
    return 0


def change_directory(target_path):
    """Function to change the directory."""
    try:
        # os module call to change the directory depending on the target path
        os.chdir(target_path)
        return 0
    # for any error, print the following string
    except Exception:
        print("File or directory is not valid")
        return 1


def exit_shell():
    """Function to exit the shell."""
    exit()


# dictionary that contains commands as keys and functions as values
command_dict = {"pwd": pwd, "ls": list_files, "quit": exit_shell, "exit": exit_shell}


def main():
    """Main function to enter either an interactive or non-interactive shell."""
    # print("")
    print("pyprompt 0.1.0")
    # print("")
    # infinite while loop to enter the shell
    while True:
        # catch if the run command is redirected
        mode = os.fstat(0).st_mode
        if stat.S_ISREG(mode):
            # print ("stdin is redirected")
            try:
                x = input("> ")
                if x.startswith("cd"):
                    target_path = x.replace("cd", "").strip()
                    print("cd", target_path)
                    change_directory(target_path)
                # use elifs for commands rather than the dictionary for redirection
                elif x == "pwd":
                    print("pwd")
                    pwd()
                elif x == "ls":
                    print("ls")
                    list_files()
                elif x == "quit" or x == "exit":
                    if x == "quit":
                        print("quit")
                    else:
                        print("exit")
                    exit_shell()
                else:
                    print("Command not found")
            except KeyboardInterrupt:
                print("\nCommand not found")

        else:
            try:
                x = input("> ")
                # look for commands starting with cd
                if x.startswith("cd"):
                    # strip the cd to extract the path given
                    target_path = x.replace("cd", "").strip()
                    # use the path with the change_directory function
                    change_directory(target_path)
                # look for keys in dictionary
                elif x in command_dict:
                    # attach () to the value name in order to call the function
                    command_dict[x]()
                # produce error if command is not in the dictionary
                else:
                    print("Command not found")
            # print a string if ctrl+C is used
            except KeyboardInterrupt:
                print("\nCommand not found")


if __name__ == "__main__":
    main()