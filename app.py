from flask import Flask, jsonify, request
from sentence_transformers import SentenceTransformer, util

app = Flask(__name__)

model = SentenceTransformer('all-MiniLM-L6-v2')


@app.route('/', methods=['POST'])
def calculate_similarity():
    data = request.get_json()
    sentence1 = data['text1']
    sentence2 = data['text2']
    embedding1 = model.encode(sentence1, convert_to_tensor=True)
    embedding2 = model.encode(sentence2, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(embedding1, embedding2)
    normalized_score = 0.5 * (cosine_scores + 1)
    similarity_score = round(normalized_score.item(), 2)
    return jsonify({"similarity score": similarity_score})


if __name__ == '__main__':
    app.run()
