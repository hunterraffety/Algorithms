f = open('words.txt', 'r')
words = f.read().split("\n")
words = [w.lower() for w in words]
f.close()
anagrams = {}
# GENERATE ALL SETS OF ANAGRAMS
for word in words:
    # convert list to string
    signature = "".join(sorted(word.lower()))
    if signature not in anagrams:
        anagrams[signature] = []
    anagrams[signature].append(word)
def anagrams(word):
    signature = "".join(sorted(word.lower()))
    if signature not in anagrams:
        return []
    else:
        return anagrams[signature]