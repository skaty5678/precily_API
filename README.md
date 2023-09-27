# Text Similarity API

This Flask API calculates the similarity between two text sentences using the Sentence Transformers library. It utilizes pre-trained models to convert text into embeddings and computes the cosine similarity between them.

### Prerequisites

- Python 3.x
- Flask
- Sentence Transformers

Install the required Python packages using the following command:

```bash
pip install flask sentence-transformers
```

### Usage

1. Clone this repository to your local machine.

2. Open a terminal and navigate to the project directory.

3. Run the Flask API using the following command:

   ```bash
   python app.py
   ```

   This will start the API locally on `http://localhost:8080`.

4. Use a tool like `curl` or `Postman` to send POST requests to the API with JSON data containing two text sentences for which you want to calculate similarity. Example:

   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"text1": "First sentence", "text2": "Second sentence"}' http://localhost:8080
   ```

5. The API will respond with a JSON object containing the similarity score between the two sentences.

### Endpoint

- **POST /**

   - Request:
   
     ```json
     {
       "text1": "First sentence",
       "text2": "Second sentence"
     }
     ```

   - Response:

     ```json
     {
       "similarity score": 0.85
     }
     ```
