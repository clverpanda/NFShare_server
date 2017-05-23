import leancloud


leancloud.init("4pg1MkOjOpccIENtzRijjjd3-9Nh9j0Va", master_key="m5r8SA26l8qUAOqMn2pCckTj")


def push_tencent_message(installation_id, title, content, action, silent):
    message_content = dict()
    message_content['title'] = title
    message_content['alert'] = content
    if action is not None:
        message_content['action'] = action
    if silent is not None:
        message_content['silent'] = silent
    query = leancloud.Query('_Installation')
    return leancloud.push.send(message_content, where=query.equal_to("installationId", installation_id))


def push_normal_message(installation_id, title, content):
    return push_tencent_message(installation_id, title, content, None, None)


if __name__ == "__main__":
    back_content = push_normal_message("4dc9a3412a2a44cdc1b90c2050ea14bb", "测试一下", "水水水水水")
    print(back_content)
