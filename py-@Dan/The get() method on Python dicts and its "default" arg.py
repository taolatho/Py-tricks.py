# The get() method on dicts
# and its "default" argument

name_for_userid = {
    1: "Alice",
    2: "Bob",
    3: "Dilbert",
}


def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")


print(greeting(1))  # Hi Alice!
print(greeting(2))  # Hi Bob!
print(greeting(3))  # Hi Dilbert!
print(greeting(0))  # Hi there!
