# CSE_597_FA24

## SmallCap

This code demonstrates how I replicated [SmallCap](https://openaccess.thecvf.com/content/CVPR2023/papers/Ramos_SmallCap_Lightweight_Image_Captioning_Prompted_With_Retrieval_Augmentation_CVPR_2023_paper.pdf), the lightweight image captioning model from CVPR 2023.

## Requirements
### Download evaluation package
Download evaluation package from this [repository](https://github.com/daqingliu/coco-caption.git) to compute BLEU-4, METEOR, CIDEr, and SPICE. 
For example, the directory of annotation folder should be places as follows: `./coco-caption/annotation/`

### Download the COCO index and captions
Download the [COCO index](https://drive.google.com/file/d/1ZP5I-xbjaNU7cU48C_ctHd95SaA0jBHe/view?usp=sharing) and [related captions](https://drive.google.com/file/d/1BT0Qc6g40fvtnJ_yY0aipfCuCMgu5qaR/view?usp=sharing). 
Make a new directory: `./datastore`
Place these files in datastore folder: `./datastore/coco_index.file` and `./datastore/coco_index_captions.json`

### Download COCO Karpathy splits file
Dowload the COCO Karpathy splits file (dataset_coco.json) from this [repository](https://www.kaggle.com/datasets/shtvkumar/karpathy-splits).
Place dataset_coco.json under the data folder: `./data/dataset_coco.json`

## Training
The model is trained in Google Colab environment. The entire training process is conducted through `./prepare.ipynb` jupyter notebook file. Below summarizes this process.

- Install requirements
- Download COCO 2017 dataset (train/test/val)
- Put all COCO 2017 dataset into ./data/images/
- Install the full CLIP model
- Extract features
- Retrieve captions
- Train model
- Infer on COCO test set
- Evaluate using metrics






