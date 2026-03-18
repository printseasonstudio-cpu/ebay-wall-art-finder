import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("🔥 eBay Wall Art Finder (Real Data)")

if "saved" not in st.session_state:
    st.session_state.saved = []

mode = st.radio("Choose Mode", ["Trend Search", "Idea Generator"])

# ---------------- REAL EBAY SEARCH ----------------
def get_ebay_data(keyword):
    url = f"https://www.ebay.com/sch/i.html?_nkw={keyword}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.select(".s-item")

    prices = []
    titles = []

    for item in items[:20]:
        title = item.select_one(".s-item__title")
        price = item.select_one(".s-item__price")

        if title and price:
            titles.append(title.text)
            price_text = price.text.replace("$", "").split(" ")[0]
            try:
                prices.append(float(price_text))
            except:
                pass

    return titles, prices

# ---------------- TREND SEARCH ----------------
if mode == "Trend Search":
    keyword = st.text_input("Enter keyword")

    if st.button("Find Real Trends"):
        if keyword:
            titles, prices = get_ebay_data(keyword)

            if prices:
                avg_price = sum(prices) / len(prices)

                st.write(f"📊 Listings analyzed: {len(titles)}")
                st.write(f"💰 Avg Price: ${round(avg_price,2)}")

                if len(titles) > 15:
                    st.error("❌ High Competition")
                elif len(titles) > 8:
                    st.warning("⚠️ Medium Competition")
                else:
                    st.success("🔥 Low Competition (Good Niche)")

                st.subheader("Top Listings")

                for t in titles[:5]:
                    st.write("•", t)

# ---------------- IDEA GENERATOR ----------------
elif mode == "Idea Generator":
    if st.button("Generate Ideas"):
        ideas = [
            "Krishna Minimal Line Art Poster",
            "Dark Gym Motivation Poster",
            "Vintage Paris Travel Poster",
            "Anime Neon Poster",
            "Luxury Gold Abstract Art",
            "Spiritual Mandala Wall Art"
        ]

        for idea in ideas:
            col1, col2 = st.columns([4,1])
            col1.write(idea)
            if col2.button("Save", key=idea):
                st.session_state.saved.append(idea)

# ---------------- SAVED ----------------
st.subheader("Saved Ideas")

for s in st.session_state.saved:
    st.write("✔", s)
