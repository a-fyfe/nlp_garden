# nlp_garden

## NLP Task: Garden Path Sentences

**Overview:

A simple Python project to test NLP tokenising and entity recognition with a list of
garden path sentences.

## Contents

* 1. Installation
* 2. Features

## 1. Installation

This project makes use of a Dockerfile to allow interested parties to run the garden.py file correctly.

The Dockerfile will execute the garden.py file's various requirements, as seen in requirements.txt

These include the use of the spaCy library.

For information on how to use Docker to deploy this web app, please refer to the following guide: 

https://www.devteam.space/blog/how-to-deploy-a-web-app-with-docker-containers/


## 2. Features

Run the garden.py file to see each garden path sentence printed, along with a tokenised version
of the sentence. Each tokenised sentence is also run through spaCy entity recognition.

Finally, some key entities are explained (e.g. NORP, LAW) for the user's convenience.
