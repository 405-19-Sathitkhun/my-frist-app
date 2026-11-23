import streamlit as st
st.title("แอปพลิเคชั่นคำนวณส่วนลดและVAT 7%")
price = st.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0 , value=0.0)
sale = price * (sale/100)
endprice = price - sale
vat = price * 0.07
ovrprice = endprice + vat
st.header(f"• ราคาและส่วนลด: **{price:.2f}** บาท, **{sale:.2f}** บาท")
st.header(f"• ส่วนลด: {endprice:.2f} บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
st.header(f"• vat7%: {vat:.2f} บาท")
st.divider()
st.write("นายสถิตคุณ ผิวงาม เลขที่19 ม.4/5")
