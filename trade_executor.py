import logging
from trading_broker import TradingBroker

class TradeExecutor:
    def __init__(self):
        self.broker = TradingBroker()
        self.current_orders = []

    def start(self):
        self.active = True
        # Connect to broker
        if not self.broker.connect():
            raise ConnectionError("Failed to connect to trading broker.")

    def stop(self):
        self.active = False
        # Disconnect from broker
        self.broker.disconnect()

    def execute_trades(self, orders):
        if not isinstance(orders, list):
            raise TypeError("Orders must be a list of dictionaries.")
        
        executed_orders = []
        for order in orders:
            try:
                trade_id = self.broker.place_order(order)
                executed_orders.append(trade_id)
                logging.info(f"Executed order {trade_id}")
            except Exception as e:
                logging.error(f"Failed to execute order: {str(e)}")
        
        return executed_orders

    def get_positions(self):
        positions = self.broker.get_positions()
        if not positions:
            raise ValueError("No positions found.")
        return positions