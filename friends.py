from vk_api.vk_api import VkApiMethod


def get_user_friends(vk: VkApiMethod, user_id: int):
    response = vk.friends.get(user_id=user_id)
    return response['items']