## Facebook page - Auto posting tool
This tool can be used to post (Image + Text) directly to the page you manage.


### How to use this program ?
### 1. fp_config.ini 
1. fill your access token using this tool [Facebook developer](https://developers.facebook.com/tools/explorer/). Never forget to tick the page manage permissions.
2. image file path
3. text you want to put on your page
4. Page ID
5. Page Name (not required)

Sample idea 
```text
[ACCESS_TOKEN]
access_token = EAACEose0cBAOCHQkwPet1cyd8AxmddHQ1G4PdrehZAju6SsUZCaLKsW4m4Ig7LTXPscGNd19mngy1zqXbr7qv19ZBYCKcQZCerIgTprKQLjYn0


[PAGE_01]
page_name = I have born to Win
page_id = 349846765475688
message = #Attitude #Winner #BorntoWin #Goals #SuccessQuotes #Determination
image_file = media/success.jpg


[PAGE_02]
page_name = Hugh Jackman - Wolverine
page_id = 330464567403738
message = #HughJackman #FansClub #Wolverine #Forever
image_file = media/hugh_jackman.jpg


[PAGE_03]
page_name = Farming - A Life Essential Skill
page_id = 384058171992290
message = #Farmers #Lifesavers #Farming #Agriculture #FarmersFamily #Farmerson #FarmerDaughter #FarmingLife #Nature
image_file = media/farmers.jpeg


```

### 2. fp_publish.py

Just run this program - nothing to configure inside

Happy Hacking :) 
