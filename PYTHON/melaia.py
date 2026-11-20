
import re


def build_scripture_dictionary(bom_text):
    """
    Purpose: Create a dictionary containing every Book of Mormon verse.
    Parameters: bom_text - the complete Book of Mormon text as a string.
    Returns: A dictionary with scripture references as keys and verses as values.
    """

    scriptures = {}
    current_book = ""

    book_headings = {
        "THE FIRST BOOK OF NEPHI": "1 Nephi",
        "THE SECOND BOOK OF NEPHI": "2 Nephi",
        "THIRD BOOK OF NEPHI": "3 Nephi",
        "FOURTH BOOK OF NEPHI": "4 Nephi",
        "THE WORDS OF MORMON": "Words of Mormon"
    }

    chapter_pattern = re.compile(r"^.+ Chapter \d+$")
    verse_pattern = re.compile(r"(?<!\S)(\d+):(\d+)\s+")

    for line in bom_text.splitlines():
        line = line.strip()

        # Identify the name of each book.
        if line in book_headings:
            current_book = book_headings[line]
            continue

        elif line.startswith("THE BOOK OF "):
            current_book = line.replace("THE BOOK OF ", "").title()
            continue

        # Skip chapter headings.
        if chapter_pattern.match(line):
            continue

        if current_book:
            matches = list(verse_pattern.finditer(line))

            # Find every verse, including multiple verses on one line.
            for i, match in enumerate(matches):

                if i + 1 < len(matches):
                    end = matches[i + 1].start()
                else:
                    end = len(line)

                chapter = match.group(1)
                verse_number = match.group(2)

                reference = (
                    current_book + " " + chapter + ":" + verse_number
                )

                verse_text = line[match.end():end].strip()

                scriptures[reference] = verse_text

    return scriptures


def find_search_results(search_phrase, scriptures):
    """
    Purpose: Find scriptures containing the requested search phrase.
    Parameters: search_phrase - the user's search;
                scriptures - the scripture dictionary.
    Returns: A list of matching scripture references.
    """

    results = []

    if "&" in search_phrase:
        terms = search_phrase.split("&", 1)
        terms = [term.strip() for term in terms]

        if not all(terms):
            return results

        for reference, verse in scriptures.items():
            if all(term in verse for term in terms):
                results.append(reference)

    elif "|" in search_phrase:
        terms = search_phrase.split("|", 1)
        terms = [term.strip() for term in terms]

        if not all(terms):
            return results

        for reference, verse in scriptures.items():
            if any(term in verse for term in terms):
                results.append(reference)

    else:
        for reference, verse in scriptures.items():
            if search_phrase in verse:
                results.append(reference)

    return results


def prompt_next_action():
    """
    Purpose: Ask the user what they want to do next.
    Parameters: None.
    Returns: A valid action: <, >, n, or x.
    """

    while True:
        action = input(
            "\nPress < for previous, > for next, "
            "n for new search, or x to exit: "
        ).strip().lower()

        # Allow keys that do not require holding Shift.
        if action == ",":
            action = "<"
        elif action == ".":
            action = ">"

        if action in ["<", ">", "n", "x"]:
            return action

        print("Invalid option. Please try again.")


# Read the Book of Mormon text file.
with open("bomscriptures.txt", "r", encoding="utf-8") as file:
    bom_text = file.read()


# Build the scripture dictionary.
scriptures = build_scripture_dictionary(bom_text)

print("Book of Mormon Scripture Search")
print("Total scriptures loaded:", len(scriptures))


# Main program loop.
while True:

    search_phrase = input(
        "\nEnter a name or phrase to search (x to exit): "
    )

    if search_phrase.lower() == "x":
        print("Goodbye!")
        break

    # Find matching scripture references.
    hits = find_search_results(search_phrase, scriptures)

    print("\nNumber of hits:", len(hits))

    if len(hits) == 0:
        print("No matching scriptures found.")
        continue

    current_hit = 0

    # Allow the user to move through the search results.
    while True:

        reference = hits[current_hit]

        print("\n--------------------------------")
        print("Citation:", reference)
        print("Verse:", scriptures[reference])
        print("--------------------------------")

        action = prompt_next_action()

        if action == "x":
            print("Goodbye!")
            exit()

        elif action == "n":
            break

        elif action == "<":
            current_hit = (current_hit - 1) % len(hits)

        elif action == ">":
            current_hit = (current_hit + 1) % len(hits)
