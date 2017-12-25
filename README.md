# Website blocker for increased productivity

## Requirements
1. Mac OSX
2. Python 2.7

## Usage

### Block
To block websites, add them to the list `websites_to_block` in block.py. Then in Terminal, navigate to the directory containing block.py and run 

	sudo python block.py

This script can be run repeatedly. Each time block.py is run, the websites that are blocked will be updated to match those in `websites_to_block` in block.py.

### Unblock
To unblock, use the Terminal to navigate to the directory containing unblock.py and run 

	sudo python unblock.py

This unblocks all blocked websites, if any. 

It is thus safe to run this repeatedly, even while no websites are being blocked.

### Notes
1. `sudo` permission is required for the script to modify the file `/etc/hosts`, and to refresh the system cache.
2. You may need to restart your browser for changes to take effect.

