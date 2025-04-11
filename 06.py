tel = {'jack': 4098, 'sape': 4139}

del tel['sape']              # 'sape' 키 삭제
tel['irv'] = 4127            # 'irv' 키 추가

print(tel)                   # 현재 딕셔너리 출력

print(list(tel))             # 키만 리스트로 변환

print(sorted(tel))           # 키를 정렬한 리스트 반환

print('guido' in tel)        # 'guido'라는 키가 있는지 확인 → False

print('jack' not in tel)     # 'jack' 키가 없냐? → False
