# vulnerable.py
import subprocess

def run_command(cmd):
    subprocess.run(cmd, shell=True)  # This is a vulnerability

