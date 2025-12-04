from misskey import Misskey
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

# トークン直書き
TOKEN = "F7l2B04qPnBI1dxFycZU4MvWRIIoNqEI"
mi = Misskey("https://misskey.stream", i=TOKEN)

def post_message():
    now = datetime.now()
    hour = now.hour

    if hour == 0:
        text = "起爆"
    else:
        text = "爆破" * hour  # 時間に応じて爆破を繰り返す

    mi.notes_create(text=text)
    print(f"{hour}時に投稿: {text}")

# 毎時0分に投稿するスケジューラ
scheduler = BlockingScheduler()
scheduler.add_job(post_message, 'cron', minute=0)

print("BOT起動中...")
scheduler.start()
