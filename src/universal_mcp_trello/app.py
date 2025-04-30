from typing import Annotated, Any

from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration


class TrelloApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='trelloapp', integration=integration, **kwargs)
        self.base_url = "{{baseURL}}boards"


    def get1_boards_id(self, key: Annotated[Any, ''] = None, token: Annotated[Any, ''] = None) -> Any:
        """
        GET /1/boards/{id}. Get Boards

        Tags: Board

        """

        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "key": key,
                "token": token,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get1_boards_id_lists(self, key: Annotated[Any, ''] = None, token: Annotated[Any, ''] = None) -> Any:
        """
        GET /1/boards/{id}/lists. GET /1/boards/{id}/lists

        Tags: Board

        """

        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "key": key,
                "token": token,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post1_cards(self, desc: Annotated[Any, ''] = None, idBoard: Annotated[Any, ''] = None, idList: Annotated[Any, ''] = None, key: Annotated[Any, ''] = None, name: Annotated[Any, ''] = None, token: Annotated[Any, ''] = None) -> Any:
        """
        POST /1/cards. POST /1/cards

        Tags: Cards

        """

        request_body = {
            "desc": desc,
            "idBoard": idBoard,
            "idList": idList,
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "key": key,
                "token": token,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get1_cards_id(self, key: Annotated[Any, ''] = None, token: Annotated[Any, ''] = None) -> Any:
        """
        GET /1/cards/{id}. GET /1/cards/{id}

        Tags: Cards

        """

        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "key": key,
                "token": token,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def put1_cards_id(self, desc: Annotated[Any, ''] = None, key: Annotated[Any, ''] = None, name: Annotated[Any, ''] = None, token: Annotated[Any, ''] = None) -> Any:
        """
        PUT /1/cards/{id}. PUT /1/cards/{id}

        Tags: Cards

        """

        request_body = {
            "desc": desc,
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "key": key,
                "token": token,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete1_cards_id(self, key: Annotated[Any, ''] = None, token: Annotated[Any, ''] = None) -> Any:
        """
        DELETE /1/cards/{id}. DELETE /1/cards/{id}

        Tags: Cards

        """

        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "key": key,
                "token": token,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()


    def list_tools(self):
        return [

            self.get1_boards_id,
            self.get1_boards_id_lists,
            self.post1_cards,
            self.get1_cards_id,
            self.put1_cards_id,
            self.delete1_cards_id
        ]
