import main
import streamlit as st


st.header("Game Recommendation App")
st.caption("Search")
col1, col2 = st.columns([3, 1])
qury = col1.text_input("", label_visibility="collapsed")
search = col2.button("Search...")
if search:
    st.write("Search Results For ---{}---".format(qury))
    st.write(main.out(main.query(qury)))
    # st.write(main.out())
else:
    st.caption("Input Some Text To Start Searching...")

# st.write(main.out())