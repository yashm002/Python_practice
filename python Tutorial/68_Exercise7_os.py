import os

files = os.listdir("rough png")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"rough png/{file}", f"rough png/{i}.png")
        i = i + 1