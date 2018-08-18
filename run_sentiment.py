# Main wrapper file
# Written by Vera Abaimova

import analyze_sentiment

def run_sentiment(textToAnalyze):
	# Create an analyzer
	sent = SentimentAnalyzer(textToAnalyze)



if __name__ == "__main__":

	# Read in all the text locations
	f = open('file_locs.txt','r')
	texts = []
	for line in f:
		texts.append(line.strip())
	# texts should now be a list of file names of texts

	# Run sentiment analysis on each text
	for text in texts:
		run_sentiment(text)