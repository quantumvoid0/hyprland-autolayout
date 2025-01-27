This simple program allows you to automatically open select applications into a workspace
This script is still in development (current version is stable). feel free to open issues or contribute code

make sure you have python installed.
In the `layout.py` i have added it to open `superfile` , `fastfetch` and `btop`; you can edit the apps u need to open to ur needs.

## how to make it work?
save `layout.py` into your `~` directory (i.e the home directory) and then add this `bind = $mainMod,1,exec,python layout.py` to your `hyprland.conf`

now when you press your keycode (for example here 1) your layout will open up.

if code is broken or something doesnt seem to work , please open an issue
