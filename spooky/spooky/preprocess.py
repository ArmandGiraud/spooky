from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import sklearn


# Transform text into features Data:

def preprocess(dataset, add_frequency = True, tfidf = None, scale_data = False):

	# Lexical features

	
	if tfidf is None:
		print("preprocessing training data... ")
		tfidf = TfidfVectorizer(max_features=3000, ngram_range=(1,2))
		X = tfidf.fit_transform(raw_documents=dataset.text)

	else:
		print("preprocessing test data... ")
		# we pass the object to the preparator if we are at test time
		X = tfidf.transform(dataset.text)


	X = pd.DataFrame(X.toarray() , columns = tfidf.get_feature_names())
	
	# optionnally add additional features

	if add_frequency:
		text_len = dataset.text.apply(lambda x: len(x))
		X["text_len"] = text_len

	if scale_data:
		raise("Not implemented")

	return X, tfidf

print(sklearn.__version__)
print(pd.__version__)