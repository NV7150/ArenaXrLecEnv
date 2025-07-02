# arena xrのモジュール
from arena import *

from const import *

# 保存した画像のパスを入力
image_path = "localdata/Very.png"

# シーンのロード
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


# 画像のアップロード：アップロードした後のurlが返ってくる
image_url = scene.upload_store_file(image_path)
print(f"Image uploaded to {image_url}")

# 画像を作成
new_image = Image(
    # オブジェクト識別のためのID
    object_id = f"{USER_NAME}_image",
    # 内容：アップロードする
    url=image_url,
    # マーカとの相対位置（メートル）
    position=(0, 0, -0.1),
    # 大きさ (メートル)
    scale=(0.5, 0.5, 0.5),
    # 永続化
    persist=True,
    # 作成したマーカ情報を付加
    armarker=marker
)

# あとはテキストと一緒：オブジェクトを追加・削除

@scene.run_once
def add_image():
    scene.add_object(new_image)

def del_image(scene):
    scene.delete_object(new_image)
scene.end_program_callback = del_image

scene.run_tasks()
