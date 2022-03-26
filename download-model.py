from mlflow.store.artifact.models_artifact_repo import ModelsArtifactRepository
from mlflow.tracking import MlflowClient

client = MlflowClient()
my_model = client.download_artifacts("30a359ffc3644402aec9959c5d316bec", path="model")
print(f"Placed model in: {my_model}")



