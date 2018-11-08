import random

words = []
f = input("Enter a file to open: ")
text = open("./" + f)

print("Loading text into memory...")
i = 0
for line in text:
    line = line.replace('\r', ' ').replace('\n', ' ')
    line = line.lower()
    new_words = line.split(' ')
    new_words = [word for word in new_words if word not in ['', ' ']]
    words = words + new_words
    if i % 1000 == 0:
        print("{0} lines processed".format(i))
    i += 1
print('Corpus size: {0} words.'.format(len(words)))

print("Building 1-1 chain...")
chain = {}  
n_words = len(words)  
for i, key in enumerate(words):  
    if n_words > (i + 1):
        word = words[i + 1]
        if key not in chain:
            chain[key] = [word]
        else:
            chain[key].append(word)
print('Chain size: {0} distinct words.'.format(len(chain)))

print("Building 2-1 chain...")
chain2 = {}  
n_words = len(words)  
for i, key1 in enumerate(words):  
    if n_words > i + 2:
        key2 = words[i + 1]
        word = words[i + 2]
        if (key1, key2) not in chain:
            chain2[(key1, key2)] = [word]
        else:
            chain2[(key1, key2)].append(word)

kez = chain2.keys()
while True:
    l = int(input("How long of a text to generate? "))
    c = int(input("How many? "))
    count = 0
    while count < c:
        error = True
        while error == True:
            try:
                w1 = random.choice(words)
                w2 = random.choice(words)
                error = False
            except:
                error = True

        tweet = w1 + ' ' + w2
        last = ""
        while len(tweet) < l:
            ts = tweet.split(' ')
            w1 = ts[len(ts)-2]
            w2 = ts[len(ts)-1]
            ks = []
            for k in kez:
                if k[0] == w1:
                    if k[1] == w2:
                        ks.append(k)
            try:
                w2 = random.choice(chain2[random.choice(ks)])
                if last == w2:
                    w2 = random.choice(chain[w1])
                if w1 == w2:
                    w2 = random.choice(words)
                error = False
                last = w2
            except:
                try:
                    w2 = random.choice(chain[w1])
                except:
                    w2 = random.choice(words)
            tweet += ' ' + w2

        print(tweet)
        print()
        count += 1