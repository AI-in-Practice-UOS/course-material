import tensorflow as tf

model = None

# save as .keras
model.save('model.keras')

# load
model = tf.keras.models.load_model('model.keras')

