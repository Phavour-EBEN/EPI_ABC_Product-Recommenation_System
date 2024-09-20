from flask import Flask, request, jsonify
from personalization import merged_df, user_user_cf, create_user_item_matrix
from personalization import get_user_interests, content_based_recommendation
from personalization import hybrid_recommendation

app = Flask(__name__)
@app.route('/recommend', methods=['POST'])
def recommend():
    user_item_matrix = create_user_item_matrix(merged_df)
    data = request.get_json()
    target_user = data.get('user_id')
    

    if target_user is None:
        return jsonify({"error": "Both user_id is required"}), 400

    try:
        recommendations = hybrid_recommendation(merged_df,user_item_matrix, target_user)
        return jsonify({"recommendations": recommendations})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
