from typing import Any
from tensortrade.oms.instruments.quantity import Quantity
from tensortrade.oms.instruments.trading_pair import TradingPair
import tensortrade.env.default as default
from tensortrade.data.cdd import CryptoDataDownload
from tensortrade.feed.core import Stream, DataFeed
from tensortrade.oms.exchanges import Exchange
from tensortrade.oms.services.execution.simulated import execute_order
from tensortrade.oms.instruments import USD, BTC, ETH
from tensortrade.oms.wallets import Wallet, Portfolio
from tensortrade.agents import DQNAgent
import tensortrade.env.default.actions as actions
import tensortrade.env.default.rewards as rewards
import tensortrade.env.default.stoppers as stoppers
import dashboard
import threading
import requests
import json
import wget
import pandas as pd
from datetime import datetime,timedelta
ds = dashboard.DashboardServer()
t = threading.Thread(target=ds.run)
t.start()
now = datetime.now()
registry = {}
## Pyserum using Solana API. Raydium DEX uses PySerum.
from pyserum.connection import conn
from pyserum.market import Market
import pandas as pd 
import statistics
cc = conn("https://api.mainnet-beta.solana.com/")
market_address = "HWHvQhFmJB3NUcu1aihKmrKegfVxBEHzwVX6yZCKEsi1" # Address for SOL/USDT

def extract_bid():
    today = datetime.today()
    datem = datetime(today.year, today.month, 1)
    print(datem)
    # Load the given market
    market = Market.load(cc, market_address)
    asks = market.load_asks()
    # Show all current ask order



    # Show all current bid order

    raw_bids = market.load_bids()

    tmp = pd.DataFrame()
    bids = []
    for bid in raw_bids:
        bids.append(bid.info.price)
    bids_avg = statistics.mean(bids)
    data = [[datem,bids_avg]]
    
    # Create the pandas DataFrame
    df1 = pd.DataFrame(data, columns = ['date', 'bid'])

    df1.to_csv("bids_daily.csv")
    return df1

# To Custom select SOL and USDT
class Instrument:
    """A financial instrument for use in trading.

    Parameters
    ----------
    symbol : str
        The symbol used on an exchange for a particular instrument.
        (e.g. SOL, BTC, TSLA)
    precision : int
        The precision the amount of the instrument is denoted with.
        (e.g. SOL=8,  BTC=8, AAPL=1)
    name : str, optional
        The name of the instrument being created.
    """

    def __init__(self, symbol: str, precision: int, name: str = None) -> None:
        self.symbol = symbol
        self.precision = precision
        self.name = name

        registry[symbol] = self

    def __eq__(self, other: "Any") -> bool:
        """Checks if two instruments are equal.

        Parameters
        ----------
        other : `Any`
            The instrument being compared.

        Returns
        -------
        bool
            Whether the instruments are equal.
        """
        if not isinstance(other, Instrument):
            return False
        c1 = self.symbol == other.symbol
        c2 = self.precision == other.precision
        c3 = self.name == other.name
        return c1 and c2 and c3

    def __ne__(self, other: "Any") -> bool:
        """Checks if two instruments are not equal.

        Parameters
        ----------
        other : `Any`
            The instrument being compared.

        Returns
        -------
        bool
            Whether the instruments are not equal.
        """
        return not self.__eq__(other)

    def __rmul__(self, other: float) -> "Quantity":
        """Enables reverse multiplication.

        Parameters
        ----------
        other : float
            The number used to create a quantity.

        Returns
        -------
        `Quantity`
            The quantity created by the number and the instrument involved with
            this operation.
        """
        return Quantity(instrument=self, size=other)

    def __truediv__(self, other: "Instrument") -> "TradingPair":
        """Creates a trading pair through division.

        Parameters
        ----------
        other : `Instrument`
            The instrument that will be the quote of the pair.

        Returns
        -------
        `TradingPair`
            The trading pair created from the two instruments.

        Raises
        ------
        InvalidTradingPair
            Raised if `other` is the same instrument as `self`.
        Exception
            Raised if `other` is not an instrument.
        """
        if isinstance(other, Instrument):
            return TradingPair(self, other)
        raise Exception(f"Invalid trading pair: {other} is not a valid instrument.")

    def __hash__(self):
        return hash(self.symbol)

    def __str__(self):
        return str(self.symbol)

    def __repr__(self):
        return str(self)


# Crypto
SOL = Instrument('SOL', 8, 'Solana')
BTC = Instrument('BTC', 8, 'Bitcoin')
ETH = Instrument('ETH', 8, 'Ethereum')
XRP = Instrument('XRP', 8, 'XRP')
NEO = Instrument('NEO', 8, 'NEO')
BCH = Instrument('BCH', 8, 'Bitcoin Cash')
LTC = Instrument('LTC', 8, 'Litecoin')
ETC = Instrument('ETC', 8, 'Ethereum Classic')
XLM = Instrument('XLM', 8, 'Stellar Lumens')
LINK = Instrument('LINK', 8, 'Chainlink')
ATOM = Instrument('ATOM', 8, 'Cosmos')
DAI = Instrument('DAI', 8, 'Dai')
USDT = Instrument('USDT', 8, 'Tether')

# FX
USD = Instrument('USD', 2, 'U.S. Dollar')
EUR = Instrument('EUR', 2, 'Euro')
JPY = Instrument('JPY', 2, 'Japanese Yen')
KWN = Instrument('KWN', 2, 'Korean Won')
AUD = Instrument('AUD', 2, 'Australian Dollar')

# Commodities
XAU = Instrument('XAU', 2, 'Gold futures')
XAG = Instrument('XAG', 2, 'Silver futures')

# Stocks

AAPL = Instrument('AAPL', 2, 'Apple stock')
MSFT = Instrument('MSFT', 2, 'Microsoft stock')
TSLA = Instrument('TSLA', 2, 'Tesla stock')
AMZN = Instrument('AMZN', 2, 'Amazon stock')

def build_env():
    df1 = extract_bid()
    ## Using AWS lambda function to upload the csv to AWS S3 and downlod it 
    response = requests.get("https://trudmbc2w0.execute-api.ap-south-1.amazonaws.com/default/solanaohlcv")
    # download the csv file from AWS S3
    wget.download("https://solanaai.s3.ap-south-1.amazonaws.com/Solana.csv")
    


    def rsi(price: Stream[float], period: float) -> Stream[float]:
        r = price.diff()
        upside = r.clamp_min(0).abs()
        downside = r.clamp_max(0).abs()
        rs = upside.ewm(alpha=1 / period).mean() / downside.ewm(alpha=1 / period).mean()
        return 100*(1 - (1 + rs) ** -1)


    def macd(price: Stream[float], fast: float, slow: float, signal: float) -> Stream[float]:
        fm = price.ewm(span=fast, adjust=False).mean()
        sm = price.ewm(span=slow, adjust=False).mean()
        md = fm - sm
        signal = md - md.ewm(span=signal, adjust=False).mean()
        return signal


    features = []
    for c in data.columns[1:]:
        s = Stream.source(list(data[c]), dtype="float").rename(data[c].name)
        features += [s]

    cp = Stream.select(features, lambda s: s.name == "close")

    features = [
        cp.log().diff().rename("lr"),
        rsi(cp, period=20).rename("rsi"),
        macd(cp, fast=10, slow=50, signal=5).rename("macd")
    ]

    feed = DataFeed(features)
    feed.compile()

    Raydium = Exchange("Raydium", service=execute_order)(
        Stream.source(list(data["close"]), dtype="float").rename("USDT-SOL")
    )

    cash = Wallet(Raydium, 10000 * USDT)
    asset = Wallet(Raydium, 0 * SOL)

    portfolio = Portfolio(USDT, [
        cash,
        asset
    ])

    renderer_feed = DataFeed([
        Stream.source(list(data["date"])).rename("date"),
        Stream.source(list(data["open"]), dtype="float").rename("open"),
        Stream.source(list(data["high"]), dtype="float").rename("high"),
        Stream.source(list(data["low"]), dtype="float").rename("low"),
        Stream.source(list(data["close"]), dtype="float").rename("close"),
        Stream.source(list(data["volume"]), dtype="float").rename("volume"),
         Stream.source(list(df1["bid"]), dtype="float").rename("bid")
    ])

    reward_scheme = rewards.SimpleProfit()
    action_scheme = actions.BSH(cash, asset)


    env = default.create(
        portfolio=portfolio,
        action_scheme=action_scheme,
        reward_scheme=reward_scheme,
        stopper=stoppers.MaxLossStopper(1000.0),
        feed=feed,
        renderer_feed=renderer_feed,
        renderer=default.renderers.PlotlyTradingChart(display=False, height=700, save_format="html"),
        window_size=20
    )
    return env


env = build_env()

def simple_trader(num_runs=10, n_steps=200):
    for i in range(num_runs):
        env.reset()
        action = 1
        for i in range(n_steps):
            env.render()
            dashboard.dashboard.update_figure(env.renderer.fig)
            action = action ^ 1
            ob, rew, done, info = env.step(action)

if __name__ == '__main__':
    simple_trader()
