global bgColors, fgColors
bgColors = ['050300', '08131a', '1c1b23', '1a2428', '192b36', '2e2b2e', '393738', '333a44', '244464', '5a403c', '7b5451', 'b75026', 'dc8c64', 'f9f3e3']
fgColors = ['f9f3e3', 'f9f3e3', 'f9f3e3', 'f9f3e3', 'f9f3e3', 'f9f3e3', 'f9f3e3', 'f9f3e3', 'f9f3e3', 'f9f3e3', 'f9f3e3', 'f9f3e3', '050300', '050300']
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

mod = "mod4"
terminal = guess_terminal()

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key(
        [mod, "shift"],"Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "w", lazy.spawn('python /home/Dew/code/py/wallch.py'), desc="Reloads the walls"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn('bash /home/Dew/.config/polybar/cuts/scripts/launcher.sh'), desc="Spawn a command using a prompt widget"),
    Key([mod],"F4", lazy.spawn('light -U 10')),
    Key([mod],"F5", lazy.spawn('light -A 10')),
    Key([mod], "f", lazy.spawn('firefox')),
    Key([mod], "F2", lazy.spawn('pactl -- set-sink-volume 0 -10%')),
    Key([mod], "F1", lazy.spawn('pactl -- set-sink-mute 0 toggle')),
    Key([mod], 'F3', lazy.spawn('pactl -- set-sink-volume 0 +10%')),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),

            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

widget_defaults = dict(
        font = "MesloLGM Nerd Font Bold",
        fontsize = 11,
        padding = 8,)

args = {
        "border_focus":'FFD95A',
        "border_normal":'000000',
        "border_width":0,
        "margin":18,
        }

layouts = [
    layout.Columns(**args),
    layout.Max(**args),
    layout.Bsp(**args),
    layout.MonadTall(**args),
    layout.MonadWide(**args),
    layout.Tile(**args),
]

screens = [ Screen() ]

#bgColors = ["1e2120","262b2a","303635","3a403f","262b2a",'5f6763',"525a57",'989b97','adafac','cbcdcb']
#bgColors = ["006764","008BA8", "52A1A5", "008BA8", "30DEAB", "013A55", "013A35", "002C39", "000B27", "76424F","502833", "A26E00"]
#bgColors = ['607E62','07130F','071616','1A3B2C','28422B','A5AF87','021216','050B0E','05211D','040807','05110D','020705']

dark = bgColors[0]
light = bgColors[-1]

follow_mouse_focus = False
auto_fullscreen = True
wmname = "LG3D"
