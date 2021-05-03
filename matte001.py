import os
import sys
print(os.getcwd())
print(sys.prefix)
print(os.path.join(sys.prefix, 'BackgroundMattingV2-master'))
sys.path.append(os.path.join(sys.prefix, 'BackgroundMattingV2-master'))
import torch
from model import MattingRefine
from torchvision.transforms.functional import to_tensor, to_pil_image
from PIL import Image
#device = torch.device('cuda')
device = torch.device('cpu')
precision = torch.float32

model = MattingRefine(backbone='resnet101', #Or other model
                      backbone_scale=0.25,
                      refine_mode='sampling',
                      refine_sample_pixels=80_000)

model.load_state_dict(torch.load(os.path.join(sys.prefix, 'BackgroundMattingV2-master','pytorch_resnet101.pth'), map_location = device)) #Or other model
model = model.eval().to(precision).to(device)

sourceFolder = os.path.join(sys.prefix,'BackgroundMattingV2-master','in')
outputFolder = os.path.join(sys.prefix,'BackgroundMattingV2-master','out')

bgr = Image.open(os.path.join(sys.prefix,'BackgroundMattingV2-master','cleanPlate.png'))
bgr = to_tensor(bgr).unsqueeze(0)#.cuda().unsqueeze(0)

file_names = next(os.walk(sourceFolder))[2]
with torch.no_grad():
    for fileSrc in file_names:
        src = Image.open(sourceFolder+'/'+fileSrc)
        src = to_tensor(src).unsqueeze(0)#.cuda().unsqueeze(0)
        pha, fgr = model(src, bgr)[:2]
#        com = pha * fgr + (1 - pha) * torch.tensor([120/255, 255/255, 155/255], device='cpu').view(1, 3, 1, 1)
        to_pil_image(pha[0].cpu()).save(outputFolder+'/pha002'+fileSrc)
#        to_pil_image(fgr[0].cpu()).save(outputFolder+'fgr002'+fileSrc)
#        to_pil_image(com[0].cpu()).save(outputFolder+'com002'+fileSrc)
