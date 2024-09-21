import streamlit as st
from input_processing import preprocess_input
from context_processing import should_enrich_context, search_web
#from openai_interaction import generate_response as generate_response_openai
from cohere_interaction import generate_response as generate_response_cohere

# Sidebar for configuration
st.sidebar.title("Configuration")
response_service = st.sidebar.selectbox("Select the response service", ["OpenAI", "Cohere"])
context_service = st.sidebar.selectbox("Select the context service", ["Google Web Search", "None"])

st.markdown("<h1 style='text-align: center; color: blue;'>Chatbot Interface</h1>", unsafe_allow_html=True)

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

user_input = st.text_area("You:", placeholder="Type your message here...", height=100)

if st.button("Send"):
    if user_input:
        processed_input = preprocess_input(user_input)
        additional_context = None

        if processed_input and context_service == "Google Web Search":
            if should_enrich_context(processed_input):
                additional_context = search_web(processed_input)
                st.write(f"Debug: API Response: {additional_context}")
                if additional_context:
                    processed_input += f" Context: {additional_context}"

        st.session_state['messages'].append({"role": "user", "text": processed_input})

        # Generate response based on the selected service
        if response_service == "OpenAI":
            response = generate_response_openai(processed_input)
        elif response_service == "Cohere":
            response = generate_response_cohere(processed_input)
        else:
            response = "This is a placeholder response."

        st.session_state['messages'].append({"role": "bot", "text": response})
    else:
        st.warning("Your input was invalid. Please try again.")

for message in st.session_state['messages']:
    if message['role'] == 'user':
        st.markdown(f"<div style='text-align: left; color: black;'><b>You:</b> {message['text']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: right; color: green;'><b>Bot:</b> {message['text']}</div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
