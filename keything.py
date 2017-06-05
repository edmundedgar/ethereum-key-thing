from mnemonic import Mnemonic
from ethereum.utils import privtoaddr, decode_hex, encode_hex
import sys


if len(sys.argv) > 3 or len(sys.argv) < 2:
    action = "usage"
else:
    action = sys.argv[1]
    
if action == "generate":
    print 'Generating a new mnemonic for you. I hope your random number generator is really generating random numbers, if not you will have a bad day.'
    print ''

elif action == "private":
    print 'Restoring from private key'
    words = sys.argv[2]

elif action == "addr":
    print 'Restoring from addr_wordsess mnemonic'

else:
    print 'Usage: '
    print 'python keything.py generate'
    print 'or'
    print 'python keything.py private "your key consisting of a long list of a grand total of four and twenty words from last time you ran this in quotation marks"'
    print 'or'
    print 'python keything.py addr "your address words consisting of only fifteen words"'
    sys.exit(1)

if action == "generate":
    m = Mnemonic('english')
    words = m.generate(256)

if action == "private":
    words = sys.argv[2]

if action in ["generate", "private"]:
    m = Mnemonic('english')
    e = m.to_entropy(words)
    he = encode_hex(e)

    print "Your private key as hex"
    print "0x"+he
    print ""

    print "Your private key as a mnemonic"
    print words
    print ""

    addr = "0x"+encode_hex(privtoaddr(decode_hex(he)))

if action == "addr":
    addr_words = sys.argv[2]
    print "loading address with words %s", (addr_words)
    am = Mnemonic('english')
    amm = am.to_entropy(addr_words)
    addr = "0x"+encode_hex(amm)
    #addr_words = encode_hex(am.to_entropy(amm))

print "Your address, as an address"
print addr
print ""

am = Mnemonic('english')
amm = am.to_mnemonic(decode_hex(addr[2:]))

print "Your address, as a mnemomic"
print amm
print ""
