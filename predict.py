import numpy as np
import os, sys
import keras
from keras.models import load_model
import h5py


if __name__ == '__main__':
	model = load_model(sys.argv[1])
	print("model1 built")
	sequence_group = h5py.File(sys.argv[2])
	condon_group = h5py.File(sys.argv[3])
	sequence_group = sequence_group['sequence'][:]
	condon_group = condon_group['codon'][:]
	if "1" in sys.argv[2]:
		sequence_group = sequence_group.reshape(-1, 800, 4)
		condon_group = condon_group.reshape(-1, 798, 64)
		predict = model.predict([sequence_group, condon_group])
		del sequence_group, condon_group
		np.savetxt('./tmp/group1_predict_plants.csv', predict[0])
		np.savetxt('./tmp/group1_predict_germs.csv', predict[1])
		np.savetxt('./tmp/group1_predict_invertebrates.csv', predict[2])
		np.savetxt('./tmp/group1_predict_vertebrates.csv', predict[3])
		np.savetxt('./tmp/group1_predict_human.csv', predict[4])
	else:
		sequence_group = sequence_group.reshape(-1, 1600, 4,)
		condon_group = condon_group.reshape(-1, 1596, 64,)
		predict = model.predict([sequence_group, condon_group])
		del sequence_group, condon_group
		np.savetxt('./tmp/group2_predict_plants.csv', predict[0])
		np.savetxt('./tmp/group2_predict_germs.csv', predict[1])
		np.savetxt('./tmp/group2_predict_invertebrates.csv', predict[2])
		np.savetxt('./tmp/group2_predict_vertebrates.csv', predict[3])
		np.savetxt('./tmp/group2_predict_human.csv', predict[4])
	del predict
	del model
	



