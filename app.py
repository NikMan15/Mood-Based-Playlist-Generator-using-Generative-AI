from transformers import pipeline, set_seed
import streamlit as st
import re

# Load the model
generator = pipeline("text-generation", model="gpt2")
set_seed(42)

st.title("Mood-Based Playlist Generator 🎶")

mood = st.text_input("Enter a mood (e.g., Happy, Sad, Energetic, Calm):")

if mood:
    st.subheader("Generated Playlist:")
    prompt = f"List 7 fictional song titles for a '{mood}' playlist:\n1."

    output = generator(prompt, max_length=100, num_return_sequences=1, pad_token_id=50256)
    playlist_text = output[0]["generated_text"]

    # Extract only the lines starting with 1., 2., etc.
    song_lines = re.findall(r"\d+\.\s*(.+)", playlist_text)

    # Show cleaned-up list
    for idx, song in enumerate(song_lines[:7], 1):
        st.write(f"{idx}. {song.strip()}")

