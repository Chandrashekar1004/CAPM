This project implements Capital Asset Pricing Model (CAPM) analysis using weekly stock data.
It computes risk-adjusted performance measures such as the Sharpe Ratio and Treynor Ratio, and performs CAPM regression for selected stocks relative to the S&P 500 market index.

The analysis is performed on 50 weeks of data (one observation per week), making the project lightweight while still capturing systematic risk relationships.

Stocks analyzed:

Netflix (NFLX)
Navitas (NVTS)

Market proxy:

S&P 500 Index

Risk-free rate:

US Treasury Bill (T-Bill) data

. Return Calculation

Simple weekly returns are computed for each stock and the market index:

Rt=Pt−Pt−1Pt−1
R
t
	​

=
P
t−1
	​

P
t
	​

−P
t−1
	​

	​

2. Risk-Free Adjustment

Weekly risk-free rate is extracted from Treasury Bill data.

Excess returns are computed as:

Rtexcess=Rt−Rf
R
t
excess
	​

=R
t
	​

−R
f
	​

3. Performance Metrics
Sharpe Ratio

Measures risk-adjusted return relative to total volatility:

Sharpe=E[R−Rf]σ(R)
Sharpe=
σ(R)
E[R−R
f
	​

]
	​

Treynor Ratio

Measures return per unit of systematic risk:

Treynor=E[R−Rf]β
Treynor=
β
E[R−Rf]

  CAPM Regression

The CAPM regression is implemented as:

Ri−Rf=α+β(Rm−Rf)+ϵ
R
i
	​

−R
f
	​

=α+β(R
m
	​

−R
f
	​

)+ϵ

Where:

Ri
R
i
	​

: Stock return (NFLX or NVDA)

Rm
R
m
	​

: Market return (S&P 500)

Rf
R
f
	​

: Risk-free rate

β
β: Systematic risk

α
α: Abnormal return

The regression estimates:

Beta (β) — market sensitivity

Alpha (α) — excess performance

Residual variance​

]
	​
