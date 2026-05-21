import streamlit as st
import os

def get_ai_response(question: str, history: list) -> str:
    """Get response from OpenAI or fallback to rule-based answers."""
    try:
        import openai
        api_key = st.session_state.get("openai_key", "")
        if not api_key:
            return rule_based_response(question)
        client = openai.OpenAI(api_key=api_key)
        messages = [
            {"role": "system", "content": (
                "You are AshBot, an expert AI assistant for AshTech AI Portal. "
                "You help users with AI/ML concepts, Data Science, Cloud technologies, "
                "job search advice, interview preparation, and career guidance. "
                "Be concise, helpful, and encouraging."
            )}
        ]
        for h in history[-6:]:
            messages.append({"role": h["role"], "content": h["content"]})
        messages.append({"role": "user", "content": question})
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages, max_tokens=500
        )
        return response.choices[0].message.content
    except Exception:
        return rule_based_response(question)


def rule_based_response(q: str) -> str:
    q = q.lower()
    if any(w in q for w in ["machine learning", "ml"]):
        return ("**Machine Learning** is a subset of AI where systems learn from data.\n\n"
                "**Key types:**\n- Supervised Learning (labeled data)\n"
                "- Unsupervised Learning (unlabeled data)\n- Reinforcement Learning\n\n"
                "**Popular algorithms:** Linear Regression, Decision Trees, Random Forest, SVM, Neural Networks\n\n"
                "Want to know about a specific algorithm?")
    elif any(w in q for w in ["deep learning", "neural network", "cnn", "rnn", "lstm"]):
        return ("**Deep Learning** uses multi-layered neural networks.\n\n"
                "**Key architectures:**\n- CNN (images)\n- RNN/LSTM (sequences/time series)\n"
                "- Transformer (NLP)\n- GAN (generative)\n\n"
                "**Frameworks:** TensorFlow, PyTorch, Keras")
    elif any(w in q for w in ["job", "career", "interview", "resume", "hire"]):
        return ("**Career Tips for AI/ML:**\n\n"
                "1. Build a strong GitHub portfolio\n"
                "2. Work on end-to-end projects (data → model → deployment)\n"
                "3. Learn MLOps (Docker, Kubernetes, CI/CD)\n"
                "4. Practice LeetCode for coding rounds\n"
                "5. Know your ML fundamentals deeply\n\n"
                "Check the **Job Search** tab for current openings!")
    elif any(w in q for w in ["python", "pandas", "numpy", "sklearn"]):
        return ("**Python for Data Science essentials:**\n\n"
                "```python\nimport pandas as pd\nimport numpy as np\n"
                "from sklearn.model_selection import train_test_split\n"
                "from sklearn.ensemble import RandomForestClassifier\n\n"
                "# Load data\ndf = pd.read_csv('data.csv')\nX = df.drop('target', axis=1)\n"
                "y = df['target']\n\n# Split & train\nX_train, X_test, y_train, y_test = "
                "train_test_split(X, y, test_size=0.2)\nmodel = RandomForestClassifier()\n"
                "model.fit(X_train, y_train)\n```")
    elif any(w in q for w in ["gcp", "bigquery", "cloud", "airflow", "terraform"]):
        return ("**GCP & Cloud Data Engineering:**\n\n"
                "- **BigQuery**: Serverless data warehouse for analytics\n"
                "- **Airflow**: Workflow orchestration for data pipelines\n"
                "- **Terraform**: Infrastructure as Code (IaC)\n"
                "- **Tekton**: Kubernetes-native CI/CD pipelines\n\n"
                "These are key skills for Cloud Data Engineering roles at companies like Ford!")
    elif any(w in q for w in ["nlp", "natural language", "bert", "transformer", "gpt"]):
        return ("**NLP & Transformers:**\n\n"
                "- **BERT**: Bidirectional encoder for understanding text\n"
                "- **GPT**: Generative model for text generation\n"
                "- **Transformers**: Attention-based architecture\n\n"
                "**Key tasks:** Sentiment analysis, NER, Text classification, Q&A\n\n"
                "**Library:** HuggingFace Transformers 🤗")
    elif any(w in q for w in ["hello", "hi", "hey", "namaste"]):
        return ("👋 Hello! I'm **AshBot**, your AI assistant.\n\n"
                "I can help you with:\n- 🤖 AI/ML concepts\n- 💼 Job search & career advice\n"
                "- 📚 Technical knowledge\n- 🐍 Python & Data Science\n- ☁️ Cloud technologies\n\n"
                "What would you like to know?")
    else:
        return ("I'm here to help with AI, ML, Data Science, and career topics!\n\n"
                "Try asking about:\n- Machine Learning algorithms\n- Deep Learning & Neural Networks\n"
                "- Python for Data Science\n- Career & interview tips\n- Cloud & MLOps\n- NLP & Transformers")


def show():
    st.markdown("## 🤖 AshBot — AI Assistant")
    st.markdown("Ask me anything about AI, ML, Data Science, careers & more!")

    # Optional OpenAI key
    with st.expander("⚙️ Connect your OpenAI API key for smarter responses (optional)"):
        key = st.text_input("OpenAI API Key", type="password", placeholder="sk-...")
        if key:
            st.session_state["openai_key"] = key
            st.success("Key saved for this session!")

    st.markdown("---")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            {"role": "assistant", "content":
             "👋 Hi! I'm **AshBot**. Ask me about AI, ML, jobs, or anything tech!"}
        ]

    # Display chat
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input
    if prompt := st.chat_input("Ask AshBot anything..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_ai_response(prompt, st.session_state.chat_history)
            st.markdown(response)
        st.session_state.chat_history.append({"role": "assistant", "content": response})

    # Quick prompts
    st.markdown("---")
    st.markdown("**💡 Quick Questions:**")
    cols = st.columns(3)
    quick = [
        "What is Machine Learning?",
        "How to prepare for ML interviews?",
        "Explain Deep Learning",
        "Python for Data Science",
        "What is GCP BigQuery?",
        "Career tips for AI engineers"
    ]
    for i, q in enumerate(quick):
        with cols[i % 3]:
            if st.button(q, key=f"quick_{i}"):
                st.session_state.chat_history.append({"role": "user", "content": q})
                resp = get_ai_response(q, st.session_state.chat_history)
                st.session_state.chat_history.append({"role": "assistant", "content": resp})
                st.rerun()
