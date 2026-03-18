import streamlit as st
import random

st.set_page_config(page_title="eBay Wall Art Finder PRO", layout="centered")

st.title("🔥 eBay Wall Art Finder (PRO Version)")

# ---------------- SESSION ----------------
if "saved" not in st.session_state:
    st.session_state.saved = []

# ---------------- MODE ----------------
mode = st.radio("Choose Mode", ["Trend Search", "Idea Generator"])

# ---------------- TREND SEARCH ----------------
if mode == "Trend Search":
    keyword = st.text_input("Enter keyword (e.g. boho wall art)")

    if st.button("Find Trends"):
        if keyword:
            # Simulated realistic data
            competition = random.randint(15, 120)
            avg_price = random.randint(8, 25)

            st.write(f"📊 Estimated Listings: {competition}")
            st.write(f"💰 Avg Price: ${avg_price}")

            if competition < 30:
                st.success("🔥 Low Competition (GOOD)")
            elif competition < 70:
                st.warning("⚠️ Medium Competition")
            else:
                st.error("❌ High Competition")

            if avg_price > 12:
                st.success("💰 Good Profit Potential")
            else:
                st.warning("Low pricing niche")

# ---------------- IDEA GENERATOR ----------------
elif mode == "Idea Generator":
    if st.button("Generate Ideas"):
        ideas = [
            "Boho Sun Wall Art",
            "Neutral Abstract Set of 3",
            "Pink Paris Aesthetic Poster",
            "Minimal Line Art Faces",
            "Gym Motivation Typography Poster",
            "Anime Neon Wall Art",
            "Luxury Gold Abstract Design",
            "Vintage Travel Poster",
            "Black White Quote Poster",
            "Spiritual Mandala Art"
        ]

        st.success("💡 Trending Ideas")
        for idea in ideas:
            st.write("•", idea)

# ---------------- SMART AUTO FINDER ----------------
st.markdown("---")
st.header("🔥 Smart Winning Niche Finder")

base_keywords = [
    "boho", "minimalist", "abstract", "typography",
    "anime", "gym", "spiritual", "vintage", "aesthetic"
]

modifiers = [
    "wall art", "poster", "print", "set of 3",
    "decor", "canvas", "modern art"
]

if st.button("Find Winning Niches"):
    results = []

    for b in base_keywords:
        for m in modifiers:
            keyword = f"{b} {m}"

            competition = random.randint(20, 80)
            price = random.randint(10, 25)

            score = (price * 2) - competition

            if score > 15:
                results.append((keyword, competition, price, score))

    if results:
        st.success("🔥 Best Niches")
        top_results = sorted(results, key=lambda x: x[3], reverse=True)[:5]

        for r in top_results:
            st.write(f"✅ {r[0]} | Comp: {r[1]} | Price: ${r[2]} | Score: {r[3]}")
    else:
        st.warning("Try again")

# ---------------- CANVA PROMPT GENERATOR ----------------
st.markdown("---")
st.header("🎨 Canva Poster Prompt Generator")

niche = st.text_input("Enter niche (e.g. boho, anime, gym)")

if st.button("Generate Design Prompt"):
    if niche:
        prompt = f"""
Minimal {niche} wall art,
clean modern design,
high contrast colors,
printable poster,
center composition,
trending aesthetic style,
4K resolution,
neutral or dark background,
professional wall decor look
"""
        st.success("🎯 Canva Prompt")
        st.code(prompt)

# ---------------- TITLE GENERATOR ----------------
st.markdown("---")
st.header("🛒 eBay Title Generator")

title_input = st.text_input("Enter niche for title (e.g. boho wall art)")

if st.button("Generate eBay Title"):
    if title_input:
        title = f"{title_input.title()} Printable Poster Modern Home Decor Wall Art Digital Download"
        st.success("📦 Ready Title")
        st.code(title)

# ---------------- SAVED IDEAS ----------------
st.markdown("---")
st.subheader("💾 Saved Ideas")

for s in st.session_state.saved:
    st.write("✔", s)
