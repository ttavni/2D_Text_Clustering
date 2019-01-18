from pke.unsupervised import TopicRank

def automatic_labelling(df, col='corpus', label_col='labels'):
	mapping = {}

	for label in df[label_col].unique():
			extractor = TopicRank()
			tx = ' '.join(df[df[label_col] == label][col].tolist())

			extractor.load_document(input=tx,language="en",normalization=None)

			# select the keyphrase candidates, for TopicRank the longest sequences of
			# nouns and adjectives
			extractor.candidate_selection(pos={'NOUN', 'PROPN', 'ADJ'})

			# weight the candidates using a random walk. The threshold parameter sets the
			# minimum similarity for clustering, and the method parameter defines the
			# linkage method
			extractor.candidate_weighting(threshold=0.5,
										  method='average')

			# print the n-highest (10) scored candidates
			cluster_labels = ' | '.join(
				[keyphrase for keyphrase, score in extractor.get_n_best(n=10, stemming=True)][0:5])
			mapping[label] = cluster_labels
			print('-' * 30)
			print(cluster_labels)

	df['cluster_name'] = df[label_col].map(mapping)

	return df