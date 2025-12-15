import subprocess, os

def run_command():
    cmd = os.environ.get("VULN_CMD")  # user-controlled
    subprocess.run(cmd, shell=True)

run_command()
