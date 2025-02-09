FROM public.ecr.aws/lambda/python:3.8

RUN mkdir -p /app
COPY ./main.py /app/
COPY model/ /app/model/
COPY ./requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y install curl
RUN apt-get install libgomp1
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
WORKDIR /app
EXPOSE 8080
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]