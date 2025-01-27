# hyprland-autolayout
This simple program allows you to automatically open select applications into a workspace
This script is still in development , expect to have bugs. feel free to open issues or contribute code

make sure you have python installed.
In the `layout.py` i have added it to open `superfile` , `fastfetch` and `btop`. (here when btop closes everything else will close) , you can edit the apps u need to open to ur needs.

## how to make it work?
save `layout.py` into your `~` directory (i.e the home directory) and then edit your `~/.bashrc` or `~/.zshrc` and at the end add `alias 1='python layout.py`.

you can replace `1` in alias with whatever call name you want.

now when you open terminal and type `1` and enter , it will open the apps you added in `layout.py`

if code is broken or something doesnt seem to work , please open an issue
