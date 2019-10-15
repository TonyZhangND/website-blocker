# Website blocker for increased productivity

## Requirements
1. Mac OSX
2. Python 2.7

## Usage

### Block
To block websites, add their urls to the file websites.txt, with one url on each line. Then in Terminal, run 

```
./block
```

This script can be run repeatedly. Each time `./block` is run, the websites that are blocked will be updated to match those in websites.txt.

### Unblock
To unblock, use the Terminal to navigate to the project directory and run 

```
./unblock
```

This unblocks all websites listed in websites.txt. 

It is thus safe to run this repeatedly, even while no websites are being blocked.

### Notes
1. `sudo` permission is required for the script to modify the file `/etc/hosts`, and to refresh the system cache.
2. You may need to restart your browser for changes to take effect.

