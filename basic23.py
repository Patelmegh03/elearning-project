try:
    file = open("f1.txt", "r").read()
    print("Initial content of f1.txt:\n", file)
except FileNotFoundError:
    print(" File 'f1.txt' not found. Skipping read step.")

data = open("fl.txt", "w")
data.write("Ahmedabad")
data.close()

file = open("fl.txt", "r").read()
print("\nAfter writing:\n", file)

data = open("fl.txt", "a")
data.write("\nSurat")
data.close()

file = open("fl.txt", "r").read()
print("\nAfter appending:\n", file)





