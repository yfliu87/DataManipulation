import sys
import json


def parse_tweet(tweet_file):
	reader = open(tweet_file, 'r')
	tags = {}

	for line in reader:
		json_line = json.loads(line)

		if json_line.has_key('delete'):
			continue

		entity = json_line['entities']
		hashtags = entity['hashtags']

		for hashtag in hashtags:
			key = hashtag['text'].encode('utf-8')
			#occurrence = len(hashtag['indices'])

			if key not in tags:
				tags[key] = 1 
			else:
				tags[key] += 1 

	reader.close()
	import collections
	sorted_tags = collections.OrderedDict(sorted(tags.items(), key=lambda k:k[1], reverse=True))

	counter = 1
	for key, value in sorted_tags.items():
		print str(key) + ' ' + str(float(value))
		counter += 1

		if counter > 10:
			break



def main():
	tweet_file = sys.argv[1]
	parse_tweet(tweet_file)


if __name__ == '__main__':
	main()