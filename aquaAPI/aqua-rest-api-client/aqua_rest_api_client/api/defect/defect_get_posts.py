from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.api_backend_not_available_error import ApiBackendNotAvailableError
from ...models.api_forbidden_error import ApiForbiddenError
from ...models.api_internal_error import ApiInternalError
from ...models.api_not_found_error import ApiNotFoundError
from ...models.api_post_paginated import ApiPostPaginated
from ...models.api_unauthorized_error import ApiUnauthorizedError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    first_result: Union[Unset, None, int] = 0,
    max_results: Union[Unset, None, int] = 100,
    ascending: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/api/Defect/{id}/Post".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["firstResult"] = first_result

    params["maxResults"] = max_results

    params["ascending"] = ascending

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiPostPaginated,
        ApiUnauthorizedError,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ApiPostPaginated.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ApiForbiddenError.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ApiNotFoundError.from_dict(response.json())

        return response_404
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


def _build_response(*, client: Client, response: httpx.Response) -> Response[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiPostPaginated,
        ApiUnauthorizedError,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    first_result: Union[Unset, None, int] = 0,
    max_results: Union[Unset, None, int] = 100,
    ascending: Union[Unset, None, bool] = True,
) -> Response[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiPostPaginated,
        ApiUnauthorizedError,
    ]
]:
    """Get posts

     Get posts (also known as comments or discussions) of the defect with the id.

    Args:
        id (int):
        first_result (Union[Unset, None, int]):
        max_results (Union[Unset, None, int]):  Default: 100.
        ascending (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiPostPaginated, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        first_result=first_result,
        max_results=max_results,
        ascending=ascending,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    first_result: Union[Unset, None, int] = 0,
    max_results: Union[Unset, None, int] = 100,
    ascending: Union[Unset, None, bool] = True,
) -> Optional[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiPostPaginated,
        ApiUnauthorizedError,
    ]
]:
    """Get posts

     Get posts (also known as comments or discussions) of the defect with the id.

    Args:
        id (int):
        first_result (Union[Unset, None, int]):
        max_results (Union[Unset, None, int]):  Default: 100.
        ascending (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiPostPaginated, ApiUnauthorizedError]]
    """

    return sync_detailed(
        id=id,
        client=client,
        first_result=first_result,
        max_results=max_results,
        ascending=ascending,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    first_result: Union[Unset, None, int] = 0,
    max_results: Union[Unset, None, int] = 100,
    ascending: Union[Unset, None, bool] = True,
) -> Response[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiPostPaginated,
        ApiUnauthorizedError,
    ]
]:
    """Get posts

     Get posts (also known as comments or discussions) of the defect with the id.

    Args:
        id (int):
        first_result (Union[Unset, None, int]):
        max_results (Union[Unset, None, int]):  Default: 100.
        ascending (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiPostPaginated, ApiUnauthorizedError]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        first_result=first_result,
        max_results=max_results,
        ascending=ascending,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    first_result: Union[Unset, None, int] = 0,
    max_results: Union[Unset, None, int] = 100,
    ascending: Union[Unset, None, bool] = True,
) -> Optional[
    Union[
        ApiBackendNotAvailableError,
        ApiForbiddenError,
        ApiInternalError,
        ApiNotFoundError,
        ApiPostPaginated,
        ApiUnauthorizedError,
    ]
]:
    """Get posts

     Get posts (also known as comments or discussions) of the defect with the id.

    Args:
        id (int):
        first_result (Union[Unset, None, int]):
        max_results (Union[Unset, None, int]):  Default: 100.
        ascending (Union[Unset, None, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiBackendNotAvailableError, ApiForbiddenError, ApiInternalError, ApiNotFoundError, ApiPostPaginated, ApiUnauthorizedError]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            first_result=first_result,
            max_results=max_results,
            ascending=ascending,
        )
    ).parsed
