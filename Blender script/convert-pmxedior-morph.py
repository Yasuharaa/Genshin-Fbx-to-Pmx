import bpy

# set selected object as active and call its shape keys
obj = bpy.context.object
shape_keys = obj.data.shape_keys.key_blocks

# for Brow
for brow_key in shape_keys:
    brow_key.name = brow_key.name.replace("0003_Brow_morph0", "Brow_Default")
    brow_key.name = brow_key.name.replace("0003_Brow_morph1", "困る左")
    brow_key.name = brow_key.name.replace("0003_Brow_morph2", "困る右")
    brow_key.name = brow_key.name.replace("0003_Brow_morph3", "にこり左")
    brow_key.name = brow_key.name.replace("0003_Brow_morph4", "にこり右")
    brow_key.name = brow_key.name.replace("0003_Brow_morph5", "怒り左")
    brow_key.name = brow_key.name.replace("0003_Brow_morph6", "怒り右")
    brow_key.name = brow_key.name.replace("0003_Brow_morph7", "恥ずかしい左")
    brow_key.name = brow_key.name.replace("0003_Brow_morph8", "恥ずかしい右")
    brow_key.name = brow_key.name.replace("0003_Brow_morph9", "上左")
    brow_key.name = brow_key.name.replace("0003_Brow_morph10", "上右")
    brow_key.name = brow_key.name.replace("0003_Brow_morph11", "下左")
    brow_key.name = brow_key.name.replace("0003_Brow_morph12", "下右")
    brow_key.name = brow_key.name.replace("0003_Brow_morph13", "に近い左")
    brow_key.name = brow_key.name.replace("0003_Brow_morph14", "に近い右")

# for Face
for mouth_key in shape_keys:
    mouth_key.name = mouth_key.name.replace("0005_Face_morph0", "Mouth_Default")
    mouth_key.name = mouth_key.name.replace("0005_Face_morph1", "あ")
    mouth_key.name = mouth_key.name.replace("0005_Face_morph2", "い")
    mouth_key.name = mouth_key.name.replace("0005_Face_morph3", "にやり")
    mouth_key.name = mouth_key.name.replace("0005_Face_morph4", "ワ")
    mouth_key.name = mouth_key.name.replace("0005_Face_morph5", "ん")
    mouth_key.name = mouth_key.name.replace("0005_Face_morph6", "い１")
    mouth_key.name = mouth_key.name.replace("0005_Face_morph7", "い２")
    mouth_key.name = mouth_key.name.replace("0005_Face_morph8", "あ２")
    mouth_key.name = mouth_key.name.replace("0005_Face_morph9", "にやり２")
    mouth_key.name = mouth_key.name.replace("0005_Face_morph10", "にやり３")
    mouth_key.name = mouth_key.name.replace("0005_Face_morph11", "ω")
    mouth_key.name = mouth_key.name.replace("0005_Face_morph12", "てへぺろ")
    mouth_key.name = mouth_key.name.replace("0005_Face_morph13", "ぺろっ")
    mouth_key.name = mouth_key.name.replace("0005_Face_morph14", "口横広げ")
    mouth_key.name = mouth_key.name.replace("0005_Face_morph15", "口横狭め")
    mouth_key.name = mouth_key.name.replace("0005_Face_morph16", "舌広げ")

# for Face_Eye
for eye_key in shape_keys:
    eye_key.name = eye_key.name.replace("0006_Face_Eye_morph0", "Eye_Default")
    eye_key.name = eye_key.name.replace("0006_Face_Eye_morph1", "ウィンク")
    eye_key.name = eye_key.name.replace("0006_Face_Eye_morph2", "ウィンク")
    eye_key.name = eye_key.name.replace("0006_Face_Eye_morph3", "ウィンク右")
    eye_key.name = eye_key.name.replace("0006_Face_Eye_morph4", "ウィンク２")
    eye_key.name = eye_key.name.replace("0006_Face_Eye_morph5", "ｳｨﾝｸ２右")
    eye_key.name = eye_key.name.replace("0006_Face_Eye_morph6", "なごみ左")
    eye_key.name = eye_key.name.replace("0006_Face_Eye_morph7", "なごみ右")
    eye_key.name = eye_key.name.replace("0006_Face_Eye_morph8", "びっくり")
    eye_key.name = eye_key.name.replace("0006_Face_Eye_morph9", "じと目")
    eye_key.name = eye_key.name.replace("0006_Face_Eye_morph10", "喜び")
    eye_key.name = eye_key.name.replace("0006_Face_Eye_morph11", "怒り目")
    eye_key.name = eye_key.name.replace("0006_Face_Eye_morph12", "ジト目")
    eye_key.name = eye_key.name.replace("0006_Face_Eye_morph13", "眼角上")
    eye_key.name = eye_key.name.replace("0006_Face_Eye_morph14", "眼角下")
    eye_key.name = eye_key.name.replace("0006_Face_Eye_morph15", "下眼上")