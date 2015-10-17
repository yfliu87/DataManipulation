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

def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    sent_dict = read_sent_file(sent_file)
    print len(sent_dict)
    #sent_score(tweet_file, sent_dict)

if __name__ == '__main__':
    main()
