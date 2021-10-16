# SOLTRON

<img src="/screenshots/soltron_logo.png" width="640" />

## What is SOLTRON

**SOLANA ULTRON is an Artificial General Intelligence with an aim to serve humanity to trade better and learn better, build on top of SOLANA and Project Serum**

### Utron Vs SOLTRON

<img src="/screenshots/ultron_vs_soltron.png" width="640" />

<img src="/screenshots/main.png" width="640" />

### It consists of two integrated solutions.
  
1. **The first one is an empathetic conversational AI, to answer any query that a user has, regarding blockchain, trading, or crypto in general, the other one is a Deep Reinforcement learning-based simulation for trading. The trading results are displayed as a dash app for the user, and the URL for the dash app can be fed to the conversational AI to get more insight into users' queries. The conversational AI uses a 400 million parameter language model, based on API, with internet search capability from Facebook AI Research. Unlike time freezed model such as GPT-3 it has dynamic access to the whole world thrugh internet We deployed the language model as, world's first API which has single world, single AI agent, and multiple human agents. We used docker containers, inside the AWS P2.8xlarge instance, which uses 8 Tesla K80 GPU, in parallel processing to power the inference.**

<img src="/screenshots/1.png" width="640" />

<img src="/screenshots/agent2.png" width="640" />

<img src="/screenshots/cse.png" width="640" />

**custom search engine for the blenderbot 2.0 retrievel based model**


2. **The Reinforcement learning uses tensortrade API which is an opensource API for Deep Reinforcement learning simulation of trading environment, it uses Solana API from Serum, to get the real-time bid values of SOL-USDT and other variables, which includes the OHLCV historical data of SOL-USDT trade, portfolio of coins, reward and action schemes to build an environment and simulate the trade so that a trader can understand the risk before the actual trading. Like I said earlier, the Dash app URL then send back to the conversational AI API for better query response.**

<img src="/screenshots/env.png" width="640" />


## Running the RL
**Tested on GTX 1650 Ti Nvidia GPU**

Install Anaconda python : https://www.anaconda.com/products/individual

RUN

```sh
conda create -n soltron pip python=3.7
conda activate soltron
conda install -c anaconda tensorflow-gpu
pip install -r requirements.txt
python rl_simulation.py
```
## Serum API usage
We first convert the the data of SOL-USDT from **Pyserum** which is a client library for interacting with the Project Serum DEX, to **OHLCV** with the help of some additional python API. We made a lambda function to do the job for us. When ever a GET request implemented on the API gateway, the lambda will trigger and upload the csv to AWS S3. Which then used by the above script.

<img src="/screenshots/lambda_function_api.png" width="640" />

The rectangle portion shows the usage of PySerum API from SERUM that uses SOLANA and SERUM DEX. The real time data is send as a data feeder to the environment.

<img src="/screenshots/main_api.png" width="640" />


<img src="/screenshots/main_feed.png" width="640" />

![alt text](https://github.com/kishorkuttan/SOLTRON/blob/master/screenshots/drl.png)

In here we can see the
1. candlestick price plot of the trade with several steps that the agent takes to simulate, we can also see the free, total, locked values of each coin, SOL worth, and net worth. On the bottom side, there is a plot for the volume, performance, and Net Worth during the simulation. 
2. We are using the real-time bid values to adjust the agent's performance using SOLANA API, which is supplied as a data feed into the environment. 
3. After the training or simulation, we can see the overall performance of the trade. 



## Running blenderbot 2.0 API 
**Due to higher charge on the EC2 instance we had stopped the instance, but you can run the Google colab notebook to get the same results**

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1hdKC2mUZN9Ov6fmdoOYbLQH4MhKyKwYr?usp=sharing)

<img src="/screenshots/colab.png" width="640" />

<img src="/screenshots/agent1.png" width="640" />

App link Link : http://ec2-13-234-110-244.ap-south-1.compute.amazonaws.com/

I may stop the AWS EC2 instance due to the instance charge- Mail me if needed to test

### Run app in local system

```sh
python app.py
```

<img src="/screenshots/agent3.png" width="640" />



## GitHub Repo for custom deployment as a docker

