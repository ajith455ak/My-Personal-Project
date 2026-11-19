"""
Authentication Module - My-Personal-Project
Student: Ajith Kumar R
Register Number: 192321144
Course: CSA10 Software Engineering
"""

import hashlib

USER_DATABASE = {
    "ajith455": "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918",  # sha256 for 'admin'
    "student": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"   # sha256 for 'password123'
}

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username: str, password: str) -> bool:
    if username not in USER_DATABASE:
        return False
    return USER_DATABASE[username] == hash_password(password)

if __name__ == "__main__":
    print("Testing Login Authentication Module...")
    assert authenticate("ajith455", "admin") == True
    assert authenticate("student", "password123") == True
    assert authenticate("invalid_user", "wrong") == False
    print("All authentication tests passed successfully!")
