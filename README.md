# Simple Key Thing

This is a simple script make Ethereum addresses on an offline computers. You can then export them on a piece of paper, or multiple pieces of paper. We also allow you to export the address in this way.

This is intended to be very simple, without all the key password and formatting bureaucracy found in parity and geth. In general that bureaucracy is there to protect you, so you probably shouldn't be using this.

I made this for myself, I haven't thought very hard about documenting it so that other people can use it without all their stuff getting hacked.

Hopefully you can make a secure key with it, but maybe not, who knows. YMMV, ABSOLUTELY NO WARRANTY etc etc etc.

## Usage

Don't use it. But if you insist, 

`pip install -r requirements.txt`

Then run `python keything.py` to get a list of options.

## Deployment

You can deploy the whole thing (python and libraries) onto a USB stick as follows:

virtualenv --no-site-packages --distribute venv
virtualenv --relocatable venv/
source venv/bin/activate
pip install -r requirements
deactivate
sudo rsync -urL simpleethkeything/ /mnt/usb/simpleethkeything/
