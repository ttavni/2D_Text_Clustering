import tensorflow as tf
import tensorflow_hub as hub
import pandas as pd

module_url = "https://tfhub.dev/google/universal-sentence-encoder-large/3"
embed = hub.Module(module_url)
tf.logging.set_verbosity(tf.logging.ERROR)

def text_features(corpus):
    """ Convert documents to text vector """

    with tf.Session() as session:
        session.run([tf.global_variables_initializer(), tf.tables_initializer()])
        message_embeddings = session.run(embed(messages))
    
    return pd.DataFrame(message_embeddings)
