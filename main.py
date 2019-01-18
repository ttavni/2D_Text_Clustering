from TeePee.features import text_features
from TeePee.reduction import Mapper
from TeePee.labeller import automatic_labelling
from TeePee.viz import Visualiser
import pandas as pd

corpus = pd.read_csv('data/data.csv')
corpus.dropna(inplace=True)
corpus = [item for sublist in [corpus[col].tolist() for col in corpus.columns] for item in sublist]

tf = text_features(corpus)
data = Mapper(tf.values, corpus)
mapping = automatic_labelling(pd.DataFrame(data))

Visualiser(mapping,folder='christmas')


