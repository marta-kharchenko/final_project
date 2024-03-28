# Greetings
def Greetings():
    print("Welcome to the best helper to choose the most suitable present for any person!")
    print("What is your name?")
    Name = input()
    print("Nice to meet you,", Name, "\b! \nNow, let's start our process of choosing the perfect gift) "
                                     "\nI will ask you questions to better understand what will suit you.")
    return Name


# Name
def Get_Receiver_Name():
    print(" ""\n1. What is the present receiver name?")
    Receiver_Name = input()
    print("Great!")
    return Receiver_Name


# Age
def Get_Age(Receiver_Name):
    print(" ""\n2. Do you know", Receiver_Name, "\b's age? (Yes/No)")
    Answer_Age = input()
    if Answer_Age.lower() == "yes":
        print("Great! Please enter the age of the present receiver.")
        Age = int(input())
    elif Answer_Age.lower() == "no":
        print("It's not a problem, another information will be more helpful)")
        Age = 35
    else:
        print("Sorry, I didn't understand your answer. Still, let's move on.")
        Age = 35
    return Age


# Age Group
def Get_Age_Group(Age):
    if Age >= 60:
        Age_Group = 4
    elif Age >= 30:
        Age_Group = 3
    elif Age >= 20:
        Age_Group = 2
    elif Age >= 10:
        Age_Group = 1
    elif Age >= 0:
        Age_Group = 0
    return Age_Group


# Relation to this person
def Get_Relation_Importance(Receiver_Name):
    print(" ""\n3. What is the relation between you and", Receiver_Name, "?"
             "\nChoose the most suitable variant for you: family, friend, best friend, college, familiar.")
    Relation = input()
    match Relation:
        case "family":
            Importance = 5
        case "best friend":
            Importance = 4
        case "friend":
            Importance = 3
        case "college":
            Importance = 2
        case "familiar":
            Importance = 1
    print("Now, I understand better.")
    return Relation, Importance


# Hobby
def Get_Hobby(Receiver_Name):
    print(" ""\n4. Do you know any of", Receiver_Name, "\b's hobby or passion? (Yes/No)")
    Answer_Hobby = input()
    if Answer_Hobby.lower() == "yes":
        print(
            "Great! Choose the most nearest variant to yours: art, sport, reading, films, cooking, traveling, or other")
        Hobby = input()
    elif Answer_Hobby.lower() == "no":
        print("Okay, we'll choose great present anyway)")
        Hobby = "other"
    else:
        print("Sorry, I didn't understand your answer. Still, let's move on.")
        Hobby = "other"
    return Hobby


# Present's lists

# Art
Art_Group_1 = ["scratch book", "scratch book & highlighters", "merch cloth with favourite piece of art",
               " art master class certificate", "master class certificate & art supplies"]
Art_Group_2 = ["scratch book & pens", "book about specific type of art", "certificate to the art shop",
               "limited edition book about art", "master class certificate & books about art"]
Art_Group_3 = ["scratch book & markers", "certificate to the art shop", "certificate to the art exhibition",
               "art master class certificate", "certificate to the art courses"]
Art_Group_4 = ["coloring page & paints", "scratch book & colour pencils", "book about specific art, or artists",
               "certificate to the art shop", "certificate to the favourite artist's exhibition"]

# Sport
Sport_Group_1 = ["T-shirt", "sport ball", "healthy sneks & T-shirt", "sport equipment", "swedish wall"]
Sport_Group_2 = ["healthy sneks", "t-shirt", "bag for sport wear", "sport hoodie", "sport sneakers"]
Sport_Group_3 = ["sport hoodie", "book about favourite sports", "sport costume", "ticket to the sport competition",
                 "exercise machine"]
Sport_Group_4 = ["healthy sneks & T-shirt", "book about sport stars", "certificate to the sport lecture",
                 "certificate to the sport store", "ticket to the sport competition & merch"]

# Reading
Reading_Group_1 = ["book-making kit", "bookish board game", "book-inspired clothing",
                   "subscription to a literature podcast", "e-book"]
Reading_Group_2 = ["diary", "reading light", "book series", "limited edition book series", "writing workshop"]
Reading_Group_3 = ["highlights & stickers", "detective book", "bookmarks", "favourite book series",
                   "book club membership"]
Reading_Group_4 = ["book journal", "book-inspired clothing", "reading tracker", "certificate to the book store",
                   "e-book"]

# Films
Films_Group_1 = ["movie-themed puzzle", "movie-themed board games", "merch with favourite film", "director's chair"]
Films_Group_2 = ["filmography journal", "film history books", "certificate to the cinematography lecture",
                 "subscription to movie club membership", "virtual reality headset"]
Films_Group_3 = ["movie night basket", "filmography diary", "cinema gift card", "certificate to the film workshop",
                 "tickets to the film festival"]
Films_Group_4 = ["book about cinematography", "tickets to the cinema", "personalized movie quote print",
                 "director's cut DVDs", "cinema light box"]

# Cooking
Cooking_Group_1 = ["personalized apron", "kitchen scale", "popular recipy book", "backing kit", "immersion blender"]
Cooking_Group_2 = ["forms for baking", "recipe book", "cooking equipment (whiskers, bowls)",
                   "gift card to the confectionary shop", "tickets to the cooking show"]
Cooking_Group_3 = ["cheese board", "cooking thermometer", "professional knife set",
                   "certificate to the cooking classes", "portable BBQ grill"]
Cooking_Group_4 = ["cooking notebook", "cast iron cookware", "food dehydrator", "subscription to a meal kit service",
                   "indoor herb garden kit"]

# Traveling
Traveling_Group_1 = ["language phrasebook", "travel-friendly board games", "cutlery set", "multi-tool", "headphones"]
Traveling_Group_2 = ["travel gear", "portable hammock", "collapsible backpack", "certificate to the guided tour",
                     "action camera"]
Traveling_Group_3 = ["fordable water bottle", "solar-powered charger", "travel-themed book", "travel wallet",
                     "tickets to any country"]
Traveling_Group_4 = ["travel-sized kit", "compact travel umbrella", "luggage set",
                     "subscription to the travel membership", "tickets to the cruise vacation"]

# Other
Other_Group_1 = ["planner", "sport equipment", "gift card to the shop", "subscription box", "wireless headphones"]
Other_Group_2 = ["accessories", "fitness tracker", "bluetooth speaker", "certificate to the language learning course",
                 "tickets to the favourite music group concert"]
Other_Group_3 = ["home decor", "expensive alcohol", "gardening set", "expensive kitchen gadget",
                 "certificate to the art lecture"]
Other_Group_4 = ["memory keepsake album", "indoor plants", "cooking set", "travel luggage set",
                 "tablet with large screen"]

# Group 0-10 years
Group_0 = ["educational toy", "board game", "T-shirts and shorts", "dream toy", "trip to the amusement park"]


# Choosing the perfect gift

while True:
    Name = Greetings()
    Receiver_Name = Get_Receiver_Name()
    Age = Get_Age(Receiver_Name)
    Relation, Importance = Get_Relation_Importance(Receiver_Name)
    Age_Group = Get_Age_Group(Age)

    if Age >= 10:
        Hobby = Get_Hobby(Receiver_Name)
        match Hobby.lower():
            case "art":
                if Age_Group == 1:
                    Gift = Art_Group_1[Importance - 1]
                elif Age_Group == 2:
                    Gift = Art_Group_2[Importance - 1]
                elif Age_Group == 3:
                    Gift = Art_Group_3[Importance - 1]
                elif Age_Group == 4:
                    Gift = Art_Group_4[Importance - 1]

            case "sport":
                if Age_Group == 1:
                    Gift = Sport_Group_1[Importance - 1]
                elif Age_Group == 2:
                    Gift = Sport_Group_2[Importance - 1]
                elif Age_Group == 3:
                    Gift = Sport_Group_3[Importance - 1]
                elif Age_Group == 4:
                    Gift = Sport_Group_4[Importance - 1]

            case "reading":
                if Age_Group == 1:
                    Gift = Reading_Group_1[Importance - 1]
                elif Age_Group == 2:
                    Gift = Reading_Group_2[Importance - 1]
                elif Age_Group == 3:
                    Gift = Reading_Group_3[Importance - 1]
                elif Age_Group == 4:
                    Gift = Reading_Group_4[Importance - 1]

            case "films":
                if Age_Group == 1:
                    Gift = Films_Group_1[Importance - 1]
                elif Age_Group == 2:
                    Gift = Films_Group_2[Importance - 1]
                elif Age_Group == 3:
                    Gift = Films_Group_3[Importance - 1]
                elif Age_Group == 4:
                    Gift = Films_Group_4[Importance - 1]

            case "cooking":
                if Age_Group == 1:
                    Gift = Cooking_Group_1[Importance - 1]
                elif Age_Group == 2:
                    Gift = Cooking_Group_2[Importance - 1]
                elif Age_Group == 3:
                    Gift = Cooking_Group_3[Importance - 1]
                elif Age_Group == 4:
                    Gift = Cooking_Group_4[Importance - 1]

            case "traveling":
                if Age_Group == 1:
                    Gift = Traveling_Group_1[Importance - 1]
                elif Age_Group == 2:
                    Gift = Traveling_Group_2[Importance - 1]
                elif Age_Group == 3:
                    Gift = Traveling_Group_3[Importance - 1]
                elif Age_Group == 4:
                    Gift = Traveling_Group_4[Importance - 1]

            case "other":
                if Age_Group == 1:
                    Gift = Other_Group_1[Importance - 1]
                elif Age_Group == 2:
                    Gift = Other_Group_2[Importance - 1]
                elif Age_Group == 3:
                    Gift = Other_Group_3[Importance - 1]
                elif Age_Group == 4:
                    Gift = Other_Group_4[Importance - 1]
    else:
        Gift = Group_0[Importance - 1]

    print(" ")
    print("Based on your previous answers, the perfect gift for", Receiver_Name, "is -", Gift, "\b."
          "\nI hope, I have helped you with choosing the gift for", Receiver_Name, "\b:)")

    with open("Info_About_Gift.txt", "w") as file:
        file.write(f"\nReceiver: {Receiver_Name}\nAge: {Age}\nRelation: {Relation}\nHobby: {Hobby}\nGift: {Gift}")

    print(" ")
    print("Do you want to chose one more present? (Yes/No)")
    Answer = input()
    if Answer.lower() != "yes":
        print("Bye!")
        break

