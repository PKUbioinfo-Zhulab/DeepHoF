import numpy as np
import os, sys
from keras.models import load_model
import tensorflow as tf
import h5py
import pandas as pd

if __name__ == '__main__':
	
	print('load library labels and scores......')
	library_label_score = h5py.File('./for_pvalue/label_test.mat')
	library_label_score = library_label_score['label_test'][:]
	library_label_score = pd.DataFrame(library_label_score, columns=['plant_label', 'germ_label', 'invertebrate_label', 'vertebrate_label', 'human_label'])

	library_scores = pd.read_csv('./for_pvalue/test_score.txt', header=0, sep='|')
	library_label_score['plant_score'] = library_scores['plant_score']
	library_label_score['germ_score'] = library_scores['germ_score']
	library_label_score['vertebrate_score'] = library_scores['vertebrate_score']
	library_label_score['invertebrate_score'] = library_scores['invertebrate_score']
	library_label_score['human_score'] = library_scores['human_score']
	del library_scores
	print('library loaded')

	print('load test scores and begin to calculate the pvalues......')
	hosts = ['plant', 'germ', 'invertebrate', 'vertebrate', 'human']
	score = pd.read_csv('./tmp/score.txt', header=0, index_col=0)
	plant_p = []
	germ_p = []
	invertebrate_p = []
	vertebrate_p = []
	human_p = []
	predicted_host = []
	for item in score.iterrows():
		item_score = list(item[1].values)

		###------plant pvalue
		library_nonplant_plant_score = library_label_score[library_label_score['plant_label'] == 0][
			'plant_score']
		plant_p.append(float(float(len(list(filter(lambda x: x >= item_score[0], library_nonplant_plant_score)))) / len(library_nonplant_plant_score)))

		###------germ pvalue
		library_nongerm_germ_score = library_label_score[library_label_score['germ_label'] == 0][
			'germ_score']
		germ_p.append(float(float(len(list(filter(lambda x: x >= item_score[1], library_nongerm_germ_score)))) / len(library_nongerm_germ_score)))

		###------invertebrate pvalue
		library_noninvertebrate_invertebrate_score = \
		library_label_score[library_label_score['invertebrate_label'] == 0]['invertebrate_score']
		invertebrate_p.append(float(
			float(len(list(filter(lambda x: x >= item_score[2], library_noninvertebrate_invertebrate_score)))) / len(library_noninvertebrate_invertebrate_score)))

		###------vertebrate pvalue
		library_nonvertebrate_vertebrate_score = \
		library_label_score[library_label_score['vertebrate_label'] == 0]['vertebrate_score']
		vertebrate_p.append(
			float(float(len(list(filter(lambda x: x >= item_score[3], library_nonvertebrate_vertebrate_score)))) / len(library_nonvertebrate_vertebrate_score)))

		###------human pvalue
		library_nonhuman_human_score = library_label_score[library_label_score['human_label'] == 0][
			'human_score']
		human_p.append(float(float(len(list(filter(lambda x: x >= item_score[4], library_nonhuman_human_score)))) / len(library_nonhuman_human_score)))


	score['plant_p'] = plant_p
	score['germ_p'] = germ_p
	score['invertebrate_p'] = invertebrate_p
	score['vertebrate_p'] = vertebrate_p
	score['human_p'] = human_p
	print(score)
	score.to_csv(sys.argv[1], sep='\t')
