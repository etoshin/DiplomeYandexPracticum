# Павел Нечитайло, 18-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request


def test_get_order_by_track():
    # Создаем заказ
    response_order = sender_stand_request.post_new_order(data.order_body)
    track = response_order.json()["track"]
    print("Заказ создан. Трека заказа:", track)

    # Получаем заказ по треку
    response_order_by_track = sender_stand_request.get_order_by_track(track)

    assert response_order_by_track.status_code == 200
    order_data = response_order_by_track.json()
    print("Заказ:")
    print(order_data)
