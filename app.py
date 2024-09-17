from flask import Flask, request, jsonify
from personalizaton import recommendation
# from flask_cors import CORS


app = Flask(__name__)

# API route to get movie recommendations
@app.route('/api/recommend', methods=['POST'])
def recommend():
    try:
        # Get the JSON data sent from the client (e.g., Postman)
        data = request.get_json()

        # Extract the movie name from the JSON payload
        movie_name = data.get('movie_name')

        if not movie_name:
            return jsonify({"error": "movie_name is required"}), 400

        # Generate recommendations using the recommendation system
        recommendations = recommendation(movie_name)

        # Return the recommendations in JSON format
        return jsonify({
            "movie_name": movie_name,
            "recommendations": recommendations
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
