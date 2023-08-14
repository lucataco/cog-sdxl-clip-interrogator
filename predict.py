import sys
from PIL import Image
from cog import BasePredictor, Input, Path
from clip_interrogator import Interrogator, Config

sys.path.append('/root/blip')

class Predictor(BasePredictor):
    def setup(self):
        self.ci = Interrogator(Config(
            blip_model_url='cache/model_large_caption.pth',
            clip_model_name="ViT-g-14/laion2B-s34B-b88K",
            clip_model_path='cache',
            device='cuda:0',
        ))

    def predict(
        self,
        image: Path = Input(description="Input image"),
        mode: str = Input(
            default="best",
            choices=["best", "fast"],
            description="Prompt Mode: fast takes 1-2 seconds, best takes 15-25 seconds.",
        ),
    ) -> str:
        """Run a single prediction on the model"""
        clip_model_name = "ViT-g-14/laion2B-s34B-b88K"
        image = Image.open(str(image)).convert("RGB")
        self.switch_model(clip_model_name)
        if mode == "best":
            return self.ci.interrogate(image)
        else:
            return self.ci.interrogate_fast(image)

    def switch_model(self, clip_model_name: str):
        if clip_model_name != self.ci.config.clip_model_name:
            self.ci.config.clip_model_name = clip_model_name
            self.ci.load_clip_model()