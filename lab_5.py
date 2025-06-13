import streamlit as st
import re

# Đoạn mã từ file core.py
def preprocess_data():
    # Tải và xử lý dữ liệu
    tan_suat = {}
    with open("giao-duc-f.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            spls = line.split(" : ")
            if len(spls) == 2:
                tu = spls[0]
                so_lan_xuat_hien = spls[1]
                tan_suat[tu] = so_lan_xuat_hien
    st.write(tan_suat)  # Hiển thị kết quả xử lý

# Đoạn mã từ file train.py
def process_text():
    file_tho = 'giao-duc.txt'
    with open(file_tho, mode='r', encoding='utf-8') as f:
        noi_dung = f.read()

    # Làm sạch dữ liệu
    noi_dung = noi_dung.lower()

    # Loại bỏ dấu câu
    for dau_cau in ['.', ',', '-', '?', ':']:
        noi_dung = noi_dung.replace(dau_cau, '')

    # Loại bỏ ký tự đặc biệt
    noi_dung = re.sub(r'[.,-?:@#$%^&*()+=_`~!{}]', '', noi_dung)

    # Tách từ và loại bỏ stopwords
    with open('stopwords.txt', mode='r', encoding='utf-8') as f:
        stop_words = [line.rstrip() for line in f]
    
    for word in stop_words:
        noi_dung = noi_dung.replace(word, '')

    # Đếm số lần xuất hiện của mỗi từ
    ds_tu = noi_dung.split(' ')
    tan_suat = {}
    for tu in ds_tu:
        if tu not in tan_suat:
            tan_suat[tu] = 1
        else:
            tan_suat[tu] += 1
    
    st.write(tan_suat)  # Hiển thị kết quả

# Hàm chính Streamlit
def main():
    st.title("Ứng dụng Xử lý Dữ liệu và Huấn Luyện Mô Hình")
    
    st.sidebar.header("Chọn Chức Năng")
    choice = st.sidebar.selectbox("Chọn chức năng", ["Tiền xử lý dữ liệu", "Xử lý văn bản"])

    if choice == "Tiền xử lý dữ liệu":
        st.subheader("Chạy Tiền Xử Lý Dữ Liệu")
        preprocess_data()
    
    elif choice == "Xử lý văn bản":
        st.subheader("Chạy Xử Lý Văn Bản")
        process_text()

if __name__ == "__main__":
    main()
