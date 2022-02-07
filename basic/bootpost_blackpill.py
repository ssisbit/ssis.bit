import microcontroller

print("This is a Blackpill, running at {:.1f} MHz".format(float(microcontroller.cpu.frequency)/1000000))
print("The CPU has a temperature of {:.1f} °C.".format(microcontroller.cpu.temperature))
