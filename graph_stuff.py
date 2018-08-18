# Graphing ALL THE THINGS
# Written by Vera Abaimova

import analyze_sentiment
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
import numpy as np
import math


def autolabel(rects,subPlot):
	# Attach text labels
	for rect in rects:
		height = rect.get_height()
		subPlot.text(rect.get_x() + rect.get_width()/2., 1.05*height, '%0.3f' % float(height), ha='center', va='bottom')

def graphComps(genre, analyzersList, color):
	# Here is where we will graph stuff

	allScores = []
	for aList in analyzersList:
		scores = aList.calcRatios()
		scores = aList.organizeEmotions(scores)

		print scores

		allScores.append(scores)

	allEms = []
	allVals = []

	for scores in allScores:
		ems = []
		vals = []
		for em, score in scores:
			ems.append(em)
			vals.append(score)
		allEms.append(ems)
		allVals.append(vals)
 
 	maxVal = max(max(allVals[0],allVals[1]))
 	ylim = int(math.ceil(maxVal + .05 * maxVal))
 	#print ylim

	# Create the x locations for the emotions
	N = 10
	inds = np.arange(N)

	# Set the width
	width = 0.35

	# Plot bar graph
	
	ax = plt.subplot(111)
	#ax.set_ylim([0,ylim])

	rects1 = ax.bar(inds, allVals[0], width, color=color, alpha=.3)
	rects2 = ax.bar(inds + width, allVals[1], width, color=color, alpha=.7)

	ax.set_ylabel("Sentiment Score")
	
	ax.set_title(genre + ' sentiment comparison')
	ax.set_xticks(inds + width)
	ax.set_xticklabels(allEms[0])

	# ax.legend((rects1[0], rects2[0]), (analyzersList[0].title, analyzersList[1].title))
	ax.legend((rects1[0], rects2[0]), (analyzersList[0].title, analyzersList[1].title),loc=2)
	# ax.legend((rects1[0], rects2[0]), (analyzersList[0].title, analyzersList[1].title),bbox_to_anchor=(0.,1.02,1.,.102),loc=3,ncol=2,borderaxespad=0.)
	
	
	ax.set_xlabel("Emotion")

	autolabel(rects1,ax)
	autolabel(rects2,ax)

	ax.set_ylim(0, max(vals)+10)

	
	plt.show()



def graph_genre_sentiment(genreToGraph):
	# Walk through the folder and create an analyzer for each text found
	myfiles = [f for f in listdir(genreToGraph) if isfile(join(genreToGraph, f))]
	
	sents = []

	for file in myfiles:
		s = analyze_sentiment.SentimentAnalyzer(genreToGraph + file)
		sents.append(s)
	
	print "Created analyzers"

	# Assign values
	for s in sents:
		s.assignValues()

	# Format genre
	genre = genreToGraph[6:-1]

	# adventure: blue
	# crime_fiction: red
	# fantasy: purple ('#7d26cd')
	# horror: black ('k')
	# humor: yellow
	# science_fiction: green
	# western: orange ('#ff8c00')
	# graphComps(genre, sents, 'b')
	# graphComps(genre, sents, 'b')
	# graphComps(genre, sents, 'r')
	# graphComps(genre, sents, '#7d26cd')
	# graphComps(genre, sents, 'k')
	# graphComps(genre, sents, 'y')
	# graphComps(genre, sents, 'g')
	graphComps(genre, sents, '#ff8c00')
	

if __name__ == "__main__":

	# folder = 'texts/test/'
	# folder = 'texts/adventure/'
	# folder = 'texts/crime_fiction/'
	# folder = 'texts/fantasy/'
	# folder = 'texts/horror/'
	# folder = 'texts/humor/'
	# folder = 'texts/science_fiction/'
	folder = 'texts/western/'

	graph_genre_sentiment(folder)