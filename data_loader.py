"""
分段执行
"""

# 配置环境
# import torch
# import utils



# # 在yolov5路径下 cd ../yolov5
# display = utils.notebook_init()

# dataloader
# from roboflow import Roboflow

# # 直接从网页导入数据，也可以自己下载下来，放在该路径下

# rf = Roboflow(api_key = "2Z4xx14CjNYGh4ZCzrf4")
# project = rf.workspace("monash-h8dbx").project("tumor-egzxx")
# dataset = project.version(2).download("yolov5")

# 加载预训练权重
# from utils.downloads import attempt_download

# p5 = ['n','s','m','l','x'] # p5 models
# cls = [f'{x}-seg' for x in p5]

# for x in cls:
#     attempt_download(f'weights/yolov5{x}.pt')

# """
# python segment/train.py --img 320 --batch 16 --epochs 100 //
# --data {dataset.location}/data.yaml --weights yolov5s-seg.pt 
# display.Image(filename=f'runs/train-seg/exp/results.png', width=1200) 

# """    