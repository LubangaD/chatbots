import streamlit as st

# Set the title of the application with custom styling
st.markdown("<h1 style='text-align: center; color: blue;'>Chatbot Interface</h1>", unsafe_allow_html=True)

# Initialize session state to keep track of the conversation history
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Text area for the user to type their message
user_input = st.text_area("You:", placeholder="Type your message here...", height=100)

# Button to send the message
if st.button("Send"):
    if user_input:
        # Append user message to chat history
        st.session_state['messages'].append({"role": "user", "text": user_input})
        
        # Placeholder response (this will be replaced with the actual chatbot response)
        response = f"This is a placeholder response to: {user_input}"
        
        # Append chatbot response to chat history
        st.session_state['messages'].append({"role": "bot", "text": response})

# Display the chat history
for message in st.session_state['messages']:
    if message['role'] == 'user':
        st.markdown(f"<div style='text-align: left; color: black;'><b>You:</b> {message['text']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: right; color: green;'><b>Bot:</b> {message['text']}</div>", unsafe_allow_html=True)

# Add some spacing at the bottom
st.markdown("<br><br>", unsafe_allow_html=True)
