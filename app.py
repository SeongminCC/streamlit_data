import streamlit as st

def main():
    st.title("Main Page")
    st.write("Welcome to the Main Page.")

    user_input = st.text_input("Enter a number:")

    if user_input:
        user_input = int(user_input)
        result = user_input * 2

        if st.button("Double"):
            st.write(result)

if __name__ == '__main__':
    main()
