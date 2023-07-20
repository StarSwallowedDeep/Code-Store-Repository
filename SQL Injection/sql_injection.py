import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# 사용자 테이블 삭제 (기존 테이블 삭제)
cursor.execute('''DROP TABLE IF EXISTS users''')

# 사용자 테이블 생성
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT,
        password TEXT
    )
''')

# 사용자 데이터 삽입
users = [
    ('admin', 'injection')
]
cursor.executemany('INSERT INTO users VALUES (?, ?)', users)

# 데이터베이스에 변경사항 저장
conn.commit()

# 사용자 인증 함수
def authenticate(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False

# 사용자 인증 과정
authenticated = False
while not authenticated:
    username = input("Username: ")
    password = input("Password: ")

    if authenticate(username, password):
        authenticated = True
        print("Authentication successful.")
    else:
        print("Authentication failed. Please try again.")

# 데이터베이스 연결 종료
conn.close()

# example
# Username: admin
# Password: injection [' OR 1=1 --]