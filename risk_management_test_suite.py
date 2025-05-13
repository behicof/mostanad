import numpy as np
import pandas as pd
from typing import Dict, List, Tuple

class RiskManagementTestSuite:
    def __init__(self, initial_balance: float = 10000.0):
        self.initial_balance = initial_balance
        self.current_balance = initial_balance
        self.daily_risk_limit = 0.05  # 5%
        self.trade_risk = 0.01        # 1%
        
    def test_position_sizing(self, 
                           entry_price: float,
                           sl_price: float,
                           atr_value: float = None) -> Dict[str, float]:
        """
        Test dynamic position sizing with volatility consideration
        """
        risk_amount = self.current_balance * self.trade_risk
        pip_risk = abs(entry_price - sl_price)
        pip_value = 10.0  # USD per pip for 1 lot XAUUSD
        
        # Base position size calculation
        position_size = risk_amount / (pip_risk * pip_value)
        
        # Volatility adjustment if ATR is provided
        if atr_value and atr_value > (pip_risk * 2):
            position_size *= 0.5  # Reduce position size in high volatility
            
        return {
            "position_size": round(position_size, 2),
            "risk_amount": risk_amount,
            "pip_risk": pip_risk
        }

    def test_daily_risk_management(self, 
                                 trades: List[Dict[str, float]]) -> Dict[str, bool]:
        """
        Test daily risk limit enforcement
        """
        daily_losses = 0.0
        max_daily_loss = self.initial_balance * self.daily_risk_limit
        trading_allowed = True
        
        for trade in trades:
            if daily_losses >= max_daily_loss:
                trading_allowed = False
                break
            daily_losses += abs(trade.get("loss", 0))
            
        return {
            "trading_allowed": trading_allowed,
            "current_risk_used": daily_losses / self.initial_balance,
            "risk_limit_reached": daily_losses >= max_daily_loss
        }

    def test_volatility_handling(self, 
                               price_data: pd.DataFrame,
                               atr_period: int = 14) -> Dict[str, bool]:
        """
        Test volatility-based risk adjustments
        """
        def calculate_atr(high: pd.Series, 
                         low: pd.Series, 
                         close: pd.Series, 
                         period: int) -> pd.Series:
            tr = pd.DataFrame()
            tr['h-l'] = high - low
            tr['h-pc'] = abs(high - close.shift(1))
            tr['l-pc'] = abs(low - close.shift(1))
            tr['tr'] = tr[['h-l', 'h-pc', 'l-pc']].max(axis=1)
            return tr['tr'].rolling(period).mean()

        # Calculate ATR
        atr = calculate_atr(price_data['high'], 
                          price_data['low'], 
                          price_data['close'], 
                          atr_period)
        
        # Test conditions
        volatility_high = atr > atr.mean() * 2
        rsi_extreme = (price_data['rsi'] > 70) | (price_data['rsi'] < 30)
        
        return {
            "reduce_position": volatility_high | rsi_extreme,
            "high_volatility_periods": volatility_high.sum(),
            "rsi_extreme_periods": rsi_extreme.sum()
        }