# Collections

데이터 타입 | 순서유무(ordered) | 변경유무(changeable) | 동일 멤버 허용유무
------------ | --------- | ---- | ---
List | O | O | O
Tuple | O | X | O
Set | X | X | X
Dictonary | O | O | X

기능 | List | Tuple | Set | Dictonary
---- | ---- | ---- | ---- | ----
생성 | list(("A","B", 1))<br>["A","B", 1] | tuple(("A","B", 1))<br>("A","B", 1)|set(("A","B", 1))<br>{"A","B", 1} | {key:value,...}
길이 | len(...) | len(...) | len(...) | 
액세스 | lst[1] : (1+1)번째 아이템<br>lst[1,3] :1~(3-1)번째아이템<br>lst[-1] : 마지막 아이템 | 좌동 | | value = dic[key]    value=dic.get(key)
변경 | lst[0] = "a"<br>list[0:2] = ["A", "b] | 리스트변환: list(tuple)<br>리스트동일변경<br>튜플변환: tuple(list)| | dic[key]=value
추가(위치)| .insert(1, "a")  | 리스트변환: list(tuple)<br>리스트동일변경<br>튜플변환: tuple(list) | .add("D") | 
추가(마지막) | .append("D") | 리스트변환: list(tuple)<br>리스트동일변경<br>튜플변환: tuple(list)  | | dic[key]=value
삭제(특정)| .remove("A") | 리스트변환: list(tuple)<br>리스트동일변경<br>튜플변환: tuple(list)  | .remove("A")    .discard("A")| .pop(key)    del dic[key]
삭제(위치) | .pop(1)    del thislist[1] | 리스트변환: list(tuple)<br>리스트동일변경<br>튜플변환: tuple(list)  | |
삭제(마지막)| .pop() | 리스트변환: list(tuple)<br>리스트동일변경<br>튜플변환: tuple(list)  | .pop() |
클리어 | .clear() | 리스트변환: list(tuple)<br>리스트동일변경<br>튜플변환: tuple(list)  | .clear() |
합치기 | .extend(list,set,tuple or dict) | 리스트변환: list(tuple)<br>리스트동일변경<br>튜플변환: tuple(list)  | .update(list,set,tuple or dict) |
정렬(내림차순) | .sort() 
정렬(오름차순) | .sort(reverse=True)
정렬(lambda) | .sort(key=lambda x:abs(x-50))
복사 | lst = .copy()    list(list) | | .copy() | .copy()
Unpack | | (r,g,b)=color | for key,value in dic.items():
"  | | (r,g,*b)=(1,2,3,4,5)    -> b=[3,4,5]


## 휠터링한 새 리스트 생성
newlist = **[expression for item in iterable if condition == True]**    
1. 리스트중 애플만 아닌것만 추출    
    newlist = [x for x in fruits if x != "apple"]    
2. 0 - 9 의 숫자 리스트    
    newlist = [x for x in range(10)]    
3. 0 - 9 의 숫자중 5보다 작은수의 리스트    
    newlist = [x for x in range(10) if x < 5]    
4. (0, 0) - (3, 3) 리스트 작성
    newlist = [(x, y) for x in range(4) for y in range(4)]


    
    











