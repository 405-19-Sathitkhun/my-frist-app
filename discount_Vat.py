import streamlit as st
st.title("แอปพลิเคชั่นคำนวณส่วนลดและVAT 7%")
price = st.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0 , value=0.0)
sale = st.number_input("กรอกส่วนลด (%):", min_value=0.0 , value=0.0)
sole = price * (sale/100)
endprice = price - sole
vat = price * 0.07
ovrprice = endprice + vat
st.header(f"•ราคาเต็ม (บาท): {price:.2f} บาท")
st.header(f"• ส่วนลดที่ลด (บาท): {sole:.2f} บาท")
st.header(f"• ส่วนลด (%): {endprice:.2f} บาท")
st.header(f"• vat7%: {vat:.2f} บาท")
st.header(f"• ราคาสุทธิ: {ovrprice:.2f} บาท")

st.write("นายสถิตคุณ ผิวงาม เลขที่19 ม.4/5")
