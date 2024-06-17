from requests import Session
from json import loads, dumps
from typing import List, Optional, Dict, Any, Union
from uuid import uuid4

class Aria2Client:
    """
    Aria2 JSON-RPC client for Python.

    Args:
        host (str, optional): The host of the aria2 RPC Server. Defaults to "localhost".
        port (int, optional): The port of the aria2 rpc-server. Defaults to 6800.
        secret (str, optional): The secret token used for authentication. Defaults to ''.
    """

    def __init__(self, host: str = "localhost", port: int = 6800, secret: str = '') -> None:
        self.secret = secret
        self._session = Session()
        self.rpc_url = f"http://{host}:{port}/jsonrpc"

