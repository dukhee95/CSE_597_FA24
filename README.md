# CSE_597_FA24
Name: DukHee Ka

## SMALLCAP

This code demonstrates how I replicated [SmallCap](https://openaccess.thecvf.com/content/CVPR2023/papers/Ramos_SmallCap_Lightweight_Image_Captioning_Prompted_With_Retrieval_Augmentation_CVPR_2023_paper.pdf), the lightweight image captioning model from CVPR 2023.

## REQUIREMENTS
### Download Evaluation Package
Download the evaluation package from this [repository](https://github.com/daqingliu/coco-caption.git) to compute BLEU-4, METEOR, CIDEr, and SPICE. 

For example, the directory of the annotation folder should be structured as follows: `./coco-caption/annotation/`


### Download the COCO Index and Captions
Download the [COCO index](https://drive.google.com/file/d/1ZP5I-xbjaNU7cU48C_ctHd95SaA0jBHe/view?usp=sharing) and [related captions](https://drive.google.com/file/d/1BT0Qc6g40fvtnJ_yY0aipfCuCMgu5qaR/view?usp=sharing). 

Make a new directory: `./datastore`

Place these files in the datastore folder: `./datastore/coco_index.file` and `./datastore/coco_index_captions.json`


### Download COCO Karpathy Splits File
Dowload the COCO Karpathy splits file (dataset_coco.json) from this [repository](https://www.kaggle.com/datasets/shtvkumar/karpathy-splits).

Place `dataset_coco.json` under the data folder: `./data/dataset_coco.json`


## TRAINING
The model is trained in a Google Colab environment. The entire training process is conducted via `./prepare.ipynb` Jupyter notebook file. If you are unable to open prepare.ipynb in GitHub, please download it in this [repository](https://drive.google.com/file/d/1lshRN3rR9z7t8YuVeyQbZyuAcIRjGm1S/view?usp=drive_link) instead. Below is a summary of the process:
- Install requirements
- Download COCO 2017 dataset (train/test/val)
- Put all COCO 2017 dataset into ./data/images/
- Install the full CLIP model
- Extract features
- Retrieve captions
- Train model
- Infer on COCO test set
- Evaluate using metrics






