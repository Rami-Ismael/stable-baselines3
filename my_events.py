from stable_baselines3.common.callbacks import BaseCallback
class SaveMyModel(BaseCallback):
    def _on_training_end(self):
        self.model.quantize("my_model_quantized")
        print("Done")
        return True