# Brainlox Technical Courses Chatbot

This project is a custom chatbot built using LangChain, FAISS, and Flask RESTful API to answer user queries about technical courses offered on Brainlox.

## Project Structure
- **`app.py`**: Flask RESTful API implementation.
- **`data.txt`**: Extracted and cleaned course data.
- **`faiss_index.bin`**: FAISS index file for efficient similarity search.
- **`requirements.txt`**: List of dependencies for the project.

## Installation Steps

1. **Clone the Repository**
```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

2. **Create and Activate Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # For MacOS/Linux
venv\Scripts\activate     # For Windows
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run Data Extraction and Indexing**
```bash
python data_extraction.py
```
(This step extracts data from Brainlox, cleans it, and builds a FAISS index.)

5. **Run the Flask API**
```bash
python app.py
```

6. **Test API Using Postman**
- Open Postman.
- Use the endpoint: `http://127.0.0.1:5000/chat`
- Set request type to `GET`
- Add the query parameter `query` (e.g., `?query=What technical courses are available?`)

## Sample API Request
```
GET http://127.0.0.1:5000/chat?query=What technical courses are available?
```

## Sample API Response
```json
{
    "answer": "$30 per session LEARN ROBOTICS... \n$30 per session LEARN SCRATCH PROGRAMMING..."
}
```

## Additional Notes
- Ensure the Postman Desktop Agent is active to test the API on localhost.
- Make sure to extract data (`data_extraction.py`) and generate `data.txt` and `faiss_index.bin` before running the API.

## Technologies Used
- **Python** (Primary Language)
- **LangChain** (For data extraction and processing)
- **FAISS** (For efficient similarity search)
- **Flask** (To build the RESTful API)


