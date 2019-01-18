from TextProcessor.features import text_features
from TextProcessor.reduction import Mapper
from TextProcessor.labeller import automatic_labelling
from TextProcessor.viz import Visualiser

if __name__ == "__main__":
	corpus = ### List of Documents
	tf = text_features(corpus)
	data = Mapper(tf.values, corpus)
	mapping = automatic_labelling(data)
	Visualiser(mapping,folder='christmas')


