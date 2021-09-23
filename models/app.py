from flask import Flask,request,jsonify
from flask_cors import CORS
from recommender import predictions
from collections import defaultdict

app = Flask(__name__)
CORS(app)

@app.route('/test', methods=['GET'])

def recommend_movies():
    # get params
    user = request.args.get('user', None)
    n = int(request.args.get('n', None))

    # First map the predictions to each user.
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user and retrieve the k highest ones.
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return jsonify(top_n[user])

if __name__ == '__main__':
    app.run(port=5000, debug=True)