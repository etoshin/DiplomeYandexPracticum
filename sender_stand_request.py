import configuration
import requests
import data


# Создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки


response = post_new_order(data.order_body)
print(response.status_code)


#  Получение заказа по номеру
def get_order_by_track(order_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(order_number),
                        headers=data.headers)
