# Product Recommendation System

ABC Company Limited operates an online shop where customers browse and purchase products. The company has recognized the potential of AI technologies to enhance their business by personalizing product recommendations for their users. This project implements a recommendation system that provides personalized product suggestions based on user preferences.

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
├── requirements.txt             # Python dependencies
└── tests/                       # Test cases for the system
```

## How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/recommendation-system.git
cd recommendation-system
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

You can interact with the recommendation API using `curl` or Postman.

#### **Endpoint:**
- **URL:** `http://127.0.0.1:5000/recommend`
- **Method:** POST
- **Content-Type:** `application/json`

#### **Request Body Example**:
```json
{
  "userid": "user123"
}
```

#### **Response Example**:
```json
{
  "userid": "user123",
  "recommended_products": [
    "Product A",
    "Product B",
    "Product C",
    "Product D"
  ]
}
```

### 5. Customizing the Recommendation Logic

You can modify the logic in `personalization.py` and `recommendation-api.py` to suit ABC Company’s evolving needs. If needed, adjust the algorithm to better match user preferences by adding or updating features like collaborative filtering, content-based filtering, or hybrid models.

## API Details

### Personalization Engine (`personalization.py`)

This module provides real-time recommendations when a user interacts with a specific product. It works by analyzing the user’s behavior and matching it with similar products.

### Recommendation API (`recommendation-api.py`)

The Recommendation API is designed to return a set of recommended products based on the user's historical preferences. The API receives a user ID in JSON format and returns a list of recommended products for that user.

### Example Usage

```python
# Inside recommendation-api.py
def recommend_products(userid):
    # Logic to recommend products for the given user ID
    recommended_products = ["Product A", "Product B", "Product C", "Product D"]
    return recommended_products
```

## Testing

You can write test cases in the `tests/` directory to ensure the system works as expected. Use tools like `pytest` to automate testing.

To run the tests:

```bash
pytest tests/
```

## Future Enhancements

- Improve recommendation algorithms by incorporating user behavior tracking, purchase history, and real-time data.
- Implement collaborative filtering to suggest products based on similar users.
- Add A/B testing to evaluate different recommendation strategies.

## Contributing

Feel free to contribute by opening issues or submitting pull requests to improve the recommendation system.

## License

This project is licensed under the MIT License.

---
