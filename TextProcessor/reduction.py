import umap
import hdbscan

def Mapper(X, corpus,min_dist = 0.0, n_components = 2, n_neighbors=5):

	u = umap.UMAP(
		n_neighbors=n_neighbors,
		min_dist=min_dist,
		n_components=n_components,
		random_state=42,
	).fit_transform(X)

	labels = hdbscan.HDBSCAN(
		min_samples=4,
		min_cluster_size=4,
	).fit_predict(u)

	X_coords, y_coords = u[:, 0], u[:, 1]
	data = {'X':X_coords,'Y':y_coords,'labels':labels,'corpus':corpus}

	return pd.DataFrame(data)