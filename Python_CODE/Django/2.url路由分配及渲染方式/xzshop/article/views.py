from django.shortcuts import render
from django.http import HttpResponse


def detail(request, article_id):
    # 通过article_id去查询数据获取与之对应的文章
    # article = """
    # <div>
    #     <h1>你好!</h1>
    #     <div>这是第一个template</div>
    # </div>
    #
    # """
    # return HttpResponse('文章详情:  '+str(article_id))
    # return HttpResponse(article)

    return render(request, 'article.html')  # 需要配置