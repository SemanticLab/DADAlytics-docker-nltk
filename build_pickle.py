
import model
from sklearn.externals import joblib
import itertools


if __name__ == "__main__":   
	corpus_root = "/Users/thisismattmiller/Downloads/gmb-2.2.0/"    

	reader = model.read_gmb_ner(corpus_root)
 
	all_classes = ['O', 'B-per', 'I-per', 'B-gpe', 'I-gpe', 
				   'B-geo', 'I-geo', 'B-org', 'I-org', 'B-tim', 'I-tim',
				   'B-art', 'I-art', 'B-eve', 'I-eve', 'B-nat', 'I-nat']
 
	pa_ner = model.ScikitLearnChunker.train(itertools.islice(reader, 50000), feature_detector=model.ner_features,
												   all_classes=all_classes, batch_size=500, n_iter=5)
	accuracy = pa_ner.score(itertools.islice(reader, 5000))

	model.ScikitLearnChunker.__module__ = "model"
	print ("Accuracy:", accuracy) # 0.970327096314
	joblib.dump(pa_ner, 'chunker.pkl') 
