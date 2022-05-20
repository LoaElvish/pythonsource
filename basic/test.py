# 실습 : 암호 생성
# http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 . 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 e 문자 갯수 + ! 로 구성 => nav + 5 + 1 + !
# 결과 : nav51!

str = "http://naver.com"
rule1 = str[6:]
print(rule1)