import re

def is_valid_email(email):
    """
    이메일 주소가 유효한지 확인하는 함수.
    :param email: 검사할 이메일 주소
    :return: 유효하면 True, 그렇지 않으면 False
    """
    # 이메일 주소 정규식 패턴
    # raw string notation: 소문자 r을 붙이는 표현식
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(email_pattern, email) is not None


# 테스트용 샘플 이메일 리스트
email_samples = [
    "test@example.com",      # 유효한 이메일
    "user123@domain.org",    # 유효한 이메일
    "name.surname@company.net",  # 유효한 이메일
    "invalid-email.com",     # @가 없음 (유효하지 않음)
    "another.email@",        # 도메인이 없음 (유효하지 않음)
    "123@456.789",           # 도메인 형식이 잘못됨 (유효하지 않음)
    "user@site.c",           # 최상위 도메인이 너무 짧음 (유효하지 않음)
    "user@@example.com",     # @가 두 번 사용됨 (유효하지 않음)
    "valid-email@sub.domain.com",  # 유효한 이메일
    "invalid-char@domain..com"     # 도메인에 연속된 점 (유효하지 않음)
]

# 이메일 주소를 검사하고 결과를 출력
for email in email_samples:
    result = is_valid_email(email)
    print(f"{email}: {'Valid' if result else 'Invalid'}")
