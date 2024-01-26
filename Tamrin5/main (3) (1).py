def distance(s, t):
    if s == t:
        return 0
    elif len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    v0 = [None] * (len(t) + 1)
    v1 = [None] * (len(t) + 1)
    for i in range(len(v0)):
        v0[i] = i
    for i in range(len(s)):
        v1[0] = i + 1
        for j in range(len(t)):
            cost = 0 if s[i] == t[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
        for j in range(len(v0)):
            v0[j] = v1[j]
    return v1[len(t)]

def find_closest_words(sentence, target_word, n):
    for word in sentence:
        if distance(word, target_word) <= n:
            print(word)

if __name__ == "__main__":
    n = int(input("Enter the allowed Levenshtein distance: "))
    sentence = input("Enter the sentence: ").split()
    target_word = input("Enter the target word: ")

    find_closest_words(sentence, target_word, n)
