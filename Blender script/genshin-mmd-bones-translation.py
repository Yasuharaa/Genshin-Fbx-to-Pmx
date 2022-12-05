import bpy
context = bpy.context
obj = context.object

#Made with love by Berita Teyvat
#If u have any trouble pls dm me on Twitter @BeritaTeyvat

namelist = [
#("BoneNameYouWantRenamed", "BoneNameToRenameBoneTo")
#Example:
#("chest_a", "Spine1"),
# Templete
("Bip001", "センター"),
("+PelvisTwist CF A01", "下半身"),
("Bip001 Pelvis", "腰"),
("Bip001 Spine", "上半身"),
("Bip001 Spine1", "上半身3"),
("Bip001 Spine2", "上半身2"),
("Bip001 Neck", "首"),
("Bip001 Head", "頭"),
("Bip001 L Clavicle", "左肩"),
("Bip001 L UpperArm", "左腕"),
("Bip001 L Forearm", "左ひじ"),
("Bip001 L Hand", "左手首"),
("Bip001 R Clavicle", "右肩"),
("Bip001 R UpperArm", "右腕"),
("Bip001 R Forearm", "右ひじ"),
("Bip001 R Hand", "右手首"),
("Bip001 L Finger0", "左親指０"),
("Bip001 L Finger01", "左親指１"),
("Bip001 L Finger02", "左親指２"),
("Bip001 L Finger1", "左人指１"),
("Bip001 L Finger11", "左人指２"),
("Bip001 L Finger12", "左人指３"),
("Bip001 L Finger2", "左中指１"),
("Bip001 L Finger21", "左中指２"),
("Bip001 L Finger22", "左中指３"),
("Bip001 L Finger3", "左薬指１"),
("Bip001 L Finger31", "左薬指２"),
("Bip001 L Finger32", "左薬指３"),
("Bip001 L Finger4", "左小指１"),
("Bip001 L Finger41", "左小指２"),
("Bip001 L Finger42", "左小指３"),
("Bip001 R Finger0", "右親指０"),
("Bip001 R Finger01", "右親指１"),
("Bip001 R Finger02", "右親指２"),
("Bip001 R Finger1", "右人指１"),
("Bip001 R Finger11", "右人指２"),
("Bip001 R Finger12", "右人指３"),
("Bip001 R Finger2", "右中指１"),
("Bip001 R Finger21", "右中指２"),
("Bip001 R Finger22", "右中指３"),
("Bip001 R Finger3", "右薬指１"),
("Bip001 R Finger31", "右薬指２"),
("Bip001 R Finger32", "右薬指３"),
("Bip001 R Finger4", "右小指１"),
("Bip001 R Finger41", "右小指２"),
("Bip001 R Finger42", "右小指３"),
("Bip001 L Thigh", "左足"),
("Bip001 L Calf","左ひざ"),
("Bip001 L Foot", "左足首"),
("Bip001 L Toe0", "左つま先"),
("Bip001 R Thigh", "右足"),
("Bip001 R Calf","右ひざ"),
("Bip001 R Foot", "右足首"),
("Bip001 R Toe0", "右つま先"),
("+EyeBone L A01", "左目"),
("+EyeBone L A02", "左目戻"),
("+EyeBone R A01", "右目"),
("+EyeBone R A02", "右目戻"),
("+ToothBone D A01", "下歯"),
("+ToothBone U A01", "上歯"),
("DMZ L 01", "左親指０"),
("DMZ L 02", "左親指１"),
("DMZ L 03", "左親指２"),
("DMZ R 01", "左親指０"),
("DMZ R 02", "左親指１"),
("DMZ R 03", "左親指２"),

]

for name, newname in namelist:
	# get the pose bone with name
	pb = obj.pose.bones.get(name)
	# continue if no bone of that name
	if pb is None:
		continue
	# rename
	pb.name = newname