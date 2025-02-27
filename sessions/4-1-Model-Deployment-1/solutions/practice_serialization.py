import onnx
import tensorflow as tf
import tf2onnx
from dummy_model import create_model, train_model

model = create_model()
model = train_model(model)

# 1. save weights
model.save_weights("model.weights.h5")

# 2. save entire model in .keras format
model.save("model.keras")

# 3. export to ONNX
inp_size = 10
spec = (tf.TensorSpec((None, inp_size), tf.float32, name="input"),)
onnx_model, _ = tf2onnx.convert.from_keras(model, input_signature=spec)
onnx.save(onnx_model, "model.onnx")

# check model load
loaded_model = tf.keras.models.load_model("model.keras")
print(loaded_model.summary())

loaded_model.load_weights("model.weights.h5")
