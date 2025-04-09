import pickle

with open("C:/Users/Windows/MutlipleDisesasePrediction/saved_models/kidney.pkl", "rb") as f:
    model = pickle.load(f)
    print(type(model))
