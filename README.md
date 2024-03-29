# PGR-Project
<h3><b>Stock Market Simulator</b></h3>
<h5><b>The project was developed for educational purposes.</b></h5>
This is basically a stock market simulator web application based on the Django framework. You can find a list of stocks under NIFTY-50, NIFTY-500, BANKNIFTY.... and many other indices as well. This allows you to trade shares of companies using virtual money, thus helping you to gain trading experience without risking your money! The project is still open to a lot of changes and upgrades. The project uses MySQL database to store information.<br><br><br>
<p align="center">
  <img src="asset/img/indices.jpg.png" width="1500" title="Major Indices Page">
</p>
<br><br><br>
The main functionalities of the project include - 
<ul>
  <li><b>Rendering real-time prices for different stocks and indices</b></li>
    We are web-scrapping the stock prices from other websites. For this, we are using the Beautiful Soup Python library. Different threads will be running in the background that will fetch the latest stock prices and update the dictionaries. Websites used for web-scrapping include Moneycontrol.com, in.finance.yahoo.com, etc ( the web app was developed only for educational purposes and not for any business activity). The real-time prices are rendered on the HTML using AJAX calls. AJAX calls are made to the server requesting new data about the price of the stock.<br>
  <p align="center"  style="margin-top:5px;">
  <img src="asset/img/stock.png" width="700" title="hover text">
</p>
  <br><br>
  <li><b>Access to virtual cash to buy and sell stocks</b></li>
  Each user is provided with virtual cash, which can be used to trade stocks. This way, users can simulate the trading environment without actually putting their money in the play.<br>
  <p align="center"  style="margin-top:5px;">
  <img src="asset/img/stockpage.png" width="1500" title="hover text">
</p>
  <br><br>
  <li><b>Trading View Charts for Stock Analysis</b></li>
    We have embedded the Trading View Charts to help traders review the technical and fundamental analysis of the stocks.<br>
   <p align="center" style="margin-top:5px;">
  <img src="asset/img/tradingview.png" width="1500" title="hover text">
</p>
  <br><br>
  <li><b>Admin Panel</b></li>
    The Admin-Panel is used to verify the users registering on the portal. It can be further developed to give more features to control/monitor the activities carried out on the application.<br>
 <p align="center" style="margin-top:5px;">
  <img src="asset/img/admin.png" width="1200" title="hover text">
</p>
</ul>

