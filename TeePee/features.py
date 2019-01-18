## Text Extraction
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer

# Dimensionality Reduction
from sklearn.decomposition import TruncatedSVD

# NLP Tokenization & Cleaning
from nltk.tokenize import word_tokenize
from TeePee.cleaning import clean_text

# Data Handling
import numpy as np
import pandas as pd

# Word2Vec Model
from vecshare import vecshare as vs

def svd(data,dimensions=50):
    """ Function to reduce dimensions using Singular-Value-Decomposition (SVD) """

    svd = TruncatedSVD(n_components=dimensions)
    svd.fit(data.T)
    svd_results = svd.components_.T
    data = pd.DataFrame(svd_results)

    return data

def tfidf_vectors(corpus,n=50):
    """ Function to convert documents to vectors using TFIDF """

    word_tf = TfidfVectorizer()

    word_tfidf_matrix =  word_tf.fit_transform(corpus)

    if word_tfidf_matrix.shape[-1] > 50:
        word_tfidf_matrix = svd(word_tfidf_matrix,n)
    else:
        word_tfidf_matrix = pd.DataFrame(word_tfidf_matrix.toarray())
        pass

    word_tfidf_matrix.columns = [('TFIDF'+str(i)) for i in range(len(word_tfidf_matrix.columns)) ]

    return word_tfidf_matrix

def PretrainedWord2Vec(corpus,embedding_model='text8_emb'):
    """ Convert documents to vector using pretraining embedding models """

    _vec = []
    for row in corpus:

        try:
            sentence_split = word_tokenize(str(row))
            sentence_embedding = vs.query(sentence_split, embedding_model).mean().values
            _vec.append(sentence_embedding)
        except:
            _vec.append(np.zeros(50,))

    word2vec_df = pd.DataFrame(_vec)
    word2vec_df.columns = [('PretrainedWord2Vec'+str(i)) for i in range(len(word2vec_df.columns))]

    return word2vec_df

def text_hashing(corpus,n=50):
    """ Convert documents to vector using text hashing """

    hv = HashingVectorizer(n_features=n)
    h = hv.transform(corpus)
    hashing_df = pd.DataFrame(h.toarray())
    hashing_df.columns = [('HASH'+str(i)) for i in range(len(hashing_df.columns))]

    return hashing_df

def text_features(corpus):
    """ Convert documents to text vector """

    clean_corpus = [clean_text(doc) for doc in corpus]
    tfidf_array = tfidf_vectors(clean_corpus)
    word2vec_df = PretrainedWord2Vec(clean_corpus)
    hash_array = text_hashing(clean_corpus)
    tf = pd.concat([tfidf_array, word2vec_df,hash_array], axis=1)
    tf.fillna(0, inplace=True)
    return tf
