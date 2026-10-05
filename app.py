import streamlit as st
import ollama

st.set_page_config(
    page_title="Eco-Bin AI",
    page_icon="♻️",
    layout="centered"
)

st.title("♻️ Eco-Bin AI")
st.subheader("AI-Powered Waste Management System")

st.write("Select a waste type and let AI recommend the correct disposal method.")

waste_type = st.selectbox(
    "🗑️ Select Waste Type",
    [
        "Plastic Bottle",
        "Paper",
        "Cardboard",
        "Glass Bottle",
        "Metal Can",
        "Food Waste",
        "Battery",
        "Electronic Waste"
    ]
)

if st.button("🔍 Analyze Waste"):

    st.info("AI is analyzing the waste...")

    prompt = f"""
You are an environmental waste management assistant.

The detected waste item is:
{waste_type}

Provide the following:

1. Waste Category
2. Recommended Bin
3. Safe Disposal Method
4. Environmental Impact
5. Recycling Recommendation

Give the answer clearly and simply.
"""

    try:
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        st.success("Analysis completed!")

        st.subheader("🌱 AI Recommendation")

        st.write(response["message"]["content"])

    except Exception as e:
        st.error("Ollama connection failed.")
        st.code(str(e))