<h1>Crypto Currency as an Effective Hedge Agasint Currency Risk</h1>

**NOTE** This is still a working copy and should not be used to extract any reliable information from the content within

<h2>Project Goals</h2>


Make a unique observation about cryptocurrencies with statistical significance or statistical **in**significance.

<h2>Current Progress</h2>
Currently I have a working Monte Carlo simulator working in the repo under the name "Monte_Carlo.py". It is currently set to give an output of 4 years of simulated Bitcoin prices as seen in this graph below.

![Monte Carlo Simulation BTC-USD](https://github.com/beachc15/Evaluation-of-Crypto-as-a-currency-hedge/blob/master/assets/BTC-USD%20Monte%20Carlo%20Simulation.png?raw=true)


I have also simulated my S&P 100 portfolio as seen by this scaled graph included below.

![Constructed S&P 100 returns](https://github.com/beachc15/Evaluation-of-Crypto-as-a-currency-hedge/blob/master/assets/S&P%20100%20returns%20as%20percent.png?raw=true)


This portfolio will be used to calculate the value at risk in both distressed periods as well as standard periods with and without both gold and bitcoin included at different percentages in the portfolio.



<h2>Possible Methods</h2>

* If we can correlate Crypto to Gold's performance historically, then we just need to prove gold's value
* Differentiate the different numerical metrics which identify a store of value or a currency hedge and evaluate crypto against these ideas


<h2>Steps</h2>

1. Define what we need to find in order to prove certain crypto as an effective store of value/currency hedge



<h2>To Prove</h2>

* What Proves a Store of Value?
        * A store of value is an asset that **maintains its value without depreciating**. **Gold** and other metals are good stores of value as their *shelf lives are essentially perpetual*, whereas a perishable item (milk, for example[or even currency]) is a poor store of value because of its propensity to decay. Interest-bearing assets, such as **U.S. Treasury bonds (T-bonds)**, are very good stores of value because they generate interest income and their **principal balances are backed by legal contracts.** ([Investopedia](https://www.investopedia.com/terms/s/storeofvalue.asp))
    * Gold?
        * cons
            * constant supply growth
        * pros
    * U.S. Treasury Bills
        * Generate Passive Income
        * Backed by legal contracts and the faith of the US Government (trustworthy)
    
* What proves a Currency Hedge?
    * A forex hedge is a transaction implemented to **protect an existing or anticipated position from an unwanted move in exchange rates**. Forex hedges are used by a broad range of market participants, including investors, traders and businesses. By using a forex hedge properly, an individual who is long a foreign currency pair or expecting to be in the future via a transaction can be protected from downside risk. Alternatively, a trader or investor who is short a foreign currency pair can protect against upside risk using a forex hedge. ([Investopedia](https://www.investopedia.com/terms/forex/f/forex-hedge-and-currency-hedging-strategy.asp))
    * Protecting against an existing or anticipated position from an unwanted more in exchange rates
<h2>Current Ideas</h2>

* we should build some robust returns analysis tools and investigate our crypto datasets.

* My first idea is to try to find some correlation in the log returns from bitcoin to that of gold in the 1970s.


<h2> Schedule </h2>

* Monday - 11th
    * Background research finished and a *clear* idea of data anlysis path defined
* Tuesday - 12th
    * Begin Data Analysis
* Wednesday - 13th
    * Data Analysis
* Thursday - 14th
    * Finish Data Analysis and Summarize Report
* Friday - 15th
    * Writing Report
* Saturday - 16th
    * Editing publish version
* Sunday - 17th
    * Final Version FINISHED

<h2>Methods</h2>
1. Create tools for data analysis
    a. create monte carlo simulator so we can feed in a historical return list and receive 

use of monte carlo:
when we have the whole VAR adjusted portfolio weightings then we will do a monte carlo of *those* portfolios



---
<h2>Sources and working bibliography</h2>

Inspiration from [Tudor Investor Letter](https://www.docdroid.net/H1fuimX/the-great-monetary-inflation-pdf#page=3)

Datasets come from [Yahoo Finance](https://finance.yahoo.com/)

Smirnova, Elena. **Use of Gold in Financial Risk Hedge** (https://www.jstor.org/stable/44657338?seq=1)

Harvey, Campbell; Erb, Claude. **The Golden Dilemma** (https://www.jstor.org/stable/23469534)

Manganello, S.; Engle, R. "Value at Risk Models in Finance." Working paper No.75, The European Central Bank, 2001

Rogers, L., and S. Satchell. "Estimating Variance from High, Low and
Closing Prices." Annals of Applied Volatility 1.4(1991): 504-512.

Hammoudeh, S., F. Malik, and M. McAleer. Metals." Quarterly Review of Economics

Fama, E., and K. French. "Common Risk Factors in the Returns on and Bonds." Journal of Financial Economics 33.1(1993): 3-58

Ciner, C., C. Gurdgiev, and B. Lucey. "Hedges and Safe Havens: An
Examination of Stocks, Bonds, Gold, Oil and Exchange Rates." International
Review of Financial Analysis 29.C(2013): 202-211

Conlon, T., B. Lucey, and G. Uddin. "Is Gold a Hedge Against Inflation?
A Wavelet Time-Frequency Perspective." Working paper, Trinity College,
Dublin, Ireland, 2015.

Chung, S. "The Estimation of a Firm's Hedging Effects: Marginal Value at Risk (M-VaR) Approach." *Derivatives Use, Trading * Regulation* 9.2(2003): 117-132.
