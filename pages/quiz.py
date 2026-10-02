import streamlit as st

st.set_page_config(
    page_title="AI Quiz",
    page_icon="📝",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background:#050912;
    color:white;
}

.title {
    font-size:42px;
    color:#00c6ff;
    font-weight:bold;
}

.quiz {
    padding:30px;
    background:#0b1627;
    border:1px solid #173454;
    border-radius:20px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">📝 AI Quiz</div>',
    unsafe_allow_html=True
)

st.write("Test your programming knowledge.")

questions = [
    {
        "question": "Which language is commonly used for Artificial Intelligence?",
        "options": ["Python", "HTML", "CSS", "SQL"],
        "answer": "Python"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "def"
    },
    {
        "question": "Which data type is used to store a sequence of characters in Python?",
        "options": ["int", "list", "str", "float"],
        "answer": "str"
    },
    {
        "question": "Which Python loop executes as long as a condition is true?",
        "options": ["for", "while", "if", "switch"],
        "answer": "while"
    },
    {
        "question": "Which method is used to add an item to the end of a Python list?",
        "options": ["append()", "add()", "insert()", "extend()"],
        "answer": "append()"
    },
    {
        "question": "Which Java keyword is used to create a class?",
        "options": ["class", "struct", "type", "object"],
        "answer": "class"
    },
    {
        "question": "Which Java access modifier allows a class member to be accessed from anywhere?",
        "options": ["private", "protected", "public", "default"],
        "answer": "public"
    },
    {
        "question": "What is the correct Java entry point for a program?",
        "options": ["main()", "start()", "run()", "init()"],
        "answer": "main()"
    },
    {
        "question": "Which Java collection stores unique elements without duplicates?",
        "options": ["ArrayList", "HashSet", "LinkedList", "Vector"],
        "answer": "HashSet"
    },
    {
        "question": "Which Java operator is used to compare two values for equality?",
        "options": ["=", "==", "!=", ":="],
        "answer": "=="
    },
    {
        "question": "Which C data type is used to store a single character?",
        "options": ["char", "string", "int", "float"],
        "answer": "char"
    },
    {
        "question": "Which C function is used to print output to the screen?",
        "options": ["scan()", "printf()", "input()", "print()"],
        "answer": "printf()"
    },
    {
        "question": "Which symbol is used to end a statement in C?",
        "options": [":", ";", ",", "."],
        "answer": ";"
    },
    {
        "question": "Which C loop is best when the number of iterations is known in advance?",
        "options": ["for", "while", "do-while", "if"],
        "answer": "for"
    },
    {
        "question": "What does the C operator '&&' represent?",
        "options": ["OR", "NOT", "AND", "Assignment"],
        "answer": "AND"
    },
    {
        "question": "Which term describes a computer system that can learn from data?",
        "options": ["Machine Learning", "Compiler", "Database", "Firewall"],
        "answer": "Machine Learning"
    },
    {
        "question": "Which AI concept means the model learns by seeing labeled examples?",
        "options": ["Unsupervised learning", "Supervised learning", "Cloud computing", "Networking"],
        "answer": "Supervised learning"
    },
    {
        "question": "Which library is widely used for machine learning in Python?",
        "options": ["Pandas", "NumPy", "scikit-learn", "Matplotlib"],
        "answer": "scikit-learn"
    },
    {
        "question": "What is the process of training an AI model on data called?",
        "options": ["Compilation", "Model fitting", "Debugging", "Rendering"],
        "answer": "Model fitting"
    },
    {
        "question": "Which AI technique allows a system to make decisions based on patterns in data?",
        "options": ["Arithmetic", "Prediction", "Encryption", "Formatting"],
        "answer": "Prediction"
    }
]

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

if "quiz_completed" not in st.session_state:
    st.session_state.quiz_completed = False


def reset_quiz():
    st.session_state.current_question = 0
    st.session_state.user_answers = {}
    st.session_state.quiz_completed = False


if not st.session_state.quiz_completed:
    current_index = st.session_state.current_question
    current_question = questions[current_index]

    st.markdown(f"""
    <div class="quiz">
    <h3>Question {current_index + 1}</h3>
    <p>{current_question['question']}</p>
    </div>
    """, unsafe_allow_html=True)

    selected_answer = st.session_state.user_answers.get(current_index)
    options = current_question["options"]
    default_index = options.index(selected_answer) if selected_answer in options else 0

    answer = st.radio(
        f"Select your answer for Question {current_index + 1}:",
        options,
        index=default_index,
        key="current_question_answer"
    )
    st.session_state.user_answers[current_index] = answer

    st.caption(f"Question {current_index + 1} of {len(questions)}")

    col1, col2 = st.columns([1, 1])

    if current_index > 0:
        if col1.button("Previous"):
            st.session_state.current_question -= 1
            st.rerun()

    if current_index < len(questions) - 1:
        if col2.button("Next"):
            st.session_state.current_question += 1
            st.rerun()
    else:
        if col2.button("Finish Quiz"):
            score = 0
            for i, item in enumerate(questions):
                if st.session_state.user_answers.get(i) == item["answer"]:
                    score += 1

            st.session_state.quiz_completed = True
            st.session_state.final_score = score
            st.rerun()

else:
    score = st.session_state.final_score
    total_questions = len(questions)

    st.success(f"🎉 You scored {score} out of {total_questions}")

    for index, item in enumerate(questions, start=1):
        selected = st.session_state.user_answers.get(index - 1)
        if selected == item["answer"]:
            st.write(f"✅ Question {index}: Correct")
        else:
            st.write(f"❌ Question {index}: Correct answer is '{item['answer']}'")

    if st.button("Retry Quiz"):
        reset_quiz()
        st.rerun()