import os
from misskey import Misskey
from datetime import datetime, timezone, timedelta

# ======================
# Misskey設定（環境変数から読み込む）
TOKEN = os.getenv("MISSKEY_TOKEN")
INSTANCE_URL = "https://misskey.stream"
# ======================

mi = Misskey(INSTANCE_URL, i=TOKEN)

def post_message():
    JST = timezone(timedelta(hours=9))
    now = datetime.now(JST)
    hour = now.hour

    if hour == 0:
        text = "起爆"
    else:
        text = "爆破" * hour

    mi.notes_create(text=text)
    print(f"{hour}時に投稿: {text}")

post_message()
