# pylint: disable=line-too-long
from json import loads, dumps
from typing import List, Optional, Dict, Any, Union
from uuid import uuid4
from requests import Session


class Aria2Client:
    """
    Aria2 JSON-RPC client for Python.

    Args:
        host (str, optional): The host of the aria2 RPC Server. Defaults to "localhost".
        port (int, optional): The port of the aria2 rpc-server. Defaults to 6800.
        secret (str, optional): The secret token used for authentication. Defaults to ''.
    """

    def __init__(
        self, host: str = "localhost", port: int = 6800, secret: str = ""
    ) -> None:
        self.secret = secret
        self._session = Session()
        self.rpc_url = f"http://{host}:{port}/jsonrpc"

    def _request(
        self,
        method: Union[str, None] = None,
        params: Optional[List[Any]] = None,
    ) -> Dict[str, Any]:
        """
        Sends an RPC request to the server made for internal use.
        Do not call this method directly unless you know what you are doing.

        Args:
            method (Union[str, None], optional): The RPC method to call.
            params (Optional[List[Any]], optional): Parameters to include in the RPC call.

        Returns:
            Dict[str, Any]: The response from the RPC server.
        """

        payload = {
            "jsonrpc": "2.0",
            "params": params or [],
            "id": uuid4().hex[:16],
        }

        if method:
            payload["method"] = method

        if self.secret:
            payload["params"].insert(0, f"token:{self.secret}")

        resp = loads(
            self._session.post(self.rpc_url, data=dumps(payload)).text
        )
        # TODO: Create an error map and implement error handling here
        return resp

    def get_version(self, **kwargs) -> Union[str, Dict[str, Any]]:
        """
        Retrieves the version information from the aria2 RPC server.

        Args:
            **kwargs: Additional keyword arguments passed to modify behavior.
                - raw (bool, optional): If True, returns the raw response from rpc server as it is.

        Returns:
            Union[str, Dict[str, Any]]: The version information as a string or a dictionary, depending on the 'raw' argument.
        """

        resp = self._request("aria2.getVersion")

        if kwargs.pop("raw", None):
            return resp

        return resp["result"]["version"]
