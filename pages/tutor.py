import streamlit as st

try:
    import ollama
except Exception:
    ollama = None

st.set_page_config(
    page_title="AI Tutor",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background: #050912;
    color: white;
}

.title {
    font-size: 42px;
    color: #00c6ff;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🤖 AI Smart Tutor</div>',
    unsafe_allow_html=True
)

st.write("Ask questions and learn with your AI-powered tutor.")


def generate_local_answer(question):
    if not question or not question.strip():
        return "Please ask a valid question."

    if ollama is not None:
        try:
            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a friendly AI tutor. Explain in simple, clear, educational language. Answer as a helpful teacher."
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )
            return response["message"]["content"].strip()
        except Exception:
            pass

    q = question.lower().strip()

    if "hello" in q or "hi" in q:
        return "Hello! I am your AI tutor. Ask me anything about programming, Python, Java, C, or AI."

    if "python" in q:
        return "Python is a beginner-friendly programming language used for AI, data science, automation, web development, and scripting. It is popular because its syntax is simple and readable."

    if "java" in q:
        return "Java is an object-oriented programming language used for enterprise applications, Android apps, and backend systems. It is known for its portability and performance."

    if "c" in q and ("language" in q or "program" in q):
        return "C is a low-level programming language used for operating systems, embedded systems, and performance-critical software. It gives developers direct control over memory and hardware."

    if "ai" in q or "artificial intelligence" in q:
        return "Artificial Intelligence (AI) is the field of building machines that can learn, reason, recognize patterns, and solve problems that normally require human intelligence."

    if "machine learning" in q:
        return "Machine Learning is a subset of AI where systems learn patterns from data to make predictions or decisions without being explicitly programmed for every rule."

    if "variable" in q:
        return "A variable is a named storage location that stores data in a program. Example: x = 10 means the variable x stores the value 10."

    if "function" in q:
        return "A function is a reusable block of code that performs a specific task. It helps keep the program organized and avoids repeating code."

    if "loop" in q:
        return "A loop is used to repeat a block of code multiple times. Common examples are for loops and while loops."

    if "class" in q and "object" in q:
        return "A class is a blueprint for creating objects, and an object is a specific instance of that class. Classes define properties and methods."

    if "html" in q:
        return "HTML (HyperText Markup Language) is used to structure the content of a website, such as headings, paragraphs, links, and images."

    if "sql" in q:
        return "SQL is a language used to manage and query databases. It helps you store, update, retrieve, and delete data."

    if "how to learn" in q or "study" in q:
        return "To learn programming well, practice regularly, build small projects, and review examples. Focus on one concept at a time and solve hands-on exercises."

    return (
        "I can help with programming, Python, Java, C, AI, and general computer science topics. "
        "Try asking a question like 'What is Python?', 'Explain loops', or 'What is AI?'."
    )


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask your AI Tutor anything...")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    answer = generate_local_answer(question)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    with st.chat_message("assistant"):
        st.markdown(answer)