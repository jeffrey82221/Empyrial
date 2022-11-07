from empyrial import empyrial, Engine


def test_engine():
    portfolio = Engine(
        start_date="2018-06-09",
        portfolio=["BABA", "RELIANCE.NS", "KO", "^DJI", "^IXIC"],
        weights=[0.2, 0.2, 0.2, 0.2, 0.2],  # equal weighting by default
        benchmark=["SPY"]  # SPY by default
    )

    # empyrial(portfolio)
