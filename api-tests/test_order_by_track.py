import requests
import configuration
import data


def test_create_order_and_get_by_track_returns_200():
    # Создаём заказ
    create_url = configuration.BASE_URL + configuration.CREATE_ORDER_PATH
    create_response = requests.post(create_url, json=data.order_body)

    assert create_response.status_code in (200, 201), (
        f"Create order failed: {create_response.status_code}, {create_response.text}"
    )

    track = create_response.json().get("track")
    assert track is not None, f"No track in response: {create_response.json()}"

    # Получаем заказ по треку
    get_url = configuration.BASE_URL + configuration.GET_ORDER_BY_TRACK_PATH
    get_response = requests.get(get_url, params={"t": track})

    assert get_response.status_code == 200, (
        f"Get order failed: {get_response.status_code}, {get_response.text}"
    )
