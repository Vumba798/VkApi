import vk_api

from User import User
from friends import *
from saver import save_to_file

vk_token: str = "YOUR_TOKEN"
vk_login: str = "YOUR LOGIN"
vk_password: str = "YOUR PASSWORD"

def auth_handler() -> (str, bool):
    remember_device = False
    key = input("Enter auth code: ")
    return key, remember_device

vk_session = vk_api.VkApi(login=vk_login,
                          password=vk_password,
                          token=vk_token,
                          auth_handler=auth_handler,
                          app_id=6121396)

vk_session.auth(token_only=True)
vk: VkApiMethod = vk_session.get_api()

if __name__ == '__main__':
    userId: int = 0
    userName: str = "user name"
    user: User = User(userId,
                      userName,
                      get_user_friends(vk, userId))
    filename = "user.json"
    save_to_file(user.__dict__, filename)
