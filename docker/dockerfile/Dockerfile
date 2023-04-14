# 베이스 이미지
FROM ubuntu:14.04
# 메타데이터
LABEL name="9ilbert" purpose="practice"

# 명령어 실행
RUN apt-get update
RUN apt-get install apache2 -y

# 파일 추가
ADD test.html /var/www/html

# 명령어를 실행할 디렉터리 지정
WORKDIR /var/www/html

RUN ["/bin/bash", "-c", "echo hello >> test2.html"]

# 포트 노출
EXPOSE 80

# 컨테이너 시작 시 실행할 명령어 지정
CMD apachectl -DFOREGROUND
