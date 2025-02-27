
import tensorflow as tf
import numpy as np


def create_model() -> tf.keras.Model:
    """Create and compile a simple feedforward neural network model.

    The model consists of:
    - An input layer with 10 features.
    - Three hidden layers with 128, 64, and 32 units respectively, using ReLU activation.
    - An output layer with a single neuron using the sigmoid activation function.

    The model is compiled using the Adam optimizer and binary cross-entropy loss.

    Returns:
        tf.keras.Model: A compiled Keras model.
    """

    # model definition
    inputs = tf.keras.Input(shape=(10,))
    x = tf.keras.layers.Dense(128, activation='relu')(inputs)
    x = tf.keras.layers.Dense(64, activation='relu')(x)
    x = tf.keras.layers.Dense(32, activation='relu')(x)
    outputs = tf.keras.layers.Dense(1, activation='sigmoid')(x)
    model = tf.keras.Model(inputs, outputs)

    # compile model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    return model


def train_model(model: tf.keras.Model) -> tf.keras.Model:
    """Train the given model using randomly generated data.

    Generates a dummy dataset of 100 samples with 10 features each and
    binary labels. The model is trained for 5 epochs with a batch size of 10.

    Args:
        model (tf.keras.Model): The Keras model to be trained.

    Returns:
        tf.keras.Model: The trained Keras model.
    """

    # dummy data
    X: np.ndarray = np.random.rand(100, 10)
    y: np.ndarray = np.random.randint(0, 2, size=(100,))

    # train the model
    model.fit(X, y, epochs=5, batch_size=10)

    return model
