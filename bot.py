from misskey import Misskey

# ★トークン直書き版（あなたのトークン）
TOKEN = "F7l2B04qPnBI1dxFycZU4MvWRIIoNqEI"

# インスタンスURL（スペル注意）
mi = Misskey("https://misskey.stream", i=TOKEN)

# 投稿内容（固定文：爆破）
mi.notes_create(text="爆破")
