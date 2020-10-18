import numpy as np
import os, sys
import keras
from keras.models import load_model
import h5py
import pandas as pd

os.environ["CUDA_VISIBLE_DEVICES"] = "1"


if __name__ == '__main__':
	model = load_model(sys.argv[1])
	print("model built")
	sequence_group = h5py.File(sys.argv[2])
	condon_group = h5py.File(sys.argv[3])
	sequence_group = sequence_group['sequence'][:]
	condon_group = condon_group['codon'][:]
	if "1.mat" in sys.argv[2]:
		sequence_group = sequence_group.reshape(-1, 800, 4)
		condon_group = condon_group.reshape(-1, 798, 64)
		predict = model.predict([sequence_group, condon_group])
		del sequence_group, condon_group
		out_dict = {'plant_score': list(predict[0].reshape(1, -1)[0]), 'germ_score': list(predict[1].reshape(1, -1)[0]),
					'invertebrate_score': list(predict[2].reshape(1, -1)[0]),
					'vertebrate_score': list(predict[3].reshape(1, -1)[0]), 'human_score':list(predict[4].reshape(1, -1)[0])}
		out_df = pd.DataFrame.from_dict(out_dict)
		out_df.to_csv('./tmp/group1_predicts.txt', sep='\t', header=None, index=False)
	else:
		sequence_group = sequence_group.reshape(-1, 1600, 4,)
		condon_group = condon_group.reshape(-1, 1596, 64,)
		predict = model.predict([sequence_group, condon_group])
		del sequence_group, condon_group
		out_dict = {'plant_score': list(predict[0].reshape(1, -1)[0]), 'germ_score': list(predict[1].reshape(1, -1)[0]),
					'invertebrate_score': list(predict[2].reshape(1, -1)[0]),
					'vertebrate_score': list(predict[3].reshape(1, -1)[0]), 'human_score':list(predict[4].reshape(1, -1)[0])}
		out_df = pd.DataFrame.from_dict(out_dict)
		out_df.to_csv('./tmp/group2_predicts.txt', sep='\t', header=None, index=False)
	del predict
	del model

	



