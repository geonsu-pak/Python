# Collections

데이터 타입 | 순서유무(ordered) | 변경유무(changeable) | 동일 멤버 허용유무
------------ | --------- | ---- | ---
List | O | O | O
Tuple | O | X | O
Set | X | X | X
Dictonary | O | O | X

기능 | List | Tuple | Set | Dictonary
---- | ---- | ---- | ---- | ----
생성 | list(("A","B", 1)), ["A","B", 1] | | |
길이 | len(list) | | |
액세스 | list[1], list[1,3], list[-1]  | | |
변경 | list[0] = "a", list[0:2] = ["A", "b] | | |
추가(위치)| list.insert(1, "a")  | | |
추가(마지막) | list.append("D") | | |
삭제(특정)| list.remove("A")
삭제(위치) | list.pop(1) = del thislist[1]
삭제(마지막)| list.pop()
클리어 | list.clear()
합치기 | list.extend(list,set,tuple or dict)


## 휠터링한 새 리스트 생성
newlist = **[expression for item in iterable if condition == True]**    
1. 리스트중 애플만 아닌것만 추출    
    newlist = [x for x in fruits if x != "apple"]    
2. 0 - 9 의 숫자 리스트    
    newlist = [x for x in range(10)]    
3. 0 - 9 의 숫자중 5보다 작은수의 리스트    
    newlist = [x for x in range(10) if x < 5]    


    
    











