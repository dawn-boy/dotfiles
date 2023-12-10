libinput-gestures &
syndaemon -i 0.5 &
unclutter --start-hidden --timeout 1 &
python /home/Dew/.github/bonker/bonker.py
picom &
qtile start
