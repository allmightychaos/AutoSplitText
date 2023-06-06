def split_text():
    # Take input from the user
    num_words = int(input("Enter the number of words before the split: "))

    # Open the text.txt file
    with open('text.txt', 'r') as file:
        words = []
        lines = []

        # Iterate through the file
        for line in file:
            # Split the line into words
            line_words = line.split()

            # Check if the maximum words have been reached
            if len(words) + len(line_words) > num_words:
                # Append the current line to the lines list
                lines.append(' '.join(words))
                words = []

                # Break if three lines have been reached
                if len(lines) == 3:
                    break

            # Add the line words to the words list
            words.extend(line_words)

        # Print the resulting lines
        for line in lines:
            print(line)


# Call the function
split_text()
