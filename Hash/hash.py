import itertools
import hashlib
import time

def brute_force_attack(hash_value, characters, max_length):
    start_time = time.time()

    for length in range(1, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            password = ''.join(combination)
            hashed_password = hashlib.md5(password.encode()).hexdigest()  # 해시 함수에 맞게 수정
            if hashed_password == hash_value:
                elapsed_time = time.time() - start_time
                return password, elapsed_time

    elapsed_time = time.time() - start_time
    return None, elapsed_time

def main():
    plaintext_password = input("비밀번호 입력: ")
    hash_value = hashlib.md5(plaintext_password.encode()).hexdigest()  # 해시 함수에 맞게 수정
    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    max_password_length = int(input("비밀번호 최대 길이 입력: "))

    print("=== 무차별 대입 공격 시작 ===")
    print(f"해시 값: {hash_value}")
    print(f"해시 함수: MD5")
    print(f"문자 집합: {character_set}")
    print(f"비밀번호 최대 길이: {max_password_length}\n")

    password, elapsed_time = brute_force_attack(hash_value, character_set, max_password_length)

    if password:
        print(f"비밀번호를 찾았습니다: {password}")
        print(f"소요 시간: {elapsed_time:.2f}초")
    else:
        print("비밀번호를 찾을 수 없습니다.")

if __name__ == "__main__":
    main()