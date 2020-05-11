words = input("Say something!\n").lower()

if "hello" in words:
    print("Hello to you!")
elif "how are you" in words:
    print("I am good and what about you?")
elif "I am well, thanks!" in words:
    print("bye")
else:
    print("Huu?")