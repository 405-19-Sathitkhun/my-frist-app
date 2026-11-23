import streamlit as st
st.markdown("# :red[คำนวณค่าดัชนีมวลกาย BMI]")
st.write("กรอกน้ำหนักและส่วนสูงของคุณ เพื่อคำนวณหาค่าดัชนีมวลกาย")
weight = st.number_input("กรอกน้ำหนัก (กก.) :", min_value=1.0,  value=1.0)
hieght_cm = st.number_input("กรอกส่วนสูง (ซม.):", min_value=1.0, value=1.0)
if st.bottom("คำนวณค่า BMI"):
   hieght_m = hieght_cm / 100
   bmi = weight / (height_m ** 2)
   st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**" )
   if bmi < 18.5:
     st.warning("คุณน้ำหนักน้อยกว่าเกณฑ์⚠️  (ผอม)")
   elif 18.5 <= bmi < 23.0:
     st.success("คุณมีน้ำหนักตามเกณฑ์🎉  (สุขภาพดี)")
   elif 23.0 <= bmi <25.0:
     st.info("คุณมีน้ำหนักเกินเกณฑ์🥗 (ท้วม)")
   else:
     st.error("คุณอยู่ในเกณฑ์อ้วน ไปออกกำลังกาย🏋️🏃")

st.divider()
st.write("นายสถิตคุณ ผิวงาม ม.4/5 เลขที่19")

     
