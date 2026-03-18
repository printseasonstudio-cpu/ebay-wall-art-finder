import streamlit as st
import random

st.title("🔥 eBay Wall Art Finder")

if "saved" not in st.session_state:
    st.session_state.saved = []

mode = st.radio("Choose Mode", ["Trend Search", "Idea Generator"])

if mode == "Trend Search":
    keyword = st.text_input("Enter keyword")

    if st.button("Find Trends"):
        demand = random.randint(50, 100)
        competition = random.randint(10, 100)

        st.write("Demand:", demand)
        st.write("Competition:", competition)

        if demand > 70 and competition < 50:
            st.success("🔥 Winning niche")
        elif competition > 70:
            st.error("Too competitive")
        else:
            st.warning("Moderate opportunity")

        ideas = [
            f"{keyword} Minimal Poster",
            f"{keyword} Vintage Poster",
            f"{keyword} Typography Art"
        ]

        for idea in ideas:
            if st.button("Save " + idea):
                st.session_state.saved.append(idea)

if mode == "Idea Generator":
    if st.button("Generate Ideas"):
        ideas = [
            "Krishna Line Art Poster",
            "Gym Motivation Poster",
            "Paris Travel Poster",
            "Anime Neon Poster"
        ]

        for idea in ideas:
            if st.button("Save " + idea):
                st.session_state.saved.append(idea)

st.subheader("Saved Ideas")
for s in st.session_state.saved:
    st.write("✔", s)
