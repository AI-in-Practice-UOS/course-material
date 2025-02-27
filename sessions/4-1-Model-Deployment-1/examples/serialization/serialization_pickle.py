import pickle

model = None # your model

# save
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

# load
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

