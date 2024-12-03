from libqtile.command.client import InteractiveCommandClient
from libqtile.lazy import lazy

c = InteractiveCommandClient()

try: 
    print(" > " + c.layout.info().get("name").capitalize())
except:
    print("")

