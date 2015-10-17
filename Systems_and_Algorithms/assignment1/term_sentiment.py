import sys
import json

def read_sent(sent_file):
	reader = open(sent_file)
	sent_dict = {}

	for line in reader:
		term, score = line.split('\t')

		if ' ' in term:
			subs = term.split(' ')

			for sub in subs:
				sent_dict[sub] = score
		else:
			sent_dict[term] = score

	reader.close()
	return sent_dict


def parse_tweet(tweet_file, sent_dict):
	reader = open(tweet_file, 'r')

	for line in reader:
		json_line = json.loads(line)

		if json_line.has_key('delete'):
			continue

		text = json_line['text']
		overall, new_words = calculate_overall_sentiment(text.encode('utf-8'), sent_dict)

		for word in new_words:
			sent_dict[word] = float(overall)

	reader.close()

	for word, score in sent_dict.items():
		print str(word) + ' ' + str(float(score))


def calculate_overall_sentiment(text, sent_dict):
	overall = 0.0
	new_words = []

	text = text.lower()
	splitor = [',','.','...','/','!','@','?','$','%','*','&','#','~',':',';','(',')']

	for sp in splitor:
		if sp in text:
			text = text.replace(sp, ' ')

	words = text.split(' ')

	for word in words:
		if not word:
			continue

		if word not in sent_dict:
			new_words.append(word)
		else:
			overall += float(sent_dict[word])

	return overall, new_words


def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    sent_dict = read_sent(sent_file)
    parse_tweet(tweet_file, sent_dict)

if __name__ == '__main__':
    main()
