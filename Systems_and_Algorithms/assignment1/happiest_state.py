import sys
import json

state_dict = {
		'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }

def read_sent_file(sent_file):
	reader = open(sent_file)
	sent_dict = {}

	for line in reader:
		term, score = line.split('\t')
		sent_dict[term] = score

	reader.close()
	return sent_dict


def convert(state_full):
	for key, value in state_dict.items():
		if state_full == value:
			return key

	return None 

def sent_score(tweet_file, sent_dict):
	import json
	reader = open(tweet_file, 'r')

	state_sentiment = {}

	for line in reader:
		json_line = json.loads(line)

		if json_line.has_key('delete'):
			continue

		place = json_line['place']

		if not place:
			continue

		country = place['country_code']	

		if country and country != 'US':
			continue

		full_name = place['full_name']

		if full_name:
			state = full_name.split(', ')[1]
		else:
			location = json_line['user']['location']
			if location:
				state = location.split(', ')[1]
			else:
				continue

		if len(state) != 2:
			state = convert(state)

		if not state:
			continue

		score = tweet_score(json_line, sent_dict)

		if state in state_sentiment:
			state_sentiment[state] += score
		else:
			state_sentiment[state] = score


	import collections
	sorted_sents = collections.OrderedDict(sorted(state_sentiment.items(), key=lambda k:k[1], reverse=True))
	print str(sorted_sents.keys()[0])


def tweet_score(json_line, sent_dict):
	text = json_line['text']
	words = text.split(' ')

	score = 0.0
	for word in words:
		if word in sent_dict:
			score += float(sent_dict[word])

	return score


def main():
	sentiment_file = sys.argv[1]
	tweet_file = sys.argv[2]
	sent_dict = read_sent_file(sentiment_file)
	sent_score(tweet_file, sent_dict)

if __name__ == '__main__':
	main()