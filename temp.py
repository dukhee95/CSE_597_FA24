# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("image-to-text", model="Yova/SmallCap7M")