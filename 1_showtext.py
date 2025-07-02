# arena xrのモジュール
from arena import *

# const.pyの定数群をインポート
from const import *

# 今回は公式のarenaxr.orgが提供してくれているサーバを指定
# const.pyにかかれているシーン情報をロード
# headless=Trueにすることでユーザの認証方法を変更（GitHub Codespaceなので通常の認証だとうまくいかない）
scene = Scene(host="arenaxr.org", scene=SCENE_NAME, namespace=SCENE_NAMESPACE, headless=True)

# マーカの情報
marker = Armarker(
    # マーカ1番
    markerid="1",
    # apriltagの36h11という名前のマーカを使う
    markertype="apriltag_36h11",
    # マーカの大きさ（ミリメートル）: const.pyに定義
    size=MARKER_SIZE_1
)

# 追加するテキスト
new_text = Text(
    # オブジェクト識別のためのID
    object_id=f"{USER_NAME}_text",
    # 内容
    value="Hello, World!",
    # 中央寄せ（left, rightなどでもOK）
    align="center",
    # フォント
    font="mozillavr",
    # マーカとの相対位置（メートル）
    position=(0, 0, -0.1),
    # 大きさ (メートル)
    scale=(0.5, 0.5, 0.5),
    # 色（R,G,B 0~255）
    color=(255, 0, 0),
    # 永続化 (あとからシーンに入ってきた人も見えるようにする)
    persist=True,
    # 作成したマーカ情報を付加
    armarker=marker
)

# シーンのロード時一度だけ実行する関数として指定
@scene.run_once
def add_text():
    # 作成したオブジェクトをシーンに追加
    scene.add_object(new_text)

# そのままだとオブジェクトが残り続けてしまうので，プログラム終了したときに消す
def del_text(scene):
    scene.delete_object(new_text)

scene.end_program_callback = del_text

# 処理を実行
scene.run_tasks()

