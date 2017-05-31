import leancloud


leancloud.init("4pg1MkOjOpccIENtzRijjjd3-9Nh9j0Va", master_key="m5r8SA26l8qUAOqMn2pCckTj")


def push_tencent_message(installation_id, message_content):
    query = leancloud.Query('_Installation')
    return leancloud.push.send(message_content, where=query.equal_to("installationId", installation_id))


def prepare_message_content(title, content, action, silent):
    message_content = dict()
    message_content['title'] = title
    message_content['alert'] = content
    if action is not None:
        message_content['action'] = action
    if silent is not None:
        message_content['silent'] = silent
    return message_content


def prepare_message_callback_conn_err(transfer_id):
    msg_content = prepare_message_content(None, None, "com.clverpanda.nfshare.connunavailable", True)
    msg_content['id'] = transfer_id
    return msg_content


def prepare_message_callback_upload_done(transfer_related_data):
    msg_content = prepare_message_content("收到来自云端的任务", "任务已经放入任务列表", "com.clverpanda.nfshare.uploaddone", None)
    msg_content['description'] = transfer_related_data
    return msg_content


def push_normal_message(installation_id, title, content):
    msg_content = prepare_message_content(title, content, None, None)
    return push_tencent_message(installation_id, msg_content)


def push_conn_err_message(installation_id, transfer_id):
    msg_content = prepare_message_callback_conn_err(transfer_id)
    return push_tencent_message(installation_id, msg_content)


def push_upload_done_message(installation_id, transfer_related_data):
    msg_content = prepare_message_callback_upload_done(transfer_related_data)
    return push_tencent_message(installation_id, msg_content)


if __name__ == "__main__":
    # back_content = push_normal_message("4dc9a3412a2a44cdc1b90c2050ea14bb", "测试一下", "水水水水水")
    # back_content = push_conn_err_message("4dc9a3412a2a44cdc1b90c2050ea14bb", 4)
    back_content = push_upload_done_message("4dc9a3412a2a44cdc1b90c2050ea14bb",
                                            "{\"fileName\":\"Screenshot_1495614835.png\",\"filePath\":\"/storage/"
                                            "emulated/0/Download/Screenshot_1495614835.png\",\"space\":817143808}")
    print(back_content)
