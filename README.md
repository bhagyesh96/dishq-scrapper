# dishq-scrapper

1   > In Terminal go to dishq folder <br>
2.1 > type "scrapy runspider zomato.py -o data.json" <br>
2.2 > it will return "data.json" file in dishq directory <br>
2.3 > if data.json file is empty delete data.json and repeat step 2.1 again <br> 
2.4 > if problem persist copy url form "zomato.py" file paste in browser ,load thet url and replace that url with new url in that file <br>
3   > run Django app "web" <br>
4   > log on to "127.0.0.1/dash/zomato" <br>
5   > you will see all Scraped data on web page  <br>

<h1>Trouble shoot</h1>
  1 > to test web app rename test.json to data.json and run Django app
  2 > if it is not locating "data.json" change path in "zomato/views" for json file
  

