# import streamlit as st
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import numpy as np
# from PIL import Image

# # Load model
# @st.cache_resource
# def load_trained_model():
#     return load_model("MobileNet_RGB-2506.h5")

# model = load_trained_model()

# # Danh sách tên lớp
# class_names = ['donut', 'su kem', 'sừng bò', 'tart trứng']

# # Giao diện
# st.title("🍩🥐🍰 Nhận diện các loại bánh ngọt")
# st.write("Tải ảnh lên để mô hình phân loại.")

# uploaded_file = st.file_uploader("Tải ảnh lên", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     img = Image.open(uploaded_file).convert("RGB")
#     st.image(img, caption="Ảnh đầu vào", use_container_width=True)

#     # Resize đúng kích thước mô hình yêu cầu
#     img_resized = img.resize((150, 150))
#     img_array = image.img_to_array(img_resized)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array = img_array / 255.0

#     # Dự đoán
#     prediction = model.predict(img_array)

#     # Lấy kết quả dự đoán
#     pred_index = np.argmax(prediction)
#     confidence = float(np.max(prediction)) * 100
#     pred_class = class_names[pred_index]

#     # Hiển thị
#     st.subheader("Kết quả dự đoán:")
#     st.success(f"{pred_class} ({confidence:.2f}%)")


import streamlit as st
import requests

st.title("🍩🥐🍰  Phân loại các loại bánh ngọt")

uploaded_file = st.file_uploader("Tải lên ảnh loại bánh ngọt", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Ảnh bạn đã chọn", use_container_width=True)

    if st.button("Dự đoán"):
        files = {"file": uploaded_file.getvalue()}
        res = requests.post("http://127.0.0.1:8000/predict/", files=files)

        if res.status_code == 200:
            result = res.json()
            st.success(f"🎯 Dự đoán: `{result['prediction']}` — 🎯 Độ chính xác: `{result['confidence']}`")
        else:
            st.error("❌ Không thể dự đoán. Kiểm tra lại API.")
