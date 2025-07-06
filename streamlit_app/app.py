import streamlit as st
import requests

API_URL = "https://your-api-id.execute-api.us-east-1.amazonaws.com"  # Replace later

st.title("💡 AI Content Generator")

keywords = st.text_input("Enter keywords or short description:")

if st.button("Generate"):
    res = requests.post(f"{API_URL}/generate", json={"keywords": keywords})
    if res.status_code == 200:
        output = res.json()["generated"]
        st.success(output)
    else:
        st.error("Failed to generate content.")

if st.button("Show History"):
    res = requests.get(f"{API_URL}/history")
    if res.status_code == 200:
        for item in res.json()["items"]:
            st.write(f"🕒 {item['Timestamp']}")
            st.write(f"🔑 {item['InputKeywords']}")
            st.write(f"📝 {item['GeneratedContent']}")
            st.markdown("---")