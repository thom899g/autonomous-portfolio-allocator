import numpy as np
from portfolio_optimizer import PortfolioOptimizer

class RiskManager:
    def __init__(self):
        self.optimizer = PortfolioOptimizer()
        self.current_portfolio = None

    def start(self):
        self.active = True
        # Initialize with a default portfolio
        self.current_portfolio = self.optimizer.initialize()

    def stop(self):
        self.active = False

    def check_health(self):
        return self.optimizer.health_check()

    def evaluate_risk(self, portfolio_weights):
        if not isinstance(portfolio_weights, dict):
            raise TypeError("Portfolio weights must be a dictionary.")
        
        # Calculate VaR
        var = self.optimizer.calculate_var(portfolio_weights)
        return {'VaR': var, 'Portfolio_Risk_Profile': self.optimizer.get_risk_profile()}

    def apply_constraints(self, portfolio_weights):
        valid = True
        if not self.optimizer.check_constraints(portfolio_weights):
            valid = False
        return valid

    def stress_test(self, scenario='recession'):
        return self.optimizer.run_stress_test(scenario)