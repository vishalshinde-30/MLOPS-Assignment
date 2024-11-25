import streamlit as st
from textblob import TextBlob

# Set up the page configuration
st.set_page_config(
    page_title="Sentiment Analysis App",
    page_icon="😊",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom styles
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    .report {
        color: #2e7d32;
        font-size: 16px;
        font-weight: bold;
    }
    .header {
        font-family: 'Arial Black', sans-serif;
        color: #673ab7;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App title
st.markdown("<h1 class='header'>Sentiment Analysis App 🌟</h1>", unsafe_allow_html=True)

# App description
st.markdown(
    """
    This application analyzes the sentiment of your input text and provides additional insights like **subjectivity** 
    and **word count**. Customize your experience using the sidebar!
    """
)

# Sidebar customization
st.sidebar.title("Customize App")
bg_color = st.sidebar.color_picker("Pick a background color", "#f5f5f5")
font_color = st.sidebar.color_picker("Pick a font color", "#000000")

# Apply custom styles dynamically
st.markdown(
    f"""
    <style>
    .main {{
        background-color: {bg_color};
    }}
    body {{
        color: {font_color};
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# User input
user_input = st.text_area("Enter your text below:", height=150, max_chars=500)

# Perform sentiment analysis
if user_input:
    # Analyze sentiment
    analysis = TextBlob(user_input)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity
    word_count = len(user_input.split())

    # Display sentiment
    st.subheader("Sentiment Results:")
    if polarity > 0:
        st.success("The sentiment is **Positive** 😊")
    elif polarity < 0:
        st.error("The sentiment is **Negative** 😠")
    else:
        st.info("The sentiment is **Neutral** 😐")

    # Additional insights
    st.subheader("Text Insights:")
    st.write(f"- **Polarity Score:** {polarity:.2f} (scale: -1 to 1)")
    st.write(f"- **Subjectivity Score:** {subjectivity:.2f} (scale: 0 to 1, where 1 is subjective)")
    st.write(f"- **Word Count:** {word_count} words")

    # Highlight keywords
    # st.subheader("Highlighted Keywords:")
    # keywords = [word for word, tag in analysis.tags if tag in ["JJ", "NN"]]
    # if keywords:
    #     st.write(", ".join(keywords))
    # else:
    #     st.write("No significant keywords found.")

    # Emoji analysis
    st.subheader("Emoji-Based Feedback:")
    emoji_feedback = "😊" if polarity > 0 else "😢" if polarity < 0 else "😐"
    st.markdown(f"<h1 style='text-align: center;'>{emoji_feedback}</h1>", unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <hr style="border:1px solid #673ab7">
    <footer style="text-align: center; font-size: 14px;">
        Made with ❤️ using Streamlit | 
        <a href="https://github.com/VedankWakalkar" style="color:#673ab7;">GitHub</a>
    </footer>
    """,
    unsafe_allow_html=True,
)