Go to this [link](https://github.com/kishorkuttan/parlai) [Nb: The repo is private and access is limited to Hackathon judges.]

<img src="/screenshots/model_diagram.jpeg" width="640" />

1.  The advantage of blender bot 2.0 is that, An own long-term memory and the ability to access the internet. 
2.  It outperforms existing models in terms of, longer conversations over multiple sessions, and is more knowledgeable and has, more factual consistency, according to human evaluators. 
3.  The model stores, pertinent knowledge gleaned during the conversation, to a long-term memory store, and uses this experience to engage, in long-term conversation sessions. During the conversation, the model can search the internet by generating its search queries, reading the results, and taking them into account when formulating a response.
4.   The bot uses a custom search engine for query and response, we can give specific URL to search, which includes, Solana, chainlink, or Raydium documentations, and also our dash app URL for, better insight into the simulated trading.
5.    Users can ask anything that needs answers. The conversational history is saved, to further improve the response from the agent. Even if the user has minimum knowledge in trading, the bot response according to the knowledge of the user itself. 
6.    Trading basic terminologies like ask, bid, spread, MACD, etc. The bot can understand very complex sentences, and the bot has a specific persona to answer them. The conversation can be carried for a long time without, any distraction from the context.

## How it helps the Solana and the crypto community

The integrated AI system, that communicates between the trading simulation, results to a large internet search-based language model, which is very similar to GPT-3, but unlike GPT-3 with time frozen data, this conversational agent learns from the, trading data, and internet data. This will revolutionize the trading and helps new traders as well as, master traders to achieve great heights in their journey. The AI mentor will help you to make better decision for Solana network, since we only focused on the historical data of SOL and its supporting documents as URL.

# Credibility

1. The project started as a 2 year-long deep R&D project on advanced conversational AI and RL agent in collaboration with Government College Of Engineering Kannur. First introduced in Farmer's Assist, an AI recommendation engine from my deep tech agriculture startup **deepflow technologies Pvt. ltd.**(https://www.deepflow.in/). The company was **one among the top 25 teams** in **Cisco Agri challenge**, which is a farmer-centric innovation challenge with 10 Mn lives potential, with a prize pool of 2 Cr and potential investment. **Link** :https://prize.thenudge.org/semi-finalists. Our team is also featured in YourStory. **Link**: https://yourstory.com/2021/09/thenudge-foundation-cisco-entrepreneurs-increase-farmers-innovative-solutions/amp, and also in The New Indian Express. **Link**:https://www.edexlive.com/news/2021/jul/27/this-group-of-four-kannur-youngsters-are-developing-cyber-solutions-for-the-modern-day-22843.html. We are currently working on Deep Reinforcement Learning integration to Language model for better recommneddation engine

<img src="/screenshots/featured.jpeg" width="480" />


<img src="/screenshots/indian_express.png" width="480" />

2. Our team also won 3rd prize in the OpenCV AI competition 2021 at the regional level, which is an international AI competition celebrating OpenCV's 20th anniversary. Which is the World's biggest spatial AI competition with Prizes worth $400K and Worldwide competition with global and regional winners. We had the latest implementation of our AI agent on the AI quadruped agriculture Robot API. Winner announcement Link: https://opencv.org/opencv-ai-competition-2021/. The AI robot also won in the Agri India Hackathon organized by the Government of India and Pusa Krishi and we were one among the 11 startups form all across India, in their 2021 cohort. **Link**:https://blog.mygov.in/winner-announcement-of-agri-india-hackathon/
Github Link to Agri robot: click [here](https://github.com/kishorkuttan/AI-Quadruped-Robot-For-Agriculture).

<img src="/screenshots/hackathon.png" width="480" />

3. Our second deep tech startup is called **Convai Innovations Pvt. Ltd.** extensively focuses on **conversational AI and blockchain** in general. The startup has released its blind navigation app called depthnavai, available on the play store. https://play.google.com/store/apps/details?id=com.convaiinnovations.ml.DepthNavAI.
Which is an AI app for the visually impaired or blind, for navigation, light detection, face attribute recognition, and text recognition. We are working on implementing our integrated AI agent, which we had developed for this hackathon into the app, which means that the solana network or blockchain technology will benefit a wonderful community. The app already has 100+ downloads within a week. Both of theses startups are recognized by startup India with DPIIT certificate. Along with Dr. Anjali MBBS, who is my partner of this hackathon, and board member of both of these startups, we are trying to revolutionize the industry with blockchain and AI.

Website: https://convaiinnovations.com/


## What is  ParlAI

ParlAI is a python-based platform for enabling dialog AI research.

Its goal is to provide researchers:

1. A unified framework for sharing, training and testing dialog models

2. Many popular datasets available all in one place, with the ability to multi-task over them

3. Seamless integration of Amazon Mechanical Turk for data collection and human evaluation

4. Integration with chat services like Facebook Messenger to connect agents with humans in a chat interface link: https://github.com/facebookresearch/ParlAI

# Reference
1. https://github.com/tensortrade-org/tensortrade
2. https://parl.ai/docs/zoo.html
3. https://github.com/facebookresearch/ParlAI
4. https://parl.ai/projects/blenderbot2/


