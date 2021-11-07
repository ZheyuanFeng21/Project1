import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('--word', type=str)
args = parser.parse_args()

if not args.word:
   raise Exception('Must provide a word')

if len(args.word.split()) > 2:
   raise Exception('Max number of words in a phrase is 2')

prefixes = ('#', '@', 'https')
all_words = []
for tweet in open('tweets.txt','r').readlines():
    _, _, text = tweet.partition(', ')
    terms = text.strip().split()
    terms = [word for word in terms if not word.startswith(prefixes)]
    words = [re.sub(r'\W+', '', word).lower() for word in terms]
    all_words += words
    
count = 0
for i in (range(len(all_words)-1)):
    if len(args.word.split()) > 1:
        if (all_words[i] == args.word.split()[0]) & (all_words[i+1] == args.word.split()[1]):
            count +=1
    else:
        if all_words[i] == args.word:
            count +=1
if all_words[-1] == args.word:
    count +=1

print(f"The phrase '{args.word}' occurs {count} times")
