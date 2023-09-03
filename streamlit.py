import streamlit as st
from python_algo import main as python_main
from sumy_lib_based_summary import main as sumy_main


if __name__ == "__main__":
    st.runtime.legacy_caching.clear_cache()
    st.set_page_config(layout="wide")
    st.title("Text Summarization ✍️")
    with st.expander("About this app"):
        st.write(
            "This app is designed to showcase text summarization using various techniques. You can select the model, and a text summary will be generated at the bottom"
        )
    st.sidebar.header("Select a model from the list 👇🏻:")
    model_selection = st.sidebar.selectbox(
        "Choose a model",
        [
            "",
            "Core Python algo(Frequency and Ranking based)",
            "Lax Rank: From Python lib sumy",
            "LSA: From Python lib sumy",
            "Text Rank: From Python lib sumy",
        ],
    )
    st.info('Hit: Ctrl + Enter to get summary', icon="ℹ️")
    text_to_summarize = st.text_area("Enter your text to summarize")
    no_of_sentence_on_output = st.number_input('No. of sentences on output you want', min_value=2, max_value=100)
    st.write("Selected Model: ", model_selection)
    summary = st.write("Summary:")
    if model_selection != "" and text_to_summarize != "" and no_of_sentence_on_output != None:
        if model_selection == "Core Python algo(Frequency and Ranking based)":
            st.write(python_main(text=text_to_summarize, sentence_on_output=no_of_sentence_on_output))
        model_name = model_selection.split(":")[0]
        if model_selection == "Lax Rank: From Python lib sumy":
            st.write(sumy_main(text=text_to_summarize, model_name=model_name, sentence_on_output=no_of_sentence_on_output), )
        if model_selection == "LSA: From Python lib sumy":
            st.write(sumy_main(text=text_to_summarize, model_name=model_name, sentence_on_output=no_of_sentence_on_output))
        if model_selection == "Text Rank: From Python lib sumy":
            st.write(sumy_main(text=text_to_summarize, model_name=model_name, sentence_on_output=no_of_sentence_on_output))
