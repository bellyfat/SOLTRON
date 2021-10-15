# SOLTRON
## What is SOLTRON
**SOLTRON is an Artificial General Intelligence, build on top of SOLANA and project serum**
<img src="/screenshots/main.png" width="640" />
It consists of two integrated solutions.
  
1. **The first one is an empathetic conversational AI, to answer any query that a user has, regarding blockchain, trading, or crypto in general, the other one is a Deep Reinforcement learning-based simulation for trading. The trading results are displayed as a dash app for the user, and the URL for the dash app can be fed to the conversational AI to get more insight into users' queries. The conversational AI uses a 400 million parameter language model, based on API, with internet search capability from Facebook AI Research. We deployed the language model as, world's first API which has single world, single AI agent, and multiple human agents. We used docker containers, inside the AWS P2.8xlarge instance, which uses 8 Tesla K80 GPU, in parallel processing to power the inference.**
<img src="/screenshots/1.png" width="640" />

2. **The Reinforcement learning uses tensortrade API which is an opensource API for Deep Reinforcement learning simulation of trading environment, it uses Solana API from Serum, to get the real-time bid values of SOL-USDT and other variables, which includes the OHLCV historical data of SOL-USDT trade, portfolio of coins, reward and action schemes to build an environment and simulate the trade so that a trader can understand the risk before the actual trading. Like I said earlier, the Dash app URL then send back to the conversational AI API for better query response.**

<img src="/screenshots/trade_env.png" width="640" />


## Running the RL
```sh
pip install -r requirements.txt
!python rl_simulation.py
```
![alt text](https://github.com/kishorkuttan/SOLTRON/blob/master/screenshots/drl.png)

In here we can see the
1. candlestick price plot of the trade with several steps that the agent takes to simulate, we can also see the free, total, locked values of each coin, SOL worth, and net worth. On the bottom side, there is a plot for the volume, performance, and Net Worth during the simulation. 
2. We are using the real-time bid values to adjust the agent's performance using SOLANA API, which is supplied as a data feed into the environment. 
3. After the training or simulation, we can see the overall performance of the trade. 





1.  The advantage of blender bot 2.0 is that, An own long-term memory and the ability to access the internet. 
2.  It outperforms existing models in terms of, longer conversations over multiple sessions, and is more knowledgeable and has, more factual consistency, according to human evaluators. 
3.  The model stores, pertinent knowledge gleaned during the conversation, to a long-term memory store, and uses this experience to engage, in long-term conversation sessions. During the conversation, the model can search the internet by generating its search queries, reading the results, and taking them into account when formulating a response.
4.   The bot uses a custom search engine for query and response, we can give specific URL to search, which includes, Solana, chainlink, or Raydium documentations, and also our dash app URL for, better insight into the simulated trading.
5.    Users can ask anything that needs answers. The conversational history is saved, to further improve the response from the agent. Even if the user has minimum knowledge in trading, the bot response according to the knowledge of the user itself. 
6.    Trading basic terminologies like ask, bid, spread, MACD, etc. The bot can understand very complex sentences, and the bot has a specific persona to answer them. The conversation can be carried for a long time without, any distraction from the context.

The integrated AI system, that communicates between the trading simulation, results to a large internet search-based language model, which is very similar to GPT-3, but unlike GPT-3 with time frozen data, this conversational agent learns from the, trading data, and internet data. This will revolutionize the trading and helps new traders as well as, master traders to achieve great heights in their journey. 
