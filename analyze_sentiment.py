# Sentiment Analysis
# Written by: Vera Abaimova

from collections import Counter
import string
import matplotlib.pyplot as plt
import numpy as np

EMOTIONS = list(['anger','fear','anticipation','trust','surprise','sadness','joy','disgust','negative','positive'])
#CLASSIFICATIONS = set(['negative','positive'])
STOPWORDS = set(['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'])

class SentimentAnalyzer():

	def __init__(self, textFile):
		# Load in the sentiment lexicon
		f = open("NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt", "r")
		self.lex = []

		# Create tuples for each line in the lexicon
		for line in f:
			self.lex.append((line.strip().split('\t')))
		f.close()

		# Change AssociationFlag from string to int
		self.lex = [(elems[0],elems[1],int(elems[2])) for elems in self.lex]

		# Create counters for emotions and classifications
		# self.emotions will contain both
		self.emotions = Counter(EMOTIONS)
		for elem in self.emotions.elements():
			self.emotions[elem] = 0

		# self.classifications = Counter(CLASSIFICATIONS)
		# for elem in self.classifications.elements():
		# 	self.classifications[elem] = 0

		# Set text file
		self.textFile = textFile

		# ADJUST AS NECESSARY TO SUIT FILE STRUCTURE
		# Format the title
		#self.title = self.textFile[6:-4]

		self.title = self.textFile[0:-4]
		#self.title = "trailin"

		# Format the genre
		#self.genre = "western"

		# Create a total count of words found in the lexicon
		self.wordCount = 0



	def splitWords(self):
		f = open(self.textFile)

		# Actually lines
		words = []

		for word in f.read().lower().strip().split():
			word = word.translate(string.maketrans('',''), string.punctuation)
			words.append(word)
		f.close()

		words = filter(lambda word: word not in STOPWORDS, words)

		#print words
		return words


	def assignValues(self):
		# Acquire the text to work with
		words = self.splitWords()

		# Look up each word in lexicon, apply count to each emotion and classification
		print "Looking through words"
		i = 0
		for word in words:
			#print word
			if any(word == x[0] for x in self.lex):
				#print word
				#print "\t\t\t\t FOUND"
				self.wordCount += 1

				# Get all occurances of the word from the lexicon
				indices = [i for i, x in enumerate(self.lex) if x[0] == word]
				#print word, " ", indices
				
				# if the AssociationFlag is 1, update the emotion and classifier count
				#print "WORD: ", word
				for i in indices:
					em = []
					if self.lex[i][2] == 1:
						em.append(self.lex[i][1])
						
					self.emotions.update(em)
		print self.emotions
		print " WORD COUNT: ", self.wordCount


	def calcRatios(self):
		# Calculate the ratios of emotions to words found in the lexicon

		storedEms = self.emotions.items()
		returnEms = []

		for em, score in storedEms:
			score = float(score) / self.wordCount
			returnEms.append([em,score])

		return returnEms


	def organizeEmotions(self, storedEms):
		# Order the resulting emotional scores in one order
		# So that each text analyzed can be compared to all the others

		# storedEms = self.emotions.items()

		resultEms = [None for _ in range(10)]

		for em in storedEms:
			resultEms[EMOTIONS.index(em[0])] = em
			
		return resultEms


	def logResults(self):
		f = open("fiction_analysis.txt", "a")
		f.write("###\n")
		#f.write(self.genre + " : \n")
		f.write(self.title + "\n\n")

		scores = self.organizeEmotions()

		for em, score in scores:
			f.write('%s %d \n' % (em,score))
			#print '%s: %d' % (em,score)
		f.write("\n\n")
		f.close()


	def graphResults(self, clr):
		# Create the two lists to be graphed

		scores = self.organizeEmotions()

		ems = []
		vals = []

		for em, score in scores:
			ems.append(em)
			vals.append(score)

		print ems

		# Create the x locations for the emotions
		N = 10
		inds = np.arange(N)

		# Set the width
		width = 0.4

		# Plot bar graph
		fig = plt.figure()
		subplot = fig.add_subplot(1,1,1)

		subplot.set_xticks(inds + width/2)
		subplot.set_xticklabels(ems)
		subplot.set_title(self.title)
		subplot.set_ylabel("Sentiment Score")
		subplot.set_xlabel("Emotion")

		subplot.set_ylim(0, max(vals)+10)

		subplot.bar(inds, vals, width, color=clr, alpha=.5)
		plt.show()



# TESTING HERE
# s = SentimentAnalyzer('ch1.txt')
# # for el in s.lex:
# # 	print el
# #s.splitWords()

# print "Created analyzer"
# s.assignValues()
# print "Assigned values"
# #sent.logResults()
# #print "Logged results"
# s.organizeEmotions()