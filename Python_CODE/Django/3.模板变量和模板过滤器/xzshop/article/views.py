from django.shortcuts import render
from datetime import datetime

def detail(request, article_id):
    content = '''
     “真是时代的眼泪，好多年没有买过这类品牌了，以前还挺火的。”杭州白领李小姐向记者展示了她的宝贝，大大小小的水晶饰品摆满了一整片，“这是限定熊猫款，还有当年很火的海洋之心，这顶灰姑娘的皇冠，结婚的时候还戴过，说实话有点后悔，施华洛世奇都是人造水晶，放到现在一点价值也没有，回收也没人要，要是结婚的时候买的是黄金头冠，现在可就值钱了。”李小姐为年轻时“投资失败”而扼腕。
同样陷入尴尬境地的还有少女的魔法盒——潘多拉。这些爆火的轻奢饰品品牌似乎一夜失宠，店铺门口门可罗雀，不少网友都在社交媒体感慨——“真是时代的眼泪”“还有大冤种在买吗？”“又丑又贵。”“还不如买黄金！”
轻奢珠宝品牌在中国市场的两大巨头潘多拉和施华洛世奇曾是年轻女孩们的造梦机，凭借着高大上的专柜体验和层出不穷的营销手段维持着“高端珠宝”的形象，可随着时间发展，中国消费者更注重性价比和产品品质本身，轻奢饰品逐渐失去了品牌光环。

    '''
    return render(request, "article/detail.html", context={
        "content": content,
        "name": "xz_official",
        "age": 18,
        "age1": 19,
        "desc": None,
        "now": datetime.now(),
        "html": "<h1>Hi xz_official!!</h1>",
        "float": 12.46521895
    })