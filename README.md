# DADAlytics-docker-nltk
Docker image and scripts to build the NLTK NER component

The source for building the model and server for the docker image: https://hub.docker.com/r/semlab/dadalytics-nltk/

`model.py` - To build the Groningen Meaning Bank corpus modle
`server.py` the API server
`Dockerfile` - to build the docker image.

To use:
```
docker run -it -p 9003:9003 semlab/dadalytics-nltk
```

CURL Example:
https://gist.github.com/thisismattmiller/69e0e70031a8820b87ed588ba71c5f74

Python and Node script examples:
https://gist.github.com/thisismattmiller/fe32811b557b7c784f8111401b546040
