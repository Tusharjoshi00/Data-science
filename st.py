#streamlit
#pip install streamlit
#python lib

import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
import time


##page configuration 
st.set_page_config(
    page_title="streamlit function demo",
    page_icon="😎",
    layout="centered"
)

st.title("hello world")
st.header("1. Text element")
st.subheader("markdown,code,latex")
st.markdown("**bold text**,*italic text*,`code`text")
st.code("print('hello eyeryone')",language="python")
st.latex(r"a^2+b^2=c^2")

st.divider()

##metrices and messages
st.header("2. metrices and messages")
st.metric(label="Revenue",value=1234,delta="+10%",delta_color="inverse")
st.error("thisis an error message")
st.warning("this is an warning message")
st.info("this is an info message")
st.success('this is an success message')
st.exception(ValueError("this is an exception message"))

##data display
st.header("3. data display")
df=pd.DataFrame(np.random.randn(10,2),columns=["a","b"])
st.dataframe(df)
st.table(df.head(3))
st.json(df.to_dict())

st.divider()

#charts st.header("3. Charts")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
chart= alt.Chart(df.reset_index()).mark_line().encode(x="index",y="a")
st.altair_chart(chart,use_container_width=True)
fig , ax = plt.subplots()
ax.plot(df.index,df.a)
st.pyplot(fig)
st.divider()


#widgets
st.header('5. widgets')
with st.form('Input form'):
    name = st.text_input("enter your name", type ="password")
    age=st.number_input("enter your age")
    mood = st.radio("select your mood",("happy","sad","neutral"))
    lamguages = st.multiselect("select your languages",("English ","french"))
    submit = st.form_submit_button("submit")
    if submit : 
        st.success(f"Name ; {name}, Age : {int(age)}, Mood : {mood}, Languages :{languages}")

col1 , col2, col3 = st.columns([4,1,1]) ##form ki positioning ko set karne k liye usey column me divide kr dia
with col1:
    st.text("NAME")
    age = st.number_input("AGE")
with col2 :
    st.radio("select your mood",("happy","sad","neutral"))
    st.multiselect("select your languages",("English ","french"))
with col3 :
    st.title("output")

# with st.form("input form"):
#     with col1 , col2 = st.columns(2) 

col1 , col2 = st.columns(2)
with col1:
    number = st.slider("select a number", 0,100)
with col2:
    colour =st.color_picker("select a color","#375FA8")

st.text_area("enter your message")
st.date_input("Select a date")
st.time_input("Enter the time")
st.file_uploader("upload a file")
st.divider()

##media
st.header("6. media")
st.image(r"C:\Users\Dell\Desktop\celebal assignment\Continental GT650.jpeg")
# st.video(r"C:\Users\Dell\Desktop\celebal assignment\bb3058c5-59a8-4d77-beb0-591c94a43b64.gif")
# st.audio()


#slider and layout
st.sidebar.header("sidebar header")
st.sidebar.write("this is a sidebar text")
st.sidebar.button("click me")
option = st.sidebar.selectbox("select an option ",("option 1", "option 2", "option 3"))

##
# tab1, tab2 , tab3 =st.tabs(["tab1 ","tab2","tab3"])

##container
with st.container():
    st.write("this ia a container") #isse kya hai ki error ek conatiner  me aati hai
with st.expander("this is a expendar"):
    st.write("this is a extener")

with st.spinner("loading data. . ."):
    time.sleep(10)
st.success("data loaded")
st.toast("toast message",icon="💕")

st.page_link("https://streamlit.io",label ="streamlit website",icon="👌")