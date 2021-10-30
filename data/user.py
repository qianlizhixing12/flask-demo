users = [
    {
        "id": "001",
        "password": "吃俺老孙一棒",
        "name": "孙悟空",
        "age": "500",
        "skill": ["七十二变", "火眼金睛"]
    },
    {
        "id": "002",
        "password": "南无阿弥陀佛",
        "name": "唐三藏",
        "age": "30",
        "skill": ["紧箍咒"]
    },
]


def get_users():
    return users


def get_users_map():
    return {user["id"]: user for user in users}


__all__ = [get_users, get_users_map]
