import streamlit as st
st.title("Innomatics Data App")
st.snow()

st.write("My name is Riyaz i am a data Science Enthuasist")

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :cry:")
    st.balloons()