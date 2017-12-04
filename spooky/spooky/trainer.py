from sklearn.linear_model import LogisticRegression
from loader import data_loader
from preprocess import preprocess




def train_model(x_train, y_train):
	print("training...")
	lr = LogisticRegression(C = 0.05)
	lr.fit(x_train, y_train)

	return lr

