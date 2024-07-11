# Assuming the datamodule, model and engine is initialized from the previous step,
# Initialize the datamodule, model and engine
# Import the required modules
from anomalib.data import MVTec
from anomalib.models import EfficientAd
from anomalib.engine import Engine

model = EfficientAd()

engine = Engine()
# a prediction via a checkpoint file can be performed as follows:
predictions = engine.predict(
    model=model,
    ckpt_path="./results/EfficientAd/MVTec/tags_seg/latest/weights/lightning/model.ckpt",
    data_path='./inf_data',
)