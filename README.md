# Product Recommendation System

This project implements a recommendation system for ABC Company Limited's online shop. The system aims to understand customer preferences and personalize product recommendations for each user. It consists of two main components:

## Project Overview

The system consists of two AI engines:

1. **Personalization Engine (`personalization.py`)**: This engine returns product recommendations when a user clicks on a product. It is currently functioning as expected.
  
2. **Recommendation API (`recommendation-api.py`)**: This engine returns a list of products based on a user's preferences. The system takes in JSON data with a user ID and returns a set of recommended products in JSON format.

## Features

- **Personalized Recommendations**: When a user interacts with a product, the system provides personalized product suggestions based on their activity.
- **API-based Recommendations**: The recommendation API accepts a user ID and returns a list of recommended products in JSON format, allowing the developers to display personalized products on the user's homepage.

## Project Structure

```
.
├── personalization.py           # Personalization engine logic
├── recommendation-api.py        # API for recommendation engine
├── README.md                    # Project documentation
└── requirements.txt             # Python dependencies
```

## How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/Phavour-EBEN/EPI_ABC_Product-Recommendation_System.git
cd EPI_ABC_Product-Recommendation_System
```

### 2. Install Dependencies

Make sure you have Python 3.x installed. Install the required dependencies with:

```bash
pip install -r requirements.txt
```

### 3. Run the API

To start the recommendation API:

```bash
python recommendation-api.py
```

This will launch the API locally at `http://127.0.0.1:5000/`.

### 4. Testing with JSON Input

You can interact with the recommendation API using `Postman` or curl.

#### **Endpoint:**
- **URL:** `http://127.0.0.1:5000/recommend`
- **Method:** POST
- **Content-Type:** `application/json`

#### **Request Body Example**:
```json
{
  "user_id": "19"
}
```

#### **Response Example**:
```json
{
  "recommendations": [
    "20",
    "3",
    "19"
  ]
}
```

### 5.The Recommendation Logic

The logic in personalization.py and recommendation-api.py is designed to adapt to evolving needs. The algorithm matches user preferences by incorporating features such as collaborative filtering, content-based filtering, and hybrid models.

## API Details

### Personalization Engine (`personalization.py`)

This module provides real-time recommendations when a user interacts with a specific product. It works by analyzing the user’s behavior and matching it with similar products.

### Recommendation API (`recommendation-api.py`)

The Recommendation API is designed to return a set of recommended products based on the user's historical preferences. The API receives a user ID in JSON format and returns a list of recommended products for that user.

### Example Usage

```python
# Inside recommendation-api.py
from flask import Flask, request, jsonify
# from collections import defaultdict
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
```

## Future Enhancements

- Improve recommendation algorithms by incorporating user behavior tracking, purchase history, and real-time data.
- Add A/B testing to evaluate different recommendation strategies.
