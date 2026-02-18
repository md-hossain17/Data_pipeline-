class person:
    first_name = ""
    last_name = ""
    age = 0
    occupation = ""

matti = person()
matti.first_name = "Matti"
matti.last_name = "Meikäläinen"
matti.age = 35
matti.occupation = "it engineer"
print(matti.first_name, matti.age, matti.last_name)