import subprocess

def run_command(cmd):
		subprocess.run(cmd, shell=True)  # This is a vulnerability

run_command("ls -l")  # Example call
