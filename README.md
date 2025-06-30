# 📰 News-Article-Categorization 📊
A machine learning project that categorizes news articles into topics like Politics, Sports, and Tech using the Naive Bayes algorithm. Achieves ~86% accuracy with TF-IDF and NLP preprocessing on real-world data. Includes both CLI and GUI for real-time, scalable classification.
A smart, lightweight, and scalable machine learning solution that automatically classifies unstructured news text into structured and meaningful categories. This project addresses the increasing demand for intelligent content management in the digital age, where thousands of articles are generated every day across domains like politics, sports, technology, and entertainment.

With a fully integrated Natural Language Processing pipeline and an intuitive GUI, this project demonstrates how Naive Bayes — a time-tested algorithm — can be used to make accurate, real-time predictions on unseen news content. Built with precision and extensibility in mind, this solution showcases the harmony of machine learning theory, NLP, and software design in a single deployable product.

> "Transforming unstructured news into structured insight with the power of probability."

![GitHub Stars](https://img.shields.io/github/stars/your-username/news-article-categorization?style=social)
![GitHub Forks](https://img.shields.io/github/forks/your-username/news-article-categorization?style=social)

---

## 📚 About the Project

In an era dominated by digital content and information overload, the ability to intelligently classify and manage vast volumes of news articles is a growing necessity. With hundreds of articles being published daily across numerous domains, from politics and sports to technology and entertainment, manually organizing this information is neither scalable nor efficient. News agencies, aggregators, and content recommendation platforms struggle to deliver personalized content to users without robust and intelligent categorization systems.

The problem becomes even more pressing in the context of real-time news feeds where latency and accuracy are paramount. Poorly categorized content leads to irrelevant suggestions, poor user engagement, and ultimately, reduced platform retention. Traditional keyword-based or rule-based methods fall short in such dynamic environments due to their inflexibility and lack of adaptability.

**This project solves that problem** by implementing a scalable and reliable machine learning solution — the Naive Bayes classifier — built using Python's most powerful NLP libraries. It leverages the statistical underpinnings of Bayes' theorem to identify patterns within text and categorize articles into their relevant topics. With efficient TF-IDF vectorization and thoughtful preprocessing, the model delivers consistently high performance.

**Key Highlights:**

* 🔁 **Real-time scalability:** Trained model can instantly categorize unseen articles, suitable for high-throughput pipelines.
* 📊 **Proven accuracy:** Achieves **~86% accuracy** across five distinct categories using the BBC News dataset.
* ⚡ **Fast and Lightweight:** The Naive Bayes model, known for its simplicity, offers blazing fast predictions and a small memory footprint — ideal for production deployment.
* 🧩 **Modular and extensible:** Built with clean Python modules and GUI integration, it can be easily adapted to other datasets or NLP workflows.

> "From chaos to clarity — this project empowers digital systems to organize the internet’s most valuable resource: information."

---

## 🚀 Features

* ✅ **Auto-Categorization** of news articles using NLP and machine learning  
* 🧠 **Naive Bayes Classifier**: Efficient and interpretable model based on Bayes’ Theorem  
* 📊 **TF-IDF Vectorization**: Converts text into meaningful numeric vectors  
* 🔍 **Text Preprocessing**: Includes lemmatization, stopword removal, tokenization  
* 🗂️ **Multi-Category Support**: Supports classification into Politics, Business, Sports, Tech, Entertainment  
* 🧪 **Model Evaluation**: Accuracy, Precision, Recall, F1-score, and more  
* 🧱 **Modular Architecture**: Clean and scalable Python code structure  
* 🎨 **GUI using Tkinter**: Upload your file, get instant category classification  
* 💾 **Trained Model Export**: Saves classifier using `joblib` for reuse and deployment  
* ✨ **Bonus**: Article creation tool and file-based classification pipeline  

---

## 🛠️ Tech Stack

### 👨‍💻 Languages & Libraries:
- Python 3  
- NLTK  
- Scikit-learn  
- Pandas  
- NumPy  
- Matplotlib  
- Tkinter  
- XGBoost  
- Joblib  

### 🧠 ML Concepts:
- Naive Bayes (Multinomial)  
- TF-IDF & Bag-of-Words  
- Classification Metrics  
- Train/Test Split  

---

## 📁 Project Structure

```bash
├── data/
│   └── BBC News Train.csv       # Labeled dataset for training/testing
├── model/
│   └── text_classifier.pkl      # Saved classifier using joblib
├── src/
│   ├── preprocess.py            # Text cleaning and processing
│   ├── train_model.py           # Model training and evaluation
│   └── classify.py              # CLI and GUI based prediction
├── gui/
│   └── article_classifier_gui.py # Tkinter-based user interface
├── articles/
│   └── article12.txt            # Sample input file for prediction
├── README.md
└── requirements.txt
```
---

# ⚙️ Installation Guide

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/news-article-categorization.git  
cd news-article-categorization  
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt  
```

## 3. Download NLTK Packages

```python
import nltk  
nltk.download('punkt')  
nltk.download('wordnet')  
nltk.download('stopwords')
```

---

# 🧪 Usage

## 📌 Train Model
```bash
python src/train_model.py  
```

## 📌 Classify a New Article (CLI)
```bash
python src/classify.py articles/article12.txt  
```

## 🖼️ Classify using GUI
```bash
python gui/article_classifier_gui.py  
```

## Sample Output
```csharp
Model trained and saved as 'text_classifier.pkl'!  
Predicted Category: Technology
```

---

# 🙌 Acknowledgements

Special thanks to:

- BBC News Dataset for providing quality data  
- Python, NLTK, and Scikit-learn communities for comprehensive ML libraries  
- All contributors to open-source learning and tools  

Created with NagaVishnu-Dev04 ❤ —  passionate about NLP & AI applications.

---

# 🌐 Connect With Me

**LINKED IN**
