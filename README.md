# MACD Analysis for Cryptocurrencies (Dogecoin & Bitcoin)
## Note: Code variables, comments, and report (sprawozdanie.pdf) are in Polish.

Python-based evaluation of the MACD indicator's effectiveness for Dogecoin and Bitcoin markets with report made using LaTeX. 
Developed as part of a Numerical Methods course at Gdańsk University of Technology.

## Author
- Karolina Glaza [GitHub](https://github.com/kequel)

## Key Features  
- **MACD Implementation**: EMA, MACD, SIGNAL -  using only numpy.  
- **Dynamic Visualization**: Price charts, MACD/SIGNAL lines, and buy/sell signals.  
- **Investment Simulation**: Tests strategies with $1000 starting capital.  
- **Comparative Analysis**: Dogecoin (high volatility) vs. Bitcoin (more stable market).  

## Files  
| File | Description | 
|------|-------------|
| [`dogecoin.py`](dogecoin.py) | MACD analysis pipeline for Dogecoin |
| [`bitcoin.py`](bitcoin.py) | MACD analysis pipeline for Bitcoin | 
| [`funkcje.py`](funkcje.py) | Core functions (`calculate_ema`, `calculate_macd`) |
| [`sprawozdanie.pdf`](sprawozdanie.pdf) | Full report with conclusions |

## Results (from sprawozdanie.pdf)

### Dogecoin (2021-2025)  
- **Final Capital**: $155.39 (84.6% loss)  
- **Transactions**: 62 (17 profitable, 45 unprofitable)   

### Bitcoin (2021-2025)  
- **Final Capital**: $754.02 (24.6% loss)  
- **Transactions**: 54 (18 profitable, 36 unprofitable)  

## Installation  
1. Clone the repository:  
```bash  
git clone https://github.com/kequel/macd-analysis.git
```
Install dependencies:
```bash
pip install pandas numpy matplotlib
```
Run the analysis:
```bash
python dogecoin.py #for Dogecoin  
python bitcoin.py #for Bitcoin
```  
Generated charts are saved in the wykresy/ folder. 
