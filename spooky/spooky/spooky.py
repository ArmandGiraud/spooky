
from loader import data_loader
from preprocess import preprocess
from trainer import train_model
import pandas as pd
import os


data_path = "./data/"
output_path = "./output/"

def main():
	"""run the pipeline """
	test, train = data_loader(data_path)
	X_train, tfidf = preprocess(train, True)
	X_test, _ = preprocess(test, tfidf)
	y_train = train.author

	model = train_model(X_train, y_train)

	sub = pd.Series(model.predict(X_test))

	sub.to_csv(os.path.join(output_path,"simple_submission.csv"), index=False)


if __name__ == '__main__':
	main()
