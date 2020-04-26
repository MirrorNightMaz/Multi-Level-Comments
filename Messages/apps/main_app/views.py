import collections
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .forms import MessageForm
from .models import Messages
from .messages_forest import create_messages_forest, pre_order_messages_forest
from .ajax_html import load_messages_num_html, load_errors_html, load_new_message_html

# Create your views here.


class HandleMessages(View):
    """处理留言视图逻辑
    """
    def get(self, request):
        message_form = MessageForm()
        messages = Messages.objects.all().order_by('reply_id', 'send_time')
        messages_num = messages.count()
        messages_forest = collections.OrderedDict()
        for message in messages:
            next_find = create_messages_forest(message, messages_forest)
            if next_find:
                create_messages_forest(message, next_find)
            else:
                create_messages_forest(message, messages_forest)
        messages_list = []
        pre_order_messages_forest(messages_forest, messages_list)
        layers_list = []
        layer = 1
        for message in messages_list:
            if(message.reply_id == -1):
                layers_list.append(layer)
                layer += 1
            else:
                layers_list.append(0)
        kwargs = {
            'message_form': message_form,
            'messages_list_layers_list': zip(messages_list, layers_list),
            'messages_num': messages_num,
        }
        return render(request, 'main_app/messages.html', kwargs)

    def post(self, request):
        reply_id = request.POST.get('reply_id')
        if reply_id == '-1':
            reply_id = -1
        else:
            reply_id = int(reply_id)
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.reply_id = reply_id
            message.save()
            location_href = "#" + str(message.id)
            if reply_id == -1:
                insert_id = None
            else:
                same_reply_messages = Messages.objects.filter(reply_id=reply_id).order_by('id')
                if len(same_reply_messages) == 1:
                    insert_id = reply_id
                else:
                    insert_id = same_reply_messages[len(same_reply_messages) - 2].id
                insert_id = "#insert" + str(insert_id)
            kwargs = {
                'verify_result': 'valid',
                'location_href': location_href,
                'insert_id': insert_id,
                'new_message_html': load_new_message_html(message, reply_id),
                'messages_num_html': load_messages_num_html(),
            }
            return JsonResponse(kwargs)
        else:
            kwargs = {
                'verify_result': 'invalid',
                'errors_html': load_errors_html(message_form),
            }
            return JsonResponse(kwargs)



