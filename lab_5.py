import streamlit as st
import re

def preprocess_data():
    st.write("Vui lòng tải lên tệp `giao-duc-f.txt`.")

    uploaded_file = st.file_uploader("Chọn tệp giao-duc-f.txt", type="txt", key="file_f")

    if uploaded_file is not None:
        tan_suat = {}
        for line in uploaded_file:
            line = line.decode("utf-8").strip()
            spls = line.split(" : ")
            if len(spls) == 2:
                tu = spls[0]
                so_lan = spls[1]
                tan_suat[tu] = so_lan

        st.subheader("Kết quả tiền xử lý:")
        st.write(tan_suat)

def process_text():
    st.write("Tải lên cả `giao-duc.txt` và `stopwords.txt`.")

    file_tho = st.file_uploader("Tải tệp giao-duc.txt", type="txt", key="tho")
    file_stop = st.file_uploader("Tải tệp stopwords.txt", type="txt", key="stop")

    if file_tho and file_stop:
        noi_dung = file_tho.read().decode("utf-8").lower()

        for dau_cau in ['.', ',', '-', '?', ':']:
            noi_dung = noi_dung.replace(dau_cau, '')
        noi_dung = re.sub(r'[.,-?:@#$%^&*()+=_`~!{}]', '', noi_dung)

        stop_words = [line.decode("utf-8").strip() for line in file_stop.readlines()]
        for word in stop_words:
            noi_dung = noi_dung.replace(f' {word} ', ' ')

        ds_tu = noi_dung.split()
        tan_suat = {}
        for tu in ds_tu:
            if tu:
                tan_suat[tu] = tan_suat.get(tu, 0) + 1

        st.subheader("Tần suất từ sau xử lý:")
        st.write(tan_suat)

def main():
    st.title("Ứng dụng Xử lý Văn Bản")

    st.sidebar.header("Chức Năng")
    choice = st.sidebar.selectbox("Chọn chức năng", ["Tiền xử lý dữ liệu", "Xử lý văn bản"])

    if choice == "Tiền xử lý dữ liệu":
        st.subheader("Tiền Xử Lý Dữ Liệu")
        preprocess_data()
    elif choice == "Xử lý văn bản":
        st.subheader("Xử Lý Văn Bản")
        process_text()

if __name__ == "__main__":
    main()
