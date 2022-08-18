FROM python:alpine
WORKDIR /discode_test

RUN pip install bs4
RUN pip install datetime
RUN pip install requests

COPY discode.py /discode_test

ENV TZ=Asia/Seoul

ENTRYPOINT [ "python" ]
CMD [ "discode.py" ]