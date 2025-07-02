import base64
# openaiのモジュール
from openai import OpenAI

# const.pyの定数群をインポート
from const import *

# 画像生成させる
client = OpenAI(api_key=OPENAI_API_KEY)

prompt = "Very delicious sushi"  # プロンプト

print(f"generating image: {prompt} ...")
response = client.images.generate(
  model="dall-e-3",  # モデル
  prompt= prompt,
  n=1,  # 生成数(1で固定)
  size="1024x1024",  # 解像度 dall-e-3では1024x1024、1792x1024、1024x1792
  response_format="b64_json",  # b64_jsonで画像を返す
  quality="hd",  # 品質 standard or hd
  style="natural"  # スタイル vivid or natural
)

# 画像名を作成：タイピングの容易さから１単語目を抽出するだけ
image_path = f"localdata/{prompt.split(' ')[0]}.png"

# 生成した画像の保存
with open(image_path, "wb") as f:
    f.write(base64.b64decode(response.data[0].b64_json))

print(f"image saved to : {image_path}!")
