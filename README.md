기본이미지를 지정
```go
FROM python:alpine
```
작업 디렉토리 지정, 변경
```go
WORKDIR /discode_test
```
기본이미지에 설정할 작업
```go
RUN pip install bs4
RUN pip install datetime
RUN pip install requests
```
discode.py라는 파일을 /discode_test라는 디렉토리에 저장 
```go
COPY discode.py /discode_test
```
환경변수로써 타임존을 아시아/서울로 지정, 변경
```go
ENV TZ=Asia/Seoul
```
컨테이너 실행후 기본으로 실행할 명령어
```go
ENTRYPOINT [ "python" ]
```
ENTRYPOINT인자 뒤에 실행됨
컨테이너에서 딱 한번 실행됨 그래서 1번만 실행할 수 있고 이 명령어 뒤에는 명령어를 사용할수 없다.
CMD [ "discode.py" ]
