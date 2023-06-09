# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ...errors.unprocessable_entity_error import UnprocessableEntityError
from ...types.http_validation_error import HttpValidationError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AgentClient:
    def __init__(self, *, environment: str, token: typing.Optional[str] = None):
        self._environment = environment
        self._token = token

    def list_all_agents(self) -> typing.Any:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", "api/v1/agents"),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_agent(
        self,
        *,
        name: str,
        type: str,
        llm: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        has_memory: typing.Optional[bool] = OMIT,
        prompt_id: typing.Optional[str] = OMIT,
    ) -> typing.Any:
        _request: typing.Dict[str, typing.Any] = {"name": name, "type": type}
        if llm is not OMIT:
            _request["llm"] = llm
        if has_memory is not OMIT:
            _request["hasMemory"] = has_memory
        if prompt_id is not OMIT:
            _request["promptId"] = prompt_id
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment}/", "api/v1/agents"),
            json=jsonable_encoder(_request),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_agent(self, agent_id: str) -> typing.Any:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment}/", f"api/v1/agents/{agent_id}"),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def patch_agent(self, agent_id: str, *, request: typing.Dict[str, typing.Any]) -> typing.Any:
        _response = httpx.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._environment}/", f"api/v1/agents/{agent_id}"),
            json=jsonable_encoder(request),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_agent(self, agent_id: str) -> typing.Any:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._environment}/", f"api/v1/agents/{agent_id}"),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def prompt_agent(
        self, agent_id: str, *, input: typing.Dict[str, typing.Any], has_streaming: typing.Optional[bool] = OMIT
    ) -> typing.Any:
        _request: typing.Dict[str, typing.Any] = {"input": input}
        if has_streaming is not OMIT:
            _request["has_streaming"] = has_streaming
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment}/", f"api/v1/agents/{agent_id}/predict"),
            json=jsonable_encoder(_request),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAgentClient:
    def __init__(self, *, environment: str, token: typing.Optional[str] = None):
        self._environment = environment
        self._token = token

    async def list_all_agents(self) -> typing.Any:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment}/", "api/v1/agents"),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_agent(
        self,
        *,
        name: str,
        type: str,
        llm: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        has_memory: typing.Optional[bool] = OMIT,
        prompt_id: typing.Optional[str] = OMIT,
    ) -> typing.Any:
        _request: typing.Dict[str, typing.Any] = {"name": name, "type": type}
        if llm is not OMIT:
            _request["llm"] = llm
        if has_memory is not OMIT:
            _request["hasMemory"] = has_memory
        if prompt_id is not OMIT:
            _request["promptId"] = prompt_id
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment}/", "api/v1/agents"),
                json=jsonable_encoder(_request),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_agent(self, agent_id: str) -> typing.Any:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment}/", f"api/v1/agents/{agent_id}"),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def patch_agent(self, agent_id: str, *, request: typing.Dict[str, typing.Any]) -> typing.Any:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PATCH",
                urllib.parse.urljoin(f"{self._environment}/", f"api/v1/agents/{agent_id}"),
                json=jsonable_encoder(request),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_agent(self, agent_id: str) -> typing.Any:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "DELETE",
                urllib.parse.urljoin(f"{self._environment}/", f"api/v1/agents/{agent_id}"),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def prompt_agent(
        self, agent_id: str, *, input: typing.Dict[str, typing.Any], has_streaming: typing.Optional[bool] = OMIT
    ) -> typing.Any:
        _request: typing.Dict[str, typing.Any] = {"input": input}
        if has_streaming is not OMIT:
            _request["has_streaming"] = has_streaming
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment}/", f"api/v1/agents/{agent_id}/predict"),
                json=jsonable_encoder(_request),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Any, _response.json())  # type: ignore
        if _response.status_code == 422:
            raise UnprocessableEntityError(pydantic.parse_obj_as(HttpValidationError, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
