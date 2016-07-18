
word_counts = {}
with open('hamlet.txt', 'r') as f:
    for line in f:
        for word in line.split():
            if word not in word_counts:
                word_counts[word] = 0
            word_counts[word] += 1


word_counts = sorted(word_counts.iteritems(), key=lambda w:w[1], reverse=True)
i = 0
for word, count in word_counts:
    print word, count
    i += 1
    if i == 10:
        break
