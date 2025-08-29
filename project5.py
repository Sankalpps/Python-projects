import random
subject=[
    "A Boy ",
    "A Girl",
    "A Dog",
    "A Man"
]
action=[
    "is sitting",
    "is Sleeping",
    "is dancing",
    "is kicking"
]
Work=[
    "on a buffelo",
    "on a horse",
    "on a Cat",
    "on a fish"
]
while True:
    subject=random.choice(subject)
    action=random.choice(action)
    Work=random.choice(Work)
    hedline=f"Breaking News:{subject} {action} {Work}"
    print("\n"+hedline)
    user_input=input("\n Do you want to create another one: ").strip().lower()
    if user_input=="no":
        break
print("Thank you for visiting")