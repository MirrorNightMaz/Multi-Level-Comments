"""
需要通过Ajax植入的HTML代码，在此装配
仅供Ajax回调函数使用的数据，不在此装配
"""


from .models import Messages


"""
装载留言总数HTML代码
"""
def load_messages_num_html():
    messages_num = Messages.objects.all().order_by('reply_id', 'send_time').count()
    messages_num_html = str(messages_num) + "&nbsp;"
    return messages_num_html


"""
装载表单错误信息HTML代码
"""
def load_errors_html(message_form):
    errors_html = ""
    for error in message_form.errors['content']:
        errors_html += ("<li style=\"color: red\">\n" +
                        "<strong style=\"color: red\">" +
                        error +
                        "</strong>\n" +
                        "</li>\n")
    return errors_html


"""
装载新留言HTML代码
"""
def load_new_message_html(message, reply_id):
    hour_str = str("%02d" % message.send_time.hour)
    minute_str = str("%02d" % message.send_time.minute)
    if reply_id == -1:
        root_messages_num = Messages.objects.filter(reply_id=-1).count()
        new_message_html = ("<div class=\"vcard\">\n" +
                            "<img id=" +
                            str(message.id) +
                            " class=\"vimg\" src=\"https://gravatar.loli.net/avatar/b6f368e7734816cf9e2dea0d28b82f9f?d=wavatar&amp;v=1.3.10\" />\n" +
                            "<div class=\"vh\">\n" +
                            "<div class=\"vhead\">\n" +
                            "<span class=\"vnick\">留言id：" +
                            str(message.id) +
                            "</span>\n" +
                            "</div>\n" +
                            "<div class=\"vmeta vhead\">\n" +
                            "<span class=\"vsys\"><i class=\"fa fa-cubes\"></i>" +
                            str(root_messages_num) +
                            "层</span>\n" +
                            "<span class=\"vsys\">" +
                            str(message.send_time.year) + "年" +
                            str(message.send_time.month) + "月" +
                            str(message.send_time.day) + "日 " +
                            hour_str + ":" +
                            minute_str +
                            "</span>\n" +
                            "<span class=\"vat\"><i class=\"fa fa-commenting\"></i></span>\n" +
                            "</div>\n" +
                            "<div id=\"insert" +
                            str(message.id) +
                            "\" class=\"vcontent\">\n" +
                            "<p>" +
                            message.content +
                            "</p>\n" +
                            "</div>\n" +
                            "</div>\n")
    else:
        new_message_html = ("<div id=\"insert" +
                            str(message.id) +
                            "\" class=\"vquote\">\n" +
                            "<div class=\"vcard\">\n" +
                            "<img id=" +
                            str(message.id) +
                            " class=\"vimg\" src=\"https://gravatar.loli.net/avatar/a9126a74d0551660d7d638def0b16025?d=wavatar&amp;v=1.3.10\" />\n" +
                            "<div class=\"vh\">\n" +
                            "<div class=\"vhead\">\n" +
                            "<span class=\"vnick\">留言id：" +
                            str(message.id) +
                            "</span>\n" +
                            "<i class=\"fa fa-share\"></i>\n" +
                            "<span class=\"vnick\">留言id：" +
                            str(message.reply_id) +
                            "</span>\n" +
                            "</div>\n" +
                            "<div class=\"vmeta vhead\">\n" +
                            "<span class=\"vsys\">" +
                            str(message.send_time.year) + "年" +
                            str(message.send_time.month) + "月" +
                            str(message.send_time.day) + "日 " +
                            hour_str + ":" +
                            minute_str +
                            "</span>\n" +
                            "<span class=\"vat\"><i class=\"fa fa-commenting\"></i></span>\n" +
                            "</div>\n" +
                            "<div class=\"vcontent\">\n" +
                            "<p>" +
                            message.content +
                            "</p>\n" +
                            "</div>\n" +
                            "</div>\n" +
                            "</div>\n" +
                            "</div>\n")
    return new_message_html