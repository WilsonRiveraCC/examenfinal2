from werkzeug.security import generate_password_hash

password = "password123"

hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
print(hashed_password)