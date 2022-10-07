"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for i in range (0, len(items)):
        if i ==0:
            key = str(items[0])
            frequencies[key] = 1
        else:
            if str(items[i]) in frequencies:
                key = str(items[i])
                value = frequencies.get(key)
                frequencies[str(items[i])] = value + 1
            else:
                count = 1
                key = str(items[i])
                frequencies[key] = count

    return frequencies

print (frequencies(['a', 'a', 'b', 'b', 'b', 'c']))

print (frequencies([100, 'Hello', '100', '100', 100]))

print (frequencies([100, "100", 100, "100", 100, "100", "hello", 300, "100", 100, 100, "100", "100", "100", 100]))
