import streamlit as st
import requests

st.title("🍩🥐🍰  Phân loại các loại bánh ngọt")

uploaded_file = st.file_uploader("Tải lên ảnh loại bánh ngọt", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Ảnh bạn đã chọn", use_container_width=True)

    if st.button("Dự đoán"):
        files = {
            "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
        }

        try:
            # Thay đổi URL này thành URL của backend API của bạn trên Render
            res = requests.post("https://ten-backend-cua-ban.onrender.com/predict/", files=files)
            if res.status_code == 200:
                result = res.json()
                st.success(f"🎯 Dự đoán: `{result['prediction']}` — 🎯 Độ chính xác: `{result['confidence']}`")
            else:
                st.error(f"❌ Không thể dự đoán. Mã lỗi: {res.status_code}")
        except Exception as e:
            st.error(f"❌ Không thể kết nối tới API. Chi tiết: {e}")