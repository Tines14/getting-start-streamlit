import streamlit as st

st.title("Hello Hexagon")
st.write("Welcome to the Hexagon app built with Streamlit!")

# Initialize state
if "show_text" not in st.session_state:
    st.session_state.show_text = False

def toggle_text():
    st.session_state.show_text = not st.session_state.show_text

# Button that toggles the flag
st.button("Show Hexagon", on_click=toggle_text)

# Conditionally display the text
if st.session_state.show_text:
    st.write("""
    ```plaintext
        _______
       /       \\
      /         \\
     /           \\
     \           /
      \         /
       \_______/
    ```
    """)


st.write("อะไรเอ่ย? อยู่ในรู")
# Initialize state
if "show_text" not in st.session_state:
    st.session_state.show_text = False

def toggle_text():
    st.session_state.show_text = not st.session_state.show_text

# Button that toggles the flag
st.button("เฉลย", on_click=toggle_text)

# Conditionally display the text
if st.session_state.show_text:
    st.write("ปูนาขาเกตัวใหญ่สะไม่มี.")
    import streamlit as st

    # From a local file
    st.image("puthai.jpg", caption="Sunrise by the mountains")  # local path [[st.image](https://docs.streamlit.io/develop/api-reference/media/st.image)]

    # From a URL
    #st.image("https://example.com/myimage.jpg")  # URL [[Media elements](https://docs.streamlit.io/develop/api-reference/media)]

