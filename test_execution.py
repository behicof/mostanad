def execute_system_tests(test_data: pd.DataFrame) -> Dict[str, Dict]:
    """
    Execute comprehensive system tests
    """
    test_suite = RiskManagementTestSuite(initial_balance=10000.0)
    
    # Test Case 1: Normal Market Conditions
    normal_market_result = test_suite.test_position_sizing(
        entry_price=2000.0,
        sl_price=1990.0
    )
    
    # Test Case 2: High Volatility Conditions
    high_vol_result = test_suite.test_position_sizing(
        entry_price=2000.0,
        sl_price=1990.0,
        atr_value=15.0
    )
    
    # Test Case 3: Daily Risk Management
    sample_trades = [
        {"loss": 100},  # -1%
        {"loss": 200},  # -2%
        {"loss": 150},  # -1.5%
        {"loss": 100}   # -1%
    ]
    risk_management_result = test_suite.test_daily_risk_management(sample_trades)
    
    return {
        "normal_market": normal_market_result,
        "high_volatility": high_vol_result,
        "risk_management": risk_management_result
    }