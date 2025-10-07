def recite(start_verse, end_verse):
    ordinals = [
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]

    gifts = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming"
    ]
    verses = []
    for day in range(start_verse -1, end_verse):
        line = f"On the {ordinals[day]} day of Christmas my true love gave to me: "
        gift_lines = gifts[day::-1]
        if day != 0:
            gift_lines[-1] = "and " + gift_lines[-1]
        verse = line + ', '.join(gift_lines)
        verses.append(verse)
    return verses

