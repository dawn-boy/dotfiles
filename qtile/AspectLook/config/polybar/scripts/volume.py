from pulsectl import Pulse

try:
    pulse = Pulse('client')
    vol = pulse.sink_list()[0].volume.value_flat
    vol = round(vol*100)
    print(vol)
except:
    print("")
