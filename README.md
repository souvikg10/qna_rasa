## Setup

## Create conda environment
```
conda env create -f environment.yml -p venv/
```

### Extract QnA Pairs
To extract QnA pairs, start a flask server with 

```python
python app.py
```
In the app.py file, update the paramenter content and pass different questions through the API. You can modify the content to pass a file as well.

Based on the answer you can update the rasa/domain.yml file with the responses.

### Train a Rasa model
```
rasa train
```

### Test a Rasa model
```
rasa shell
```
