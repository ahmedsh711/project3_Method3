print("Ahmed")
print("Mohamed")
print("Alaa")
print("omar")
print("youssef")
print("a")
print('b')
print("c")
print("d")
print('e')
print("search")

def search(names, name_to_find):
    for i in range(len(names)):
        if names[i] == name_to_find:
            return i
    return -1 # not found
