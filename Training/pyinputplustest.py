import pyinputplus as pyip


response = pyip.inputMenu(['Search', 'Move', 'Delete'], numbered=True)

print(response)
