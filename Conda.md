# Windows 사용
## 다운로드 : 디폴트설정 사용
https://www.anaconda.com/products/individual

### 중요
설치중 아래 화면처럼 체크를 해주지 않으면 나중에 PATH에 ~\Anaconda3\condabin 를 등록해야 함
<img src=https://i.stack.imgur.com/11aGz.png width=50% height=50%/>    
아래 컴맨드를 실행하므로써 지금 설치한 Python을 기본으로 사용하게 됨. 

    conda init
python.exe 의 설치 장소 찾기    

    where python


## 설치 확인 및 업데이트
### Windows 메뉴 -> Ananconda Prompt (anaconda3) 실행
### 설치 폴더 이동
    cd C:\Users\[사용자명]\anaconda3
    (base) C:\Users\[사용자명]\anaconda3>conda list
    (base) C:\Users\[사용자명]\anaconda3>conda update conda
    
### 파이선 환경 조작
##### snakes 이름으로 python 3.9 환경을 생성
    conda create --name snakes python=3.9
##### snakes 환경을 sanakes2 으로 클론
    conda create --clone snakes --name snakes2
##### snakes 환경을 파일로 출력 -> 다른 PC, OS 환경에서 복제 가능
    // 파일 불러내기
    conda env export --name sanakes > snakes.yml
    // 파일 불러오기
    conda env create --file snakes.yml
##### 삭제하기
    conda remove --name snakes --all

### 환경을 활성화(들어가기), 비활성화(빠져나오기)
    conda activate snakes
    conda deactivate snakes
### 패키지 설치
    // 설치
    conda install PKGNAME==3.1.4
    // 삭제
    conda uninstall PKGNAME
    
### 환경 리스트
    conda info --envs
    
### 패키지 설치 유무
    conda search 패키지명
    
