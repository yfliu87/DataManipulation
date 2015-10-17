import sys
import codecs

def read_sent_file(sent_file):
	reader = open(sent_file)
	sent_dict = {}

	for line in reader:
		term, score = line.split('\t')
		sent_dict[term] = score

	reader.close()
	return sent_dict


def sent_score(tweet_file, sent_dict):
	import json
	reader = open(tweet_file, 'r')

	for line in reader:
		json_line = json.loads(line)

		if json_line.has_key('delete'):
			print '0.0'
			continue

		text = json_line['text']
		words = text.split(' ')

		score = 0.0
		for word in words:
			if word in sent_dict:
				score += float(sent_dict[word])

		print str(score)


def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    sent_dict = read_sent_file(sent_file)
    sent_score(tweet_file, sent_dict)

if __name__ == '__main__':
    main()
