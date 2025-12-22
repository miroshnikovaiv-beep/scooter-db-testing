# Ирина Мирошникова, 38-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request as stand

def test_create_order_returns_track():
    response = stand.create_order(data.order_body)
    assert response.status_code in (200, 201)
    assert response.json().get("track") is not None

def test_get_order_by_track_returns_200():
    create_response = stand.create_order(data.order_body)
    track = create_response.json().get("track")

    get_response = stand.get_order_by_track(track)
    assert get_response.status_code == 200

