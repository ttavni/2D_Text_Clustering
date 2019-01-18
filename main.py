from TeePee.features import text_features
from TeePee.reduction import Mapper
from TeePee.labeller import automatic_labelling
from TeePee.viz import Visualiser
import pandas as pd

if __name__ == "__main__":
	corpus = ### List of Documents
	tf = text_features(corpus)
	data = Mapper(tf.values, corpus)
	mapping = automatic_labelling(data)
	Visualiser(mapping,folder='christmas')


