amigos = [["clara", 25], [ "sebastian", 19],["sergio", 32],["juan",27]]
amigos.append(["sonia"])
amigos[4].append(1)
for amigo in amigos:
    print("{} edad: {}".format(amigo[0],amigo[1]))
print(amigos)    