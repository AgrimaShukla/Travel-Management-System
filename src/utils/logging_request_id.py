from shortuuid import ShortUUID

def get_request_id():
    return ShortUUID().random(10)