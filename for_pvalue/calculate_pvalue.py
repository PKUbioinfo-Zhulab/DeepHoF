import numpy as np
import os, sys
import h5py
import pandas as pd

def calculate_pvalue_process(score, pvalue_outfile):
	print('load library labels and scores......')
	library_label_score = pd.read_csv('./for_pvalue/score_for_calculatepvalue.txt', sep = '\t', header=0, index_col = [0])
	library_label_score = library_label_score[library_label_score['type']=='test']
	print('library loaded')

	print('load test scores and begin to calculate the pvalues......')
	hosts = ['plant', 'germ', 'invertebrate', 'vertebrate', 'human']
	plant_pvalue = []
	germ_pvalue = []
	invertebrate_pvalue = []
	vertebrate_pvalue = []
	human_pvalue = []
	for item in score.iterrows():
		item_score = list(item[1].values)

		###------plant pvalue
		library_nonplant_plant_score = library_label_score[library_label_score['host1'] == 0][
			'plant_score']
		plant_pvalue.append(float(float(len(list(filter(lambda x: x >= item_score[0], library_nonplant_plant_score)))) / len(
			library_nonplant_plant_score)))

		###------germ pvalue
		library_nongerm_germ_score = library_label_score[library_label_score['host2'] == 0][
			'germ_score']
		germ_pvalue.append(float(float(len(list(filter(lambda x: x >= item_score[1], library_nongerm_germ_score)))) / len(
			library_nongerm_germ_score)))

		###------invertebrate pvalue
		library_noninvertebrate_invertebrate_score = \
			library_label_score[library_label_score['host3'] == 0]['invertebrate_score']
		invertebrate_pvalue.append(float(
			float(len(list(filter(lambda x: x >= item_score[2], library_noninvertebrate_invertebrate_score)))) / len(
				library_noninvertebrate_invertebrate_score)))

		###------vertebrate pvalue
		library_nonvertebrate_vertebrate_score = \
			library_label_score[library_label_score['host4'] == 0]['vertebrate_score']
		vertebrate_pvalue.append(
			float(float(len(list(filter(lambda x: x >= item_score[3], library_nonvertebrate_vertebrate_score)))) / len(
				library_nonvertebrate_vertebrate_score)))

		###------human pvalue
		library_nonhuman_human_score = library_label_score[library_label_score['host5'] == 0][
			'human_score']
		human_pvalue.append(float(float(len(list(filter(lambda x: x >= item_score[4], library_nonhuman_human_score)))) / len(
			library_nonhuman_human_score)))

	score['plant_pvalue'] = plant_pvalue
	score['germ_pvalue'] = germ_pvalue
	score['invertebrate_pvalue'] = invertebrate_pvalue
	score['vertebrate_pvalue'] = vertebrate_pvalue
	score['human_pvalue'] = human_pvalue
	print(score)
	score.to_csv(pvalue_outfile, sep='\t')

if __name__ == '__main__':
	score_file = sys.argv[1]
	pvalue_outfile = sys.argv[2]
	score = pd.read_csv(score_file, header=0, sep='\t', index_col = [0])
	calculate_pvalue_process(score, pvalue_outfile)
