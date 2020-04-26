var reply_buttons = document.getElementsByClassName("vat");
var div = document.getElementById("reply_id");
var h1 = document.getElementById("id");

function ReplyButtonClick(id)
{
    div.style.display = 'block';
    h1.className = id;
    h1.innerHTML = "<i class=\"fa fa-share\"></i> 留言id：" + id;
    location.href = "#reply_id";
}

function WindowUnload()
{
    div.style.display = 'none';
    h1.className = '-1';
    h1.innerHTML = "<i class=\"fa fa-share\"></i> 留言id：-1";
}

window.addEventListener("unload", WindowUnload);

for(var i = 0; i < reply_buttons.length; i++)
{
    reply_buttons[i].addEventListener("click", function () {ReplyButtonClick(this.title)});
}