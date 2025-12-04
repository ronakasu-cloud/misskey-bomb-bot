from misskey import Misskey
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

# ====== 設定部分 ======
TOKEN = "F7l2B04qPnBI1dxFycZU4MvWRIIoNqEI"  # あなたのアクセストークン
INSTANCE_URL = "https://misskey.stream"       # MisskeyインスタンスURL
# ====================

# Misskeyに接続
mi = Misskey(INSTANCE_URL, i=TOKEN)

def post_message():
    """
    毎時0分に投稿する関数
    0時: 起爆
    1時以降: 爆破を時間分繰り返す
    """
    now = datetime.now()
    hour = now.hour

    if hour == 0:
        text = "起爆"
    else:
        text = "爆破" * hour

    try:
        mi.notes_create(text=text)
        print(f"{hour}時に投稿成功: {text}")
    except Exception as e:
        print(f"投稿失敗: {e}")

# スケジューラで毎時0分に実行
scheduler = BlockingScheduler()
scheduler.add_job(post_message, 'cron', minute=0)

print("BOT起動中...（毎時0分に自動投稿）")
scheduler.start()
