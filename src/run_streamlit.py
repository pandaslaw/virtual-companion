import streamlit as st

from src.companion import Companion
from src.config import app_settings
from src.utils import write_response_to_streamlit

if __name__ == "__main__":
    huggingface_api_key = app_settings.HUGGINGFACEHUB_API_TOKEN
    if not huggingface_api_key:
        huggingface_api_key = st.sidebar.text_input(
            "HuggingFace API Key", type="password"
        )

    st.title("⚡️🤠️ Virtual Companion App")

    with st.form("my_form"):
        text = st.text_area(
            "Enter text:",
            "What is the best way to reduce anxiety level?",
        )

        genre = st.radio(
            "Choose companion type",
            ["Romantic companion :smirk:", "Friend :sunglasses:"],
            captions=[
                "Playful and flirty personality.",
                "Supportive and trustable personality.",
            ],
        )

        if genre == "Romantic companion :smirk:":
            companion_character = Companion.ROMANTIC
        else:
            companion_character = Companion.FRIENDLY

        submitted = st.form_submit_button("Submit")
        if not huggingface_api_key.startswith("hf_"):
            st.warning("Please enter your HuggingFace API key!", icon="⚠")

        if submitted and huggingface_api_key.startswith("hf_"):
            write_response_to_streamlit(text, companion_character)
