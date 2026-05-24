import pickle

with open("encodings.pickle", "rb") as f:
    data = pickle.load(f)

print("Encoding loaded successfully!")
print(type(data))
print(len(data))
