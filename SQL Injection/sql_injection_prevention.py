# SQL 인젝션을 방지하기 위해 파라미터화된 쿼리를 사용합니다. 이 방법은 사용자의
# 입력을 쿼리 문자열에 직접 연결하는 것이 아니라, 쿼리에 플레이스홀더를 사용하고 
# 파라미터 값을 따로 전달함으로써 SQL 인젝션을 방지합니다. 이렇게 하면 사용자의 
# 입력이 쿼리 문자열에 직접 포함되지 않으며, 데이터베이스 드라이버가 파라미터를 
# 적절하게 처리하여 SQL 구문에 악의적인 코드를 삽입하는 것을 방지합니다.


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
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
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