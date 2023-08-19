from http import HTTPStatus

from fastapi.testclient import TestClient
from httpx import Response


class TestRestApi:
    ############
    # Retrieve #
    ############
    def test_get_existing_BTC_address_RETURNS_200_and_BTC_address(self, client: TestClient):
        # TODO: Should prepopulate db instead of creating an address to retrieve it.
        body = {"coin_code": "BTC"}
        client.post(url=f"/address", json=body)

        res: Response = client.get(url=f"/address/0")

        assert res.status_code == HTTPStatus.OK

    def test_get_existing_ETH_address_RETURNS_200_and_BTC_address(self, client: TestClient):
        # TODO: Should prepopulate db instead of creating an address to retrieve it.
        body = {"coin_code": "ETH"}
        client.post(url=f"/address", json=body)
        res: Response = client.get(url=f"/address/0")

        assert res.status_code == HTTPStatus.OK

    ##########
    # Create #
    ##########
    def test_create_BTC_address_WITH_non_existing_master_key_RETURNS_201_and_generates_master_key(self, client: TestClient):
        body = {"coin_code": "BTC"}
        res = client.post(url=f"/address", json=body)

        assert res.status_code == HTTPStatus.CREATED

    def test_create_ETH_address_WITH_non_existing_master_key_RETURNS_201_and_generates_master_key(self, client: TestClient):
        body = {"coin_code": "ETH"}
        res = client.post(url=f"/address", json=body)

        assert res.status_code == HTTPStatus.CREATED

    #########
    # List #
    #########
    def test_list_address_RETURNS_200_and_BTC_addresses(self, client: TestClient):
        # TODO: Should prepopulate db instead of creating an address to retrieve it.
        body = {"coin_code": "ETH"}
        client.post(url=f"/address", json=body)

        res: Response = client.get(url=f"/address")

        assert res.status_code == HTTPStatus.OK
        assert len(res.json()) > 0
