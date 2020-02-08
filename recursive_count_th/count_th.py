'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    counter = 0
    print(word)
    
    if len(word) <= 1:
        return 0
    else:
        if word[0] == 't' and word[1] == 'h':
            counter+= 1
        print(f"Word: {word}, Count: {counter}")
        return counter + count_th(word[1:])
    
