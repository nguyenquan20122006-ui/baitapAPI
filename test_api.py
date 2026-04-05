import requests

# URL API
BASE_URL = "http://127.0.0.1:8000"

def test_health():
    print("=== TEST HEALTH ===")
    response = requests.get(f"{BASE_URL}/health")
    print("Status code:", response.status_code)
    print("Response:", response.json())
    print()

def test_root():
    print("=== TEST ROOT ===")
    response = requests.get(f"{BASE_URL}/")
    print("Status code:", response.status_code)
    print("Response:", response.json())
    print()

def test_predict():
    print("=== TEST PREDICT ===")

    test_cases = [
        {"text": "I love this product, it is amazing!"},
        {"text": "This is the worst experience ever."}
    ]

    for i, data in enumerate(test_cases, 1):
        print(f"--- Test case {i} ---")
        response = requests.post(f"{BASE_URL}/predict", json=data)
        print("Input:", data)
        print("Status code:", response.status_code)
        print("Response:", response.json())
        print()

if __name__ == "__main__":
    print("===== TESTING API =====\n")
    
    test_root()
    test_health()
    test_predict()
    
    print("===== DONE =====")