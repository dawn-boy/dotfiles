try:
    file = open("/sys/class/backlight/amdgpu_bl1/actual_brightness","r");
    contents = file.read()
    print(contents)
except:
    print("")
