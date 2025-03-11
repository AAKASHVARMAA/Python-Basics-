dict={
    "course":"python",
    "duration":"3 months",
    "venue":"online"
}
print(dict["venue"])
print(dict.keys())
print(dict.items())
print(dict.get("duration"))
dict.update({"projects":3})
print(dict)
del dict["projects"]
print(dict)
