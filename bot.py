from misskey import Misskey
from datetime import datetime

# ======================
# Misskey設定
TOKEN = "F7l2B04qPnBI1dxFycZU4MvWRIIoNqEI"  # 取得済みトークン
INSTANCE_URL = "https://misskey.stream"       # インスタンスURL
# ======================

mi = Misskey(INSTANCE_URL, i=TOKEN)

def post_message():
    now = datetime.now()
    hour = now.hour
    if hour == 0:
        text = "起爆"
    else:
        text = "爆破" * hour
    mi.notes_create(text=text)
    print(f"{hour}時に投稿: {text}")

# GitHub Actionsで呼ばれるので、スケジューラは不要
post_message()
