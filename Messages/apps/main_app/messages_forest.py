import collections
from .models import Messages


def create_messages_forest(message, now_find):
    """递归创建留言森林

    参数 message：接收输入序列
    参数 now_find：当前的搜索对象
    返回值：下一步的搜索对象
    备注：对留言森林结果的保存，利用了Python变量的共享引用
    """
    if message.reply_id == -1:
        now_find[message] = collections.OrderedDict()
        return now_find
    else:
        message_reply = Messages.objects.get(id=message.reply_id)
        if message_reply in now_find:
            now_find[message_reply][message] = collections.OrderedDict()
            return now_find
        else:
            for childs_forest in now_find.values():
                if childs_forest:
                    create_messages_forest(message, childs_forest)


def pre_order_messages_forest(messages_forest, messages_list):
    """先根遍历留言森林

    参数 messages_forest：留言森林
    参数 messages_list：先根遍历得出的序列
    返回值：因为对messages_list作原位置修改，利用了Python变量的共享引用，无需返回值
    """
    for message_root, childs_forest in messages_forest.items():
        if message_root:
            messages_list.append(message_root)
            if childs_forest:
                pre_order_messages_forest(childs_forest, messages_list)




