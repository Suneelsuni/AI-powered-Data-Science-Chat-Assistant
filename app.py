import streamlit as st
import google.generativeai as genai

# 🎯 Configure Gemini AI
genai.configure(api_key="AIzaSyBrdSkMThJ0c1gIWVZcydaSHpey8dCO1dQ")

# 🧠 System prompt to keep AI focused on Data Science queries
sys_prompt = (
    "You are a helpful data science tutor. "
    "You must only resolve data science-related queries. "
    "If a user asks something unrelated, politely ask them to stay on topic."
)

# 🚀 Initialize the AI model
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-pro",
    system_instruction=sys_prompt
)

# 🎨 Streamlit UI with enhanced styling
st.title("🤖 AI-powered Data Science Chat Assistant")
st.markdown(
    """
    🎉 **Hello and Welcome!**  
    💡 Need help with **Data Science?** I'm here to assist you!  
    ✍️ Simply type your question below, and I'll provide the best answer.  
    🚫 *I only respond to Data Science-related queries.*  
    """
)

# 🗂️ Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# 💬 Display chat history
for chat in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(f"👤 **You:** {chat['question']}")
    with st.chat_message("assistant"):
        st.write(f"🤖 **AI:** {chat['answer']}")

# 📌 User input box
user_prompt = st.text_area("💡 **Ask Your Data Science Question:**", placeholder="🚀 Type your query here...")

# 🔄 Generate answer button
if st.button("✨ Get Answer"):
    if user_prompt.strip():  # Ensure input is not empty
        # 📝 Prepare conversation history
        conversation = "\n".join([f"User: {msg['question']}\nAI: {msg['answer']}" for msg in st.session_state.chat_history])
        full_prompt = f"{conversation}\nUser: {user_prompt}\nAI:"

        # 🤖 Get response from AI model
        response = model.generate_content(full_prompt)
        answer = response.text if response.text else "⚠️ Sorry, I'm unable to generate an answer right now."

        # 📌 Append to chat history
        st.session_state.chat_history.append({"question": user_prompt, "answer": answer})

        # 🔄 Refresh UI to move input box down
        st.rerun()
    else:
        st.warning("⚠️ Please enter a question before clicking the button.")

# Footer
st.markdown("""
    <div class='footer'style='text-align: center;'>
        Developed by <b>Suneel Gangapuram</b> | Built with ❤️ using Streamlit
    </div>
    """, unsafe_allow_html=True)
