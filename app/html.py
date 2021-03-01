from flask import Blueprint, make_response,current_app

html = Blueprint("html", __name__)


@html.route("/<re(r'.*'):html_file_name>")
def get_html(html_file_name):
    if not html_file_name:
        html_file_name = "index.html"

    if html_file_name != "favicon.ico":
        html_file_name = "html/"+html_file_name

    # flask 提供的返回静态文件的方法
    resp = make_response(current_app.send_static_file(html_file_name))
    return resp
