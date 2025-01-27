import subprocess
import os

apps = [
    "kitty spf",
    "kitty -e bash -c 'fastfetch; exec bash'"
]

for app in apps:
    subprocess.Popen(app, shell=True)

os.system('btop')