import streamlit as st
import re

# Tiền xử lý dữ liệu từ tệp chứa tần suất
def preprocess_data():
    st.write("Vui lòng tải lên tệp `giao-duc-f.txt` có định dạng `từ : số_lần` mỗi dòng.")
    uploaded_file = st.file_uploader("Tải tệp giao-duc-f.txt", type="txt")
    
    if uploaded_file is not None:
        tan_suat = {}
        for line in uploaded_file:
            line = line.decode("utf-8").strip()
            spls = line.split(" : ")
            if len(spls) == 2:
                tu = spls[0]
                so_lan_xuat_hien = spls[1]
                tan_suat[tu] = so_lan_xuat_hien
        st.write("Kết quả tiền xử lý:")
        st.write(tan_suat)

# Xử lý nội dung thơ và tính tần suất
def process_text():
    st.write("Vui lòng tải lên 2 tệp: `giao-duc.txt` (nội dung văn bản) và `stopwords.txt`.")
    file_tho = st.file_uploader("Tải tệp giao-duc.txt", type="txt", key="tho")
    file_stop = st.file_uploader("Tải tệp stopwords.txt", type="txt", key="stop")
    
    if file_tho is not None and file_stop is not None:
        noi_dung = file_tho.read().decode("utf-8").lower()

        # Làm sạch dấu câu và ký tự đặc biệt
        for dau_cau in ['.', ',', '-', '?', ':']:
            noi_dung = noi_dung.replace(dau_cau, '')
        noi_dung = re.sub(r'[.,-?:@#$%^&*()+=_`~!{}]', '', noi_dung)

        # Tách từ và loại bỏ stopwords
        stop_words = [line.decode("utf-8").strip() for line in file_stop.readlines()]
        for word in stop_words:
            noi_dung = noi_dung.replace(word, '')

        # Tính tần suất
        ds_tu = noi_dung.split()
        tan_suat = {}
        for tu in ds_tu:
            if tu == '':
                continue
            if tu not in tan_suat:
                tan_suat[tu] = 1
            else:
                tan_suat[tu] += 1

        st.write("Tần suất xuất hiện các từ (đã loại bỏ stopwords):")
        st.write(tan_suat)

# Giao diện chính
def main():
    st.title("Ứng dụng Xử lý Dữ liệu Văn Bản")

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
