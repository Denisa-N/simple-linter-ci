import subprocess
import os

def run_command():
cmd = os.environ.get("VULN_CMD")  # User-controlled input
    subprocess.run(cmd, shell=True)  # This is a vulnerability
