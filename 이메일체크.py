import re

def check_email(text):
    # 이메일 주소를 찾는 정규표현식 패턴
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # 입력된 텍스트에서 정규표현식과 매치되는 패턴 검색
    match = re.search(pattern, text)
    if match:
        return match.group()
    else:
        return None

# 샘플 데이터
sample_data = [
    "example@email.com",
    "user123@example.com",
    "test.email@example.co.uk",
    "hello.world123@example.co.in",
    "sample.email@example-domain.com",
    "123user@example.com",
    "email@example123.com",
    "user.email@example.com",
    "email@example.com",
    "user@sub.example.com"
]

# 각 샘플 데이터에 대해 이메일 주소 체크
for data in sample_data:
    result = check_email(data)
    if result:
        print(f"검색된 이메일 주소: {result}")
    else:
        print("이메일 주소를 찾을 수 없습니다.")
