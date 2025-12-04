from misskey import Misskey
import os

# GitHub Actions の秘密変数からトークン取得
token = os.getenv("MISSKEY_TOKEN")

# あなたのインスタンスURL
mi = Misskey("https://miskey.stream")

# ログイン
mi.login(token=token)

# 投稿内容（爆破）
mi.notes_create(text="爆破")
