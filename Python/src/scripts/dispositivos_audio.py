import sounddevice

print(sounddevice.query_devices())
print("\n")
print("Input: " + str(sounddevice.check_input_settings()))
print("\n")
print("Output: " + str(sounddevice.check_output_settings()))
