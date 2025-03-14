# QA Tester Assessment Script

import requests

# 1. Authentication
# URL for authentication endpoint
auth_url = "https://fakestoreapi.com/auth/login"

# JSON credentials for authentication
credentials = {
    "username": "mor_2314",
    "password": "83r5^_"
}

# Sending POST request to authenticate
response = requests.post(auth_url, json=credentials)

# Extracting token from response
auth_token = response.json().get("token")

if auth_token:
    print("Authentication successful. Token obtained.")
else:
    print("Authentication failed.")
    exit()

# 2. Create Invoice
invoice_url = "https://fakestoreapi.com/invoice"

# JSON data for creating an invoice
invoice_data = {
    "rfc_emisor": "AAA010101AAA",
    "rfc_receptor": "XAXX010101000",
    "concepto": "Venta de productos",
    "monto": 1000.00,
    "impuestos": 160.00,
    "total": 1160.00
}

# Headers with authorization token
headers = {
    "Authorization": f"Bearer {auth_token}"
}

# Sending POST request to create an invoice
invoice_response = requests.post(invoice_url, json=invoice_data, headers=headers)
print("Invoice Creation Response:", invoice_response.json())

# 3. Retrieve Invoices
invoices_url = "https://fakestoreapi.com/invoices"

# Sending GET request to retrieve all invoices
invoices_response = requests.get(invoices_url, headers=headers)
print("Invoices:", invoices_response.json())

# 4. Cancel Invoice
cancel_invoice_url = "https://fakestoreapi.com/invoice/1/cancel"

# Sending DELETE request to cancel an invoice
cancel_response = requests.delete(cancel_invoice_url, headers=headers)
print("Cancel Invoice Response:", cancel_response.json())
