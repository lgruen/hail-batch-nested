FROM ubuntu:20.04

WORKDIR /app

RUN apt-get update && apt-get install -y git python3-pip
RUN git clone https://github.com/populationgenomics/hail.git
RUN pip3 install -r hail/hail/python/requirements.txt

COPY deploy-config.json /deploy-config/deploy-config.json
RUN mkdir ~/.hail && ln -fs /user-tokens/tokens.json ~/.hail/tokens.json

COPY inner.py .

ENV PYTHONPATH=/app/hail/hail/python

CMD [ "python3", "inner.py" ]
