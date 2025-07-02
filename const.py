# いろんな定数を定義するファイル
# 授業内で設定は伝えます

# 適当なユーザ名（要入力）
USER_NAME = "dang0"

# 1番マーカ（画面マーカ）の大きさ（ミリメートル）
MARKER_SIZE_1 = 50

# それ以外のマーカの大きさ（ミリメートル）
MARKER_SIZE_ANY = 50

# シーンの持ち主
SCENE_NAMESPACE = "dang0"

# シーン名
SCENE_NAME = "lecture-202507"

# openai api kay
# 事故ってgitにアップロードしないようにignoreしたファイルから読む
OPENAI_API_KEY = ""
with open("api-key") as f:
    OPENAI_API_KEY = f.read()
