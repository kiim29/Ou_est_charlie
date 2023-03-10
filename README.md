# Où est Charlie
Projet de Deep Learning qui résout les jeux Où est Charlie en trouvant la position exacte de Charlie dans une image

![alt text](https://raw.githubusercontent.com/kiim29/Ou_est_charlie/main/Charlie.jpg)

Ce projet utilise un modèle Detectron2 entrainé avec torch pour retrouver Charlie.
Retrouvez notre [notebook](https://colab.research.google.com/drive/1DR7ych_KQZmBN8uMdPDZxCob_TRR85JF?usp=sharing) ici !

## Dépendances
Python: 3.9  
torch:  1.13  
cuda:  cu116 (V 11.8)  
detectron2: 0.6  

## Utilisation du modèle  
Charger le modèle :
```
cfg = get_cfg()
cfg.MODEL.WEIGHTS = os.path.join("model_final.pth")  # path to the model
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.7
predictor = DefaultPredictor(cfg)
```

Détecter Charlie dans une image :
```
im = cv2.imread('PATH_TO_THE_IMAGE')
outputs = predictor(im) 
v = Visualizer(im[:, :, ::-1],
                metadata=waldo_metadata, 
                scale=0.5
)
out = v.draw_instance_predictions(outputs["instances"].to("cpu"))
cv2_imshow(out.get_image()[:, :, ::-1])
```

![alt text](https://raw.githubusercontent.com/kiim29/Ou_est_charlie/main/DetectedCharlie.png)

## Entrainement du modèle  
Se référer au [notebook](https://colab.research.google.com/drive/1DR7ych_KQZmBN8uMdPDZxCob_TRR85JF?usp=sharing)  

## Imports dans le projet
```
import sys, os, distutils.core
import torch, detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

# import some common libraries
import numpy as np
import os, json, cv2, random
from google.colab.patches import cv2_imshow

# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog

from ListeNoms import *
import pandas as pd
from detectron2.structures import BoxMode

from detectron2.utils.visualizer import ColorMode
```
