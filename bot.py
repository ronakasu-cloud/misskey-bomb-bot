name: Misskey Bomb Bot

on:
  schedule:
    - cron: "0 * * * *"   # 毎時0分に実行
  workflow_dispatch:

jobs:
  post:
    runs-on: ubuntu-latest
    steps:
      - name: Generate message
        id: gen
        run: |
          HOUR=$(date -u +"%H")
          if [ "$HOUR" = "00" ]; then
            TEXT="起爆"
          else
            BOMBS=$(printf "爆破%.0s" $(seq 1 $HOUR))
            TEXT="$BOMBS"
          fi
          echo "text=$TEXT" >> $GITHUB_OUTPUT

      - name: Post to Misskey
        run: |
          curl -X POST https://misskey.stream/api/notes/create \
          -H "Content-Type: application/json" \
          -d "{\"i\": \"${{ secrets.MISSKEY_TOKEN }}\", \"text\": \"${{ steps.gen.outputs.text }}\"}"
