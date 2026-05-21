import streamlit as st

TOPICS = {
    "🤖 Machine Learning": {
        "icon": "🤖",
        "color": "#1a73e8",
        "subtopics": {
            "Supervised Learning": "Algorithms trained on labeled data. Examples: Linear Regression, Decision Trees, SVM, Random Forest, KNN.",
            "Unsupervised Learning": "Algorithms that find patterns in unlabeled data. Examples: K-Means, DBSCAN, PCA, Autoencoders.",
            "Ensemble Methods": "Combining multiple models: Bagging (Random Forest), Boosting (XGBoost, AdaBoost, Gradient Boosting).",
            "Model Evaluation": "Metrics: Accuracy, Precision, Recall, F1-Score, ROC-AUC, RMSE, MAE. Use cross-validation to avoid overfitting.",
            "Hyperparameter Tuning": "GridSearchCV, RandomSearchCV, Bayesian Optimization. Key params: learning rate, depth, n_estimators.",
        }
    },
    "🧠 Deep Learning": {
        "icon": "🧠",
        "color": "#7b1fa2",
        "subtopics": {
            "Neural Networks": "Layers of neurons: Input → Hidden → Output. Activation functions: ReLU, Sigmoid, Softmax.",
            "CNN (Computer Vision)": "Convolutional layers extract spatial features. Used for image classification, object detection (YOLO, ResNet).",
            "RNN / LSTM": "Recurrent networks for sequential data. LSTM solves vanishing gradient. Used in time series, NLP.",
            "Transformers": "Attention mechanism replaces recurrence. BERT (understanding), GPT (generation). Foundation of modern LLMs.",
            "Transfer Learning": "Use pretrained models (VGG, ResNet, BERT) and fine-tune on your dataset. Saves time and data.",
        }
    },
    "📊 Data Science": {
        "icon": "📊",
        "color": "#0097a7",
        "subtopics": {
            "EDA (Exploratory Data Analysis)": "Understand data with statistics and visualizations. Tools: Pandas, Matplotlib, Seaborn, Plotly.",
            "Feature Engineering": "Create new features, handle missing values, encode categoricals, scale numerics.",
            "Statistics Fundamentals": "Mean, Median, Std Dev, Distributions, Hypothesis Testing, p-value, Confidence Intervals.",
            "SQL for Data Science": "SELECT, JOIN, GROUP BY, Window Functions, CTEs. Essential for data extraction and analysis.",
            "Data Visualization": "Matplotlib, Seaborn for static. Plotly, Streamlit for interactive. Tableau/Power BI for dashboards.",
        }
    },
    "☁️ Cloud & MLOps": {
        "icon": "☁️",
        "color": "#e65100",
        "subtopics": {
            "GCP Essentials": "BigQuery (data warehouse), Cloud Storage, Dataflow, Pub/Sub, Vertex AI for ML.",
            "Apache Airflow": "DAG-based workflow orchestration. Schedule and monitor data pipelines. Used heavily in data engineering.",
            "CI/CD for ML": "Tekton, GitHub Actions, Jenkins. Automate model training, testing, and deployment pipelines.",
            "Docker & Kubernetes": "Containerize ML models with Docker. Orchestrate at scale with Kubernetes. Essential for MLOps.",
            "Terraform (IaC)": "Define cloud infrastructure as code. Reproducible, version-controlled infrastructure deployments.",
        }
    },
    "🐍 Python": {
        "icon": "🐍",
        "color": "#2e7d32",
        "subtopics": {
            "NumPy & Pandas": "NumPy for numerical computing. Pandas for data manipulation: DataFrames, Series, groupby, merge.",
            "Scikit-learn": "ML library: preprocessing, model selection, pipelines, metrics. Standard for classical ML.",
            "TensorFlow / Keras": "Google's deep learning framework. Keras provides high-level API. Good for production deployment.",
            "PyTorch": "Facebook's DL framework. Dynamic computation graph. Preferred for research and custom architectures.",
            "Streamlit": "Build data apps and ML dashboards in pure Python. Deploy easily on Streamlit Cloud.",
        }
    },
}

def show():
    st.markdown("## 📚 Technical Knowledge Base")
    st.markdown("Structured learning for AI, ML, Data Science & Cloud")
    st.markdown("---")

    selected = st.selectbox("📂 Select Topic", list(TOPICS.keys()))
    topic = TOPICS[selected]

    st.markdown(f"""
    <div style='background: linear-gradient(135deg, {topic["color"]}22, {topic["color"]}11);
                border-left: 5px solid {topic["color"]}; padding: 1rem 1.5rem;
                border-radius: 8px; margin-bottom: 1.5rem;'>
        <h3 style='color: {topic["color"]}; margin: 0;'>{selected}</h3>
    </div>
    """, unsafe_allow_html=True)

    for subtopic, content in topic["subtopics"].items():
        with st.expander(f"📌 {subtopic}"):
            st.markdown(f"<p style='color:#333; line-height:1.7;'>{content}</p>",
                        unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🎯 Interview Prep Cheatsheet")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **ML Interview Must-Know:**
        - Bias-Variance Tradeoff
        - Overfitting vs Underfitting
        - Cross-validation strategies
        - Feature selection methods
        - Regularization (L1, L2)
        """)
    with col2:
        st.markdown("""
        **Coding Round Tips:**
        - Practice array/string problems
        - Know sorting algorithms
        - Understand time complexity
        - Practice SQL queries
        - Build end-to-end ML projects
        """)
