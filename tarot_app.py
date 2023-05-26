import streamlit as st
import openai

# Set up OpenAI API credentials
openai.api_key = "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"

# Define the Tarot spread generation function
def generate_tarot_spread(user_name, situation, focus_area):
    prompt = f"Spread for {user_name}\n\nCurrent situation or question: {situation}\n\nInsights on: {focus_area}\n\nQ: Create fully tarot spread (length more than 3000 symbols) based on provided information"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=4000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        n=1
    )
    return response.choices[0].text.strip()

# Set up the Streamlit web app
def main():
    st.title("Fully Described Tarot Spread Generator")
    st.write("Enter your details and focus area to generate a fully described Tarot spread prediction.")

    # Get user input for name, situation, and focus area
    user_name = st.text_input("Enter your name")
    situation = st.text_input("Enter your current situation or question")
    focus_area = st.selectbox("Select an area to focus on", ["Love", "Career", "Personal Growth", "Other"])

    if st.button("Generate Spread"):
        with st.spinner("Generating Tarot Spread..."):
            tarot_spread = generate_tarot_spread(user_name, situation, focus_area)
            st.success("Tarot Spread Generated!")
            st.write(tarot_spread)

# Run the app
if __name__ == "__main__":
    main()
