import os

directory = os.path.dirname(os.path.realpath(__file__))
files = os.listdir(directory)

for item in files:
    if item.endswith(".mp4"):
        os.remove(os.path.join(directory, item))