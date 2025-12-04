from misskey import Misskey
import os

# GitHub Actions の秘密変数からトークン取得
token = os.getenv("MISSKEY_TOKEN")

# インスタンスURL（正しい綴り）
mi = Misskey("https://misskey.stream")

# ログイン
mi.login(token=token)

# 投稿内容
mi.notes_create(text="爆破")
