def analyze_text():
    text = input("Enter your text: ").lower()
    punctuation = [".", ",", "!", "?", ";", ":"]
    for mark in punctuation:
        text = text.replace(mark, "")

    words = text.split()  #output is in form of list
    frequency = {}

    for word in words :
        if word in frequency :  # if key in dictionary
            frequency[word] += 1   # updating value
        
        else:
            frequency[word] = 1

    return frequency

def display_frequencies(frequency):
    if not frequency:
        print("No text has been analyzed yet")
        return

    print("\nWord Frequencies:")
    for word,count in frequency.items():
        print(f"{word}: {count}")

def search_word(frequency):
    if not frequency:
        print("No text has been analyzed yet.")
        return
     
    u_word = input("Enter the word you want to search for : ").lower().strip()
    if u_word in frequency:
        print(f"'{u_word}' appears {frequency[u_word]} time(s).")
        
    else:
        print("No such word found")

def most_frequent_word(frequency):
    if not frequency:
        print("No words to analyze.")
        return

    highest_count = 0
    for word,count in frequency.items():
        if count > highest_count :
            highest_count = count
            most_frequent = word

    print(f"Most frequent word: {most_frequent}")
    print(f"Frequency: {highest_count}")

def sort_by_frequency(frequency):
    if not frequency:
        print("No text has been analyzed yet.")
        return

    sorted_words = sorted(
        frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("\nWords Sorted by Frequency:")
    for word, count in sorted_words:
        print(f"{word}: {count}")


def main():
    frequency = {}
    print("\n========== Word Frequency Analyzer ==========")
    print("1. Analyze Text")
    print("2. Search Word")
    print("3. Show All Frequencies")
    print("4. Most Frequent Word")
    print("5. Sort by Frequency")
    print("6. Exit")

while True:
    main()
    try:
        n = int(input("Choose from 1-6: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if n == 1:
        frequency = analyze_text()
        display_frequencies(frequency)

    elif n == 2:
        search_word(frequency)

    elif n == 3:
        display_frequencies(frequency)

    elif n == 4:
        most_frequent_word(frequency)

    elif n == 5:
        sort_by_frequency(frequency)

    elif n == 6:
        print("Exiting the Word Analyzer... Goodbye!")
        break

    else:
        print("Invalid choice. Please choose a number from 1 to 6.")

