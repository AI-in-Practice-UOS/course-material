import tf2onnx
import onnx
import tensorflow as tf

model = None

inp_size = 10
spec = (tf.TensorSpec((None, inp_size), tf.float32, name="input"),)
onnx_model, _ = tf2onnx.convert.from_keras(model, input_signature=spec)
onnx.save(onnx_model, 'model.onnx')

