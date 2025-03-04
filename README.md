# DDoSAttackPredictor
This is a machine learning-powered web application that detects potential DDoS attacks based on network traffic data. The frontend is built with HTML, CSS, and JavaScript, while the backend is powered by Flask and TensorFlow.

Dataset: https://www.kaggle.com/datasets/oktayrdeki/ddos-traffic-dataset/code

## 🚀 Features

- Upload network traffic details and predict whether it's a DDoS attack.
- Uses Logistic Regression trained on a DDoS dataset.
- One-Hot Encoding & Normalization for preprocessing.
- Interactive UI for easy usage.
- Deployed on Render.

## 🛠️ Setup Instructions
#### **Go on Render*
https://ddosattackpredictor.onrender.com
PS: might be down ☹️
#### **Run Locally**
```sh
# Clone the repository
git clone https://github.com/nishalahmedpk/DDoSAttackPredictor
cd DDoSAttackPredictor

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the Flask app with gunicorn
gunicorn app:app

```
Your backend will start at http://127.0.0.1:5000/

## 📡 Usage
- Open the hosted frontend URL.
- Enter network traffic details (e.g., Source Port, Dest Port, Protocols, Packet Size, etc.).
- Click "Predict" to check for DDoS Attack (1 = Yes, 0 = No)

