import random
subjects=[
    "Sharuk Khan",
    "Virat Kholi",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "A group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi"
]

actions=[
    "launches",
    "Cancels",
    "dances with",
    "eats",
    "declares wars on",
    "orders",
    "celebrates"
]

places_or_things=[
    "at red fort",
    "in mumbai local train",
    "a plate of samosas",
    "inside parliment",
    "at ganga ghat",
    "during IPL match",
    "at India Gate"
]

while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    places_or_thing=random.choice(places_or_things)

    headline=f"BREAKING NEWS: {subject} {action} {places_or_thing}"
    print("\n" + headline)

    user_input=input("\n Do you want another headline? (yes/no)").strip().lower
    if user_input=="no":
        break

print("\n Thanks for using Fake News Headline Generator. Have a funday.")
