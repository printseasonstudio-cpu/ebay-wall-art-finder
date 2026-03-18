st.markdown("---")
st.header("🔥 Auto Winning Niche Finder")

keywords = ["krishna wall art", "anime poster", "gym motivation poster", "minimalist wall art", "spiritual wall art"]

if st.button("Find Winning Niches"):
    results = []

    for kw in keywords:
        titles, prices = get_ebay_data(kw)

        if prices:
            avg_price = sum(prices) / len(prices)
            competition = len(titles)

            if competition < 10 and avg_price > 10:
                results.append((kw, competition, round(avg_price,2)))

    if results:
        st.success("🔥 Winning Niches Found")

        for r in results:
            st.write(f"✅ {r[0]} | Competition: {r[1]} | Avg Price: ${r[2]}")
    else:
        st.warning("No strong niches found right now")
