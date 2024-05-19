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

## Error in NixOS

```
/nix/store/x9gifid500jh5c6zv4787g602qxnb58a-python3-3.12.3/lib
Traceback (most recent call last):
  File "/home/robert/git/mi/dfcx-python-client/main.py", line 55, in <module>
    run_agent_with_func_tools()
  File "/home/robert/git/mi/dfcx-python-client/main.py", line 49, in run_agent_with_func_tools
    detect_intent_text(project_id, location_id, agent_id, session_id, text)
  File "/home/robert/git/mi/dfcx-python-client/main.py", line 5, in detect_intent_text
    import google.cloud.dialogflowcx_v3 as dialogflow
  File "/home/robert/git/mi/dfcx-python-client/venv/lib/python3.12/site-packages/google/cloud/dialogflowcx_v3/__init__.py", line 21, in <module>
    from .services.agents import AgentsAsyncClient, AgentsClient
  File "/home/robert/git/mi/dfcx-python-client/venv/lib/python3.12/site-packages/google/cloud/dialogflowcx_v3/services/agents/__init__.py", line 16, in <module>
    from .async_client import AgentsAsyncClient
  File "/home/robert/git/mi/dfcx-python-client/venv/lib/python3.12/site-packages/google/cloud/dialogflowcx_v3/services/agents/async_client.py", line 32, in <module>
    from google.api_core import gapic_v1
  File "/home/robert/git/mi/dfcx-python-client/venv/lib/python3.12/site-packages/google/api_core/gapic_v1/__init__.py", line 16, in <module>
    from google.api_core.gapic_v1 import config
  File "/home/robert/git/mi/dfcx-python-client/venv/lib/python3.12/site-packages/google/api_core/gapic_v1/config.py", line 23, in <module>
    import grpc
  File "/home/robert/git/mi/dfcx-python-client/venv/lib/python3.12/site-packages/grpc/__init__.py", line 22, in <module>
    from grpc import _compression
  File "/home/robert/git/mi/dfcx-python-client/venv/lib/python3.12/site-packages/grpc/_compression.py", line 20, in <module>
    from grpc._cython import cygrpc
ImportError: libstdc++.so.6: cannot open shared object file: No such file or directory
```
