import requests

API = "http://127.0.0.1:5000"

def print_title(title):
    print("\n" + "="*10 + f" {title} " + "="*10)

# ----------- TEST GET /books (initial) -----------
print_title("TEST 1: GET /books (initial)")
res = requests.get(f"{API}/books")
print(res.json())

# ----------- TEST POST /books -----------
print_title("TEST 2: POST /books")
new_book = {
    "title": "Docker with SQLite",
    "author": "Eya Soussi",
    "year": 2025
}
res = requests.post(f"{API}/books", json=new_book)
book_id = res.json().get("id")
print(res.json())

# ----------- TEST GET /books after POST -----------
print_title("TEST 3: GET /books (after POST)")
res = requests.get(f"{API}/books")
print(res.json())

# ----------- TEST GET /books/<id> -----------
print_title(f"TEST 4: GET /books/{book_id}")
res = requests.get(f"{API}/books/{book_id}")
print(res.json())

# ----------- TEST PUT /books/<id> -----------
print_title(f"TEST 5: PUT /books/{book_id}")
update_data = {
    "title": "Updated Docker Book",
    "year": 2026
}
res = requests.put(f"{API}/books/{book_id}", json=update_data)
print(res.json())

# Vérifier la mise à jour
print_title(f"TEST 6: GET /books/{book_id} (after PUT)")
res = requests.get(f"{API}/books/{book_id}")
print(res.json())

# ----------- TEST DELETE /books/<id> -----------
print_title(f"TEST 7: DELETE /books/{book_id}")
res = requests.delete(f"{API}/books/{book_id}")
print(res.json())

# Vérifier la suppression
print_title(f"TEST 8: GET /books/{book_id} (after DELETE)")
res = requests.get(f"{API}/books/{book_id}")
print(res.json())
