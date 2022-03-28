# Imagine you have a special keyboard with all keys in a single row. 
# The layout of characters on a keyboard is denoted by a string keyboard of length 26. 
# Initially your finger is at index 0. 
# To type a character, you have to move your finger to the index of the desired character. 
# The time taken to move your finger from index i to index j is abs(j - i).

# Given a string keyboard that describe the keyboard layout and a string text, 
# return an integer denoting the time taken to type string text.

# Input: keyboard = "abcdefghijklmnopqrstuvwxy", text = "cba" 
# Output: 4

def main(text):
    keyboard = 'abcdefghijklmnopqrstuvwxy'
    letters = {}

    for i,l in enumerate(keyboard):
        letters[l] = i

    res = 0

    prev = None
    for c in text:
        if prev == None:
            res += letters[c]
        else:
            res += abs(letters[c] - letters[prev])
        prev = c

    return res

if __name__ == "__main__":
    main()