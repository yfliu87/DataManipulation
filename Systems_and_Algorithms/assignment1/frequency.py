import sys
import json

def parse_tweet(tweet_file):
	reader = open(tweet_file, 'r')

	freq_dict = {}
	splitor = [',','.','...','/','!','@','?','$','%','*','&','#','~',':',';','(',')','\t','\n']

	for line in reader:
		json_line = json.loads(line)

		if json_line.has_key('delete'):
			continue

		text = json_line['text'].lower().encode('utf-8')

		for sp in splitor:
			if sp in text:
				text = text.replace(sp, ' ')

		words = text.split(' ')

		for word in words:
			if not word:
				continue

			if word not in freq_dict:
				freq_dict[word] = 1
			else:
				freq_dict[word] += 1 


	reader.close()
	for word, freq in freq_dict.items():
		print str(word) + ' ' + str(float(freq))


def main():
    tweet_file = sys.argv[1]
    parse_tweet(tweet_file)


if __name__ == '__main__':
	main()