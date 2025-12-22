import requests
import configuration

def create_order(order_body):
    url = configuration.BASE_URL + configuration.CREATE_ORDER_PATH
    return requests.post(url, json=order_body)

def get_order_by_track(track):
    url = configuration.BASE_URL + configuration.GET_ORDER_BY_TRACK_PATH
    return requests.get(url, params={"t": track})
