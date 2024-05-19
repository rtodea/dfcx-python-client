# `DialogFlow CX` client with Python

## References

1. [Google's Official Documentation](https://cloud.google.com/dialogflow/cx/docs/reference/library/python)

## Using the latest version

```
from google.cloud import dialogflowcx_v3beta1 as dialogflow
```

## Installing Deps

We recommend using a Python virtual env.
```
python -m venv venv
```

```
source venv/bin/activate
```

```
pip install -r requirements.txt
```

## Authentication

Make sure to have the `*.json` with your project credentials and pass that to the env of any script:

```shell
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"
```