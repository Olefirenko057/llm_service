How to Run the Project
Install Required Dependencies using "pip install -r requirements.txt"

Start Required Services
MongoDB: Ensure the MongoDB server is running locally
ActiveMQ: Start the ActiveMQ server

Run the Application
Start the Flask application:
python app.py

How to Run Tests:
pip install pytest

python tests/test_langchain.py
python tests/test_whisper.py
python tests/test_mongodb.py
python tests/test_llm_service.py

Replace pdf_path = "C:/Users/Win-10/Downloads/Lesson_11._Vocabulary_set.pdf"
with the absolute path to a valid PDF file on your local machine.