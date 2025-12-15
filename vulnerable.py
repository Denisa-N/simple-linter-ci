import subprocess

def run_command(cmd):
    subprocess.run(cmd, shell=True)  # Vulnerable to shell injection

user_cmd = input("Enter a command: ")
run_command(user_cmd)

