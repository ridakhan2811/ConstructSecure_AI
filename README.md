🏗️🔒 Construct Secure AI
AI-powered safety monitoring for construction sites — real-time object detection to ensure workers are equipped with essential safety gear and comply with safety protocols.

📌 Overview
construct_secure_ai is a real-time PPE (Personal Protective Equipment) detection system built with YOLOv8 and Django.
Using a live webcam feed, it detects whether workers are wearing:

✅ Safety Helmets

✅ Reflective Vests

✅ Safety Masks

✅ Safety Glasses

The system processes live video in real-time, allowing you to filter detections via a dropdown menu (helmet-only, vest-only, multiple PPE items, or all).

🚀 Key Features
🎯 Multi-Class Detection — Detect multiple PPE items in a single model.

⚡ Real-Time Processing — Works directly with webcam feed.

📋 Detection Filtering — Choose which PPE items to monitor via dropdown.

🖥️ Full Django Integration — Frontend, backend, and AI model in one platform.

🖥️ Tech Stack
Component	Technology Used
Programming	Python 3.x
AI Framework	PyTorch
Model	YOLOv8
Web Framework	Django
Frontend	HTML, CSS, JavaScript (within Django templates)
Data Annotation	LabelImg / Roboflow

🏗️ Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/construct_secure_ai.git
cd construct_secure_ai
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Prepare the Model
Place your trained YOLOv8 weights in the models/ directory.

Update the model path in the Django settings or detection script.

4️⃣ Run the Django Server
bash
Copy
Edit
python manage.py runserver
5️⃣ Access the Application
Open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:8000
📂 Project Structure
csharp
Copy
Edit
construct_secure_ai/
│
├── dataset/           # Training data & annotations
├── models/            # YOLOv8 model weights
├── detection/         # Model inference scripts
├── templates/         # Django HTML templates
├── static/            # CSS, JS, images
├── manage.py          # Django project manager
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
📈 Future Scope
📡 IP Camera / CCTV Integration

🔔 Real-Time Alerts via Email/SMS for violations

📊 Analytics Dashboard for compliance statistics

🤖 Additional PPE Types (boots, gloves, ear protection)

