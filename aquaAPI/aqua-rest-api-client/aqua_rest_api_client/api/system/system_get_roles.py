from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_internal_error import ApiInternalError
from ...models.api_role_id_name import ApiRoleIdName
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/System/Role".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, List["ApiRoleIdName"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ApiRoleIdName.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ApiUnauthorizedError.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ApiInternalError.from_dict(response.json())

        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = ApiBackendNotAvailableError.from_dict(response.json())

        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, List["ApiRoleIdName"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, List["ApiRoleIdName"]]]:
    """Get roles as list

     Get a list with all roles which are defined in the system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, List['ApiRoleIdName']]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, List["ApiRoleIdName"]]]:
    """Get roles as list

     Get a list with all roles which are defined in the system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, List['ApiRoleIdName']]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, List["ApiRoleIdName"]]]:
    """Get roles as list

     Get a list with all roles which are defined in the system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, List['ApiRoleIdName']]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, List["ApiRoleIdName"]]]:
    """Get roles as list

     Get a list with all roles which are defined in the system.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiInternalError, ApiUnauthorizedError, List['ApiRoleIdName']]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
