
def create_model():
    return None # your model building code
model = create_model()

# save
model.save_weights('model.weights.h5')

# load
model = create_model()
model.load_weights('model.weights.h5')

