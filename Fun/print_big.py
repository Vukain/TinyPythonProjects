def print_bigw(word):
    patterns = {1: '  *  ', 2: ' * * ', 3: '*   *', 4: '*****', 5: '**** ', 6: '   * ', 7: ' *   ', 8: '*   * ',
                9: '*    ', 10: '*  **'}
    alphabet = {'A': [1, 2, 4, 3, 3], 'B': [5, 3, 5, 3, 5], 'C': [4, 9, 9, 9, 4], 'D': [5, 3, 3, 3, 5],
                'E': [4, 9, 4, 9, 4], 'F': [4, 9, 3, 9, 9], \
                'G': [4, 9, 10, 8, 4], 'H': [8, 8, 4, 8, 8], 'I': [1, 1, 1, 1, 1]}
    for letter in word:
        print('\n')
        for pattern in alphabet[letter.upper()]:
            print(patterns[pattern])

word = input('Enter a word:\n')
print_bigw(word)