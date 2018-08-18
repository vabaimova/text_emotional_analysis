# Main wrapper test file
# Written by Vera Abaimova

import analyze_sentiment

def run_sentiment(textToAnalyze):
	# Create an analyzer
	sent = analyze_sentiment.SentimentAnalyzer(textToAnalyze)
	print "Created analyzer"
	sent.assignValues()
	print "Assigned values"
	sent.logResults()
	print "Logged results"
	sent.graphResults('#ff8c00')
	print "Graphed results"


if __name__ == "__main__":

	text = 'texts/test/test2.txt'

	#text = 'texts/science_fiction/a_princess_of_mars.txt'
	#text = 'texts/science_fiction/the_eyes_have_it.txt'
	#text = 'whole.txt'

	run_sentiment(text)