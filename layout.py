import subprocess
import os

apps = [
    "kitty spf",
    "kitty btop",
    "kitty -e bash -c 'fastfetch; exec bash'"
]

for app in apps:
    subprocess.Popen(app, shell=True)
