import tensorflow as tf
from trading_env import TradingEnvironment

class RLTrader:
    def __init__(self):
        self.env = TradingEnvironment()
        self.model = self._build_model()

    def _build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(6