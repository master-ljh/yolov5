import torch

# 加载.pt文件

model = torch.load("/home/ljh/v5/yolov5/runs/train-seg/exp/weights/best.pt")

# 打印模型信息
print(model)
