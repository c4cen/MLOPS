# main.py
import hydra # type: ignore
from omegaconf import DictConfig, OmegaConf # type: ignore

@hydra.main(version_base=None, config_path="config", config_name="config")
def my_app(cfg: DictConfig):
    print(OmegaConf.to_yaml(cfg))

    # Accessing model configuration
    print(f"Model: {cfg.model.name}, Pretrained: {cfg.model.pretrained}")

    # Accessing dataset configuration
    print(f"Dataset: {cfg.dataset.name}, Path: {cfg.dataset.path}")

    # Accessing training configuration
    print(f"Training: Batch Size: {cfg.training.batch_size}, Learning Rate: {cfg.training.learning_rate}")

    # Example: Running training process (Placeholder)
    # train_model(cfg.model, cfg.dataset, cfg.training)

if __name__ == "__main__":
    my_app()
