import streamlit as st
from webscrape import scrape, extract_body, clean_content, batch_maker

st.title("NLP Web Scraper")
url = st.text_input("Enter a valid website url ...")

if st.button("Scape Site"):
    st.write("Scaping website now...")
    output = scrape(url)
    content = clean_content(extract_body(output))
    st.session_state.dom_content
    print(output)