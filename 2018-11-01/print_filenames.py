import os

filenames = []

for root, dirs, files in os.walk("."):  
    for filename in files:
        print(filename)

# for item in filenames:
	# print(item)