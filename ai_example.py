import os
# Suppress TensorFlow INFO and WARNING messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

import tensorflow as tf

def simple_tensorflow_operation():
    """
    Performs and prints a simple TensorFlow operation.
    """
    try:
        # Create two constant tensors
        a = tf.constant(5.0)
        b = tf.constant(3.0)

        # Perform an addition
        c = tf.add(a, b)

        print("TensorFlow is imported and working.")
        print(f"Constant a: {a.numpy()}")
        print(f"Constant b: {b.numpy()}")
        print(f"Result of a + b: {c.numpy()}")

        # A slightly more complex operation (e.g., a mini neural network layer)
        # Define a simple sequential model with one dense layer
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(units=1, input_shape=[1], name="SimpleDenseLayer")
        ])
        
        # Initialize weights (optional, for consistent output)
        # For a dense layer with 1 unit and input_shape [1], there will be a kernel and a bias.
        # We can set them to predictable values.
        # model.get_layer("SimpleDenseLayer").set_weights([tf.constant([[2.0]]), tf.constant([1.0])])


        # Provide a sample input
        sample_input = tf.constant([[10.0]])
        output = model(sample_input) # Predict

        print("\n--- Simple Neural Network Layer Example ---")
        print(f"Input to the layer: {sample_input.numpy()}")
        # print(f"Layer weights (kernel and bias): {model.get_layer('SimpleDenseLayer').get_weights()}")
        print(f"Output of the layer: {output.numpy()}")
        print("Note: Actual weights are initialized randomly if not set, so output may vary.")


    except ImportError:
        print("Error: TensorFlow library is not installed.")
    except Exception as e:
        print(f"An error occurred during TensorFlow operations: {e}")

if __name__ == "__main__":
    simple_tensorflow_operation()
