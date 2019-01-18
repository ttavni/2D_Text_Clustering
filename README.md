# Document Clustering 

###### Made by Timothy Avni (tavni96) & Peter Simkin (DolphinDance)

We present a way to cluster text documents by stacking features from TFIDF, pretrained word embeddings and text hashing.

We then reduce these dimensions using UMAP and HDBSCAN to produce a 2-D D3.js visualisation.

```python

from TextProcessor.features import text_features
from TextProcessor.reduction import Mapper
from TextProcessor.labeller import automatic_labelling
from TextProcessor.viz import Visualiser

corpus = ### List of Documents
tf = text_features(corpus)
data = Mapper(tf.values, corpus)
mapping = automatic_labelling(data)
Visualiser(mapping,folder='test')
	
```
![Viz](https://i.imgur.com/5BiQlW3.png)