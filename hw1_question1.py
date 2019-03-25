def trifeca(word: str):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    last_letter = 'None'
    last_pair_matched = False
    consecutive_matching_pairs = 0

    for letter in word:
        if last_pair_matched:
            last_pair_matched = False
            last_letter = letter
            continue

        if letter == last_letter:
            last_pair_matched = True
            consecutive_matching_pairs += 1
            
            if consecutive_matching_pairs == 3:
                return True
        else:
            consecutive_matching_pairs = 0
        last_letter = letter 
        
    return False



if __name__ == '__main__':
    # Question 1
    while True:
        word = input('Enter a word to find out if it contains 3 consecutive letter pairs (type exit to close):\n')
        if word == 'exit':
            break
        return_value = trifeca(word)
        print(f"Answer: {return_value}")
