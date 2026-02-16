from market_analyzer import MarketAnalyzer
from risk_manager import RiskManager
from trade_executor import TradeExecutor
from rl_trader import RLTrader
from data_handler import DataHandler
from safety_guard import SafetyGuard

class MasterAgent:
    def __init__(self):
        self.market_analyzer = MarketAnalyzer()
        self.risk_manager = RiskManager()
        self.trade_executor = TradeExecutor()
        self.rl_trader = RLTrader()
        self.data_handler = DataHandler()
        self.safety_guard = SafetyGuard()

        self.running = False
        self.current_strategy = None

    def start(self):
        if not self.running:
            self.running = True
            # Initialize components
            self.market_analyzer.start()
            self.risk_manager.start()
            self.trade_executor.start()
            self.rl_trader.start()
            self.data_handler.start()
            self.safety_guard.start()

    def stop(self):
        if self.running:
            self.running = False
            # Cleanup components
            self.market_analyzer.stop()
            self.risk_manager.stop()
            self.trade_executor.stop()
            self.rl_trader.stop()
            self.data_handler.stop()
            self.safety_guard.stop()

    def monitor_health(self):
        health_status = {
            'market_data': self.market_analyzer.is_alive(),
            'risk_system': self.risk_manager.check_health(),
            'execution': self.trade_executor.is_connected(),
            'rl_model': self.rl_trader.model_health(),
            'data_available': self.data_handler.has_data()
        }
        return health_status

    def execute_strategy(self, strategy_name):
        if not self.running:
            raise Exception("System is not running.")
        
        # Select appropriate components based on strategy
        if strategy_name == 'trend_following':
            self.current_strategy = self.rl_trader.run_model()
        elif strategy_name == 'mean_reversion':
            self.current_strategy = self.market_analyzer.recommend_mean_reversion Trades()
            
        # Execute and monitor
        self.trade_executor.execute_trades(self.current_strategy)
        return self.risk_manager.evaluate_risk(current_strategy)

    def pause_operation(self):
        if self.running:
            self.running = False
            # Pause but don't stop components
            self.trade_executor.pause()
            self.rl_trader.pause_learning()

    def resume_operation(self):
        if not self.running:
            self.start()  # Ensure all components are restarted