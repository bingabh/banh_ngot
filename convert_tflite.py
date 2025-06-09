import tensorflow as tf

model = tf.keras.models.load_model("MobileNet_RGB-2506.h5")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
open("model.tflite", "wb").write(tflite_model)
print("Đã chuyển sang model.tflite")
