import requests

# API endpoints
AUTH_URL = "https://fakestoreapi.com/auth/login"
FACTURAS_URL = "https://fakestoreapi.com/carts"

# Authentication
def get_token():
    """
    Authenticate and retrieve the access token.
    - URL: https://fakestoreapi.com/auth/login
    - Method: POST
    - Request Body (JSON):
      {
        "username": "mor_2314",
        "password": "83r5^_"
      }
    - Response: Returns a token for authentication.
    """
    credentials = {
        "username": "mor_2314",
        "password": "83r5^_"
    }
    response = requests.post(AUTH_URL, json=credentials)
    return response.json().get("token")

# Get invoices
def get_facturas(token):
    """
    Retrieve the list of invoices.
    - URL: https://fakestoreapi.com/carts
    - Method: GET
    - Headers:
      {
        "Authorization": "Bearer <TOKEN>"
      }
    - Response:
      [
        {
          "id": 1,
          "userId": 1,
          "date": "2023-01-01",
          "total": 150.00,
          "items": [...]
        },
        ...
      ]
    """
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(FACTURAS_URL, headers=headers)
    return response.status_code, response.json()

# Main execution
if __name__ == "__main__":
    # Step 1: Authenticate and get the token
    token = get_token()
    print(f"Token: {token}")

    # Step 2: Retrieve invoices using the token
    status_code, facturas = get_facturas(token)
    print(f"Status Code: {status_code}")
    print(f"Facturas: {facturas}")