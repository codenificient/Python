
def is_matched(expression): 
    mapping = dict(zip('({[', ']})'))
    queue = []

    for letter in expression:
        if letter in mapping:
            queue.append(mapping[letter])
        elif not (queue and letter == queue.pop()):
            return False
        
        return not queue


#         take in a string of symbols
# devide the string of symbols by 2
# compare the first half with the second half to 
