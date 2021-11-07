import re

vocab = set()
prefixes = ('#', '@', 'https')

for tweet in open("tweets.txt", "r").readlines():
	_, _, text = tweet.partition(', ')
	terms = text.strip().split()
	terms = [word for word in terms if not word.startswith(prefixes)]
	words = [re.sub(r'\W+', '', word).lower() for word in terms]
	vocab.update(set(words))

print(f"There are '{len(vocab)}' unique words")
