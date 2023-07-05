# New Print Function
def new_print_cards(cards, hidden):
    s = ""
    for card in cards:
        s += "\t ________________"
    if hidden:
        s += "\t ________________"
    print(s)

    s = ""
    for card in cards:
        s += "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)
    
    s = ""
    for card in cards: #|  {}             |
        if card.num == 10:
            s = s + "\t|  {}            |".format(card.num)
        elif card.num == 11:
            s = s + "\t|  {}             |".format("J")
        elif card.num == 12:
            s = s + "\t|  {}             |".format("Q")
        elif card.num == 13:
            s = s + "\t|  {}             |".format("K")
        elif card.num == 14:
            s = s + "\t|  {}             |".format("A")
        else:
            s = s + "\t|  {}             |".format(card.num)
    if hidden:
        s += "\t|       ***      |"
    print(s)

    s = ""
    for card in cards:
        s += "\t|                |"
    if hidden:
        s += "\t|      *   *     |"
    print(s)

    s = ""
    for card in cards:
        if card.suit == "Spades":
            s += "\t|        .       |"
        elif card.suit == "Hearts":
            s += "\t|       _ _      |"
        elif card.suit == "Clubs":
            s += "\t|        _       |"
        else:
            s += "\t|        ^       |"
    if hidden:
        s += "\t|      *   *     |"
    print(s)


    s = ""
    for card in cards:
        if card.suit == "Spades":
            s += "\t|       /.\      |"
        elif card.suit == "Hearts":
            s += "\t|      ( v )     |"
        elif card.suit == "Clubs":
            s += "\t|       ( )      |"
        else:
            s += "\t|       / \      |"
    if hidden:
        s += "\t|          *     |"
    print(s)

    s = ""
    for card in cards:
        if card.suit == "Spades":
            s += "\t|      (_._)     |"
        elif card.suit == "Hearts":
            s += "\t|       \ /      |"
        elif card.suit == "Clubs":
            s += "\t|      (_'_)     |"
        else:
            s += "\t|       \ /      |"
    if hidden:
        s += "\t|         *      |"
    print(s)

    s = ""
    for card in cards:
        if card.suit == "Spades":
            s += "\t|       _|_      |"
        elif card.suit == "Hearts":
            s += "\t|        .       |"
        elif card.suit == "Clubs":
            s += "\t|        |       |"
        else:
            s += "\t|        .       |"
    if hidden:
        s += "\t|        *       |"
    print(s)
      
    s = ""
    for card in cards:
        s += "\t|                |"
    if hidden:
        s += "\t|        *       |"
    print(s)


    s = ""
    for card in cards:
        s += "\t|                |"
    if hidden:
        s += "\t|                |"        
    print(s)

    s = ""
    for card in cards:
        if card.num == 10:
            s = s + "\t|             {} |".format(card.num)
        elif card.num == 11:
            s = s + "\t|             {}  |".format("J")
        elif card.num == 12:
            s = s + "\t|             {}  |".format("Q")
        elif card.num == 13:
            s = s + "\t|             {}  |".format("K")
        elif card.num == 14:
            s = s + "\t|             {}  |".format("A")
        else:
            s = s + "\t|             {}  |".format(card.num)
    if hidden:
        s += "\t|        *       |"
    print(s)

    s = ""
    for card in cards:
        s = s + "\t|________________|"
    if hidden:
        s += "\t|________________|"
    print(s)

    print()