# PGR-Project
<h3><b>Stock Market Simulator</b></h3>
<h5><b>The project was developed for educational purposes.</b></h5>
This is basically a stock market simulator web application based is based on the Django framework. You can find a list of stocks under NIFTY-50, NIFTY-500, BANKNIFTY.... and many other indices as well. This allows you to trade shares of companies using virtual money, thus helping you to gain trading experience without risking your money! The project is still open to a lot of changes and upgrades.<br>
The main functionalities of the project include - 
<ul>
  <li><b>Rendering real-time prices for different stocks and indices.<b></li><br>
    We are web-scrapping the stock prices from other websites. For this, we are using the Beautiful Soup Python library. Different threads will be running in the background that will fetch the latest stock prices and update the dictionaries. Websites used for web-scrapping include Moneycontrol.com, in.finance.yahoo.com, etc ( the web app was developed only for educational purposes and not for any business activity). The real-time prices are rendered on the HTML using AJAX calls. AJAX calls are made to the server requesting new data about the price of the stock.
  <li>Access to virtual cash to buy and sell stocks.</li>
  <li>User's transaction page to list all the transactions carried out.</li>
</ul>
<p align="center">
  <img src="asset/img/undraw_posting_photo.svg" width="350" title="hover text">
</p>
