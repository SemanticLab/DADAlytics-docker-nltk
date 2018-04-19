FROM python:3

WORKDIR /usr/src/app

RUN pip install --no-cache-dir nltk falcon scikit-learn gunicorn numpy scipy

COPY chunker.pkl ./
COPY model.py ./
COPY server.py ./

COPY download_nltk_data.py ./
RUN python download_nltk_data.py


EXPOSE 9003

CMD [ "gunicorn", "server:api", "-b 0.0.0.0:9003", "--workers=4" ]