N = int(input())

words = []
for _ in range(N):
    words.append(input())

words = list(set(words)) # remove duplicate

# sorted_words = sorted(words, key=lambda x: ())

len_word_list = []
for word in words:
    len_word_list.append((len(word), word))

len_word_list.sort()
for len_word, word in len_word_list:
    print(word)