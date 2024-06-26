# Import the required modules
from anomalib.data import MVTec
from anomalib.models import EfficientAd
from anomalib.engine import Engine

# Initialize the datamodule, model and engine
datamodule = MVTec(
  category='pills',
  train_batch_size=1,
  eval_batch_size=1,
  num_workers=4,
  )
model = EfficientAd()
engine = Engine(max_epochs=20)

# Train the model
engine.fit(datamodule=datamodule, model=model)