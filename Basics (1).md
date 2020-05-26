
# Cleaning Data in Phython

This is practice cleaning data in Python. I will be using a [sample of 50,000 data points](https://www.kaggle.com/orgesleka/used-cars-database/data) regarding used car sales via the German eBay. In this project I will be using the pandas and NumPy libraries. 


```python
import pandas as pd
import numpy as np

autos = pd.read_csv("autos.csv", encoding = "Latin-1")
```


```python
autos
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>dateCrawled</th>
      <th>name</th>
      <th>seller</th>
      <th>offerType</th>
      <th>price</th>
      <th>abtest</th>
      <th>vehicleType</th>
      <th>yearOfRegistration</th>
      <th>gearbox</th>
      <th>powerPS</th>
      <th>model</th>
      <th>odometer</th>
      <th>monthOfRegistration</th>
      <th>fuelType</th>
      <th>brand</th>
      <th>notRepairedDamage</th>
      <th>dateCreated</th>
      <th>nrOfPictures</th>
      <th>postalCode</th>
      <th>lastSeen</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2016-03-26 17:47:46</td>
      <td>Peugeot_807_160_NAVTECH_ON_BOARD</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$5,000</td>
      <td>control</td>
      <td>bus</td>
      <td>2004</td>
      <td>manuell</td>
      <td>158</td>
      <td>andere</td>
      <td>150,000km</td>
      <td>3</td>
      <td>lpg</td>
      <td>peugeot</td>
      <td>nein</td>
      <td>2016-03-26 00:00:00</td>
      <td>0</td>
      <td>79588</td>
      <td>2016-04-06 06:45:54</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2016-04-04 13:38:56</td>
      <td>BMW_740i_4_4_Liter_HAMANN_UMBAU_Mega_Optik</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$8,500</td>
      <td>control</td>
      <td>limousine</td>
      <td>1997</td>
      <td>automatik</td>
      <td>286</td>
      <td>7er</td>
      <td>150,000km</td>
      <td>6</td>
      <td>benzin</td>
      <td>bmw</td>
      <td>nein</td>
      <td>2016-04-04 00:00:00</td>
      <td>0</td>
      <td>71034</td>
      <td>2016-04-06 14:45:08</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2016-03-26 18:57:24</td>
      <td>Volkswagen_Golf_1.6_United</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$8,990</td>
      <td>test</td>
      <td>limousine</td>
      <td>2009</td>
      <td>manuell</td>
      <td>102</td>
      <td>golf</td>
      <td>70,000km</td>
      <td>7</td>
      <td>benzin</td>
      <td>volkswagen</td>
      <td>nein</td>
      <td>2016-03-26 00:00:00</td>
      <td>0</td>
      <td>35394</td>
      <td>2016-04-06 20:15:37</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2016-03-12 16:58:10</td>
      <td>Smart_smart_fortwo_coupe_softouch/F1/Klima/Pan...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$4,350</td>
      <td>control</td>
      <td>kleinwagen</td>
      <td>2007</td>
      <td>automatik</td>
      <td>71</td>
      <td>fortwo</td>
      <td>70,000km</td>
      <td>6</td>
      <td>benzin</td>
      <td>smart</td>
      <td>nein</td>
      <td>2016-03-12 00:00:00</td>
      <td>0</td>
      <td>33729</td>
      <td>2016-03-15 03:16:28</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016-04-01 14:38:50</td>
      <td>Ford_Focus_1_6_Benzin_TÜV_neu_ist_sehr_gepfleg...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$1,350</td>
      <td>test</td>
      <td>kombi</td>
      <td>2003</td>
      <td>manuell</td>
      <td>0</td>
      <td>focus</td>
      <td>150,000km</td>
      <td>7</td>
      <td>benzin</td>
      <td>ford</td>
      <td>nein</td>
      <td>2016-04-01 00:00:00</td>
      <td>0</td>
      <td>39218</td>
      <td>2016-04-01 14:38:50</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2016-03-21 13:47:45</td>
      <td>Chrysler_Grand_Voyager_2.8_CRD_Aut.Limited_Sto...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$7,900</td>
      <td>test</td>
      <td>bus</td>
      <td>2006</td>
      <td>automatik</td>
      <td>150</td>
      <td>voyager</td>
      <td>150,000km</td>
      <td>4</td>
      <td>diesel</td>
      <td>chrysler</td>
      <td>NaN</td>
      <td>2016-03-21 00:00:00</td>
      <td>0</td>
      <td>22962</td>
      <td>2016-04-06 09:45:21</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2016-03-20 17:55:21</td>
      <td>VW_Golf_III_GT_Special_Electronic_Green_Metall...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$300</td>
      <td>test</td>
      <td>limousine</td>
      <td>1995</td>
      <td>manuell</td>
      <td>90</td>
      <td>golf</td>
      <td>150,000km</td>
      <td>8</td>
      <td>benzin</td>
      <td>volkswagen</td>
      <td>NaN</td>
      <td>2016-03-20 00:00:00</td>
      <td>0</td>
      <td>31535</td>
      <td>2016-03-23 02:48:59</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2016-03-16 18:55:19</td>
      <td>Golf_IV_1.9_TDI_90PS</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$1,990</td>
      <td>control</td>
      <td>limousine</td>
      <td>1998</td>
      <td>manuell</td>
      <td>90</td>
      <td>golf</td>
      <td>150,000km</td>
      <td>12</td>
      <td>diesel</td>
      <td>volkswagen</td>
      <td>nein</td>
      <td>2016-03-16 00:00:00</td>
      <td>0</td>
      <td>53474</td>
      <td>2016-04-07 03:17:32</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2016-03-22 16:51:34</td>
      <td>Seat_Arosa</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$250</td>
      <td>test</td>
      <td>NaN</td>
      <td>2000</td>
      <td>manuell</td>
      <td>0</td>
      <td>arosa</td>
      <td>150,000km</td>
      <td>10</td>
      <td>NaN</td>
      <td>seat</td>
      <td>nein</td>
      <td>2016-03-22 00:00:00</td>
      <td>0</td>
      <td>7426</td>
      <td>2016-03-26 18:18:10</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2016-03-16 13:47:02</td>
      <td>Renault_Megane_Scenic_1.6e_RT_Klimaanlage</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$590</td>
      <td>control</td>
      <td>bus</td>
      <td>1997</td>
      <td>manuell</td>
      <td>90</td>
      <td>megane</td>
      <td>150,000km</td>
      <td>7</td>
      <td>benzin</td>
      <td>renault</td>
      <td>nein</td>
      <td>2016-03-16 00:00:00</td>
      <td>0</td>
      <td>15749</td>
      <td>2016-04-06 10:46:35</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2016-03-15 01:41:36</td>
      <td>VW_Golf_Tuning_in_siber/grau</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$999</td>
      <td>test</td>
      <td>NaN</td>
      <td>2017</td>
      <td>manuell</td>
      <td>90</td>
      <td>NaN</td>
      <td>150,000km</td>
      <td>4</td>
      <td>benzin</td>
      <td>volkswagen</td>
      <td>nein</td>
      <td>2016-03-14 00:00:00</td>
      <td>0</td>
      <td>86157</td>
      <td>2016-04-07 03:16:21</td>
    </tr>
    <tr>
      <th>11</th>
      <td>2016-03-16 18:45:34</td>
      <td>Mercedes_A140_Motorschaden</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$350</td>
      <td>control</td>
      <td>NaN</td>
      <td>2000</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>150,000km</td>
      <td>0</td>
      <td>benzin</td>
      <td>mercedes_benz</td>
      <td>NaN</td>
      <td>2016-03-16 00:00:00</td>
      <td>0</td>
      <td>17498</td>
      <td>2016-03-16 18:45:34</td>
    </tr>
    <tr>
      <th>12</th>
      <td>2016-03-31 19:48:22</td>
      <td>Smart_smart_fortwo_coupe_softouch_pure_MHD_Pan...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$5,299</td>
      <td>control</td>
      <td>kleinwagen</td>
      <td>2010</td>
      <td>automatik</td>
      <td>71</td>
      <td>fortwo</td>
      <td>50,000km</td>
      <td>9</td>
      <td>benzin</td>
      <td>smart</td>
      <td>nein</td>
      <td>2016-03-31 00:00:00</td>
      <td>0</td>
      <td>34590</td>
      <td>2016-04-06 14:17:52</td>
    </tr>
    <tr>
      <th>13</th>
      <td>2016-03-23 10:48:32</td>
      <td>Audi_A3_1.6_tuning</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$1,350</td>
      <td>control</td>
      <td>limousine</td>
      <td>1999</td>
      <td>manuell</td>
      <td>101</td>
      <td>a3</td>
      <td>150,000km</td>
      <td>11</td>
      <td>benzin</td>
      <td>audi</td>
      <td>nein</td>
      <td>2016-03-23 00:00:00</td>
      <td>0</td>
      <td>12043</td>
      <td>2016-04-01 14:17:13</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2016-03-23 11:50:46</td>
      <td>Renault_Clio_3__Dynamique_1.2__16_V;_viele_Ver...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$3,999</td>
      <td>test</td>
      <td>kleinwagen</td>
      <td>2007</td>
      <td>manuell</td>
      <td>75</td>
      <td>clio</td>
      <td>150,000km</td>
      <td>9</td>
      <td>benzin</td>
      <td>renault</td>
      <td>NaN</td>
      <td>2016-03-23 00:00:00</td>
      <td>0</td>
      <td>81737</td>
      <td>2016-04-01 15:46:47</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2016-04-01 12:06:20</td>
      <td>Corvette_C3_Coupe_T_Top_Crossfire_Injection</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$18,900</td>
      <td>test</td>
      <td>coupe</td>
      <td>1982</td>
      <td>automatik</td>
      <td>203</td>
      <td>NaN</td>
      <td>80,000km</td>
      <td>6</td>
      <td>benzin</td>
      <td>sonstige_autos</td>
      <td>nein</td>
      <td>2016-04-01 00:00:00</td>
      <td>0</td>
      <td>61276</td>
      <td>2016-04-02 21:10:48</td>
    </tr>
    <tr>
      <th>16</th>
      <td>2016-03-16 14:59:02</td>
      <td>Opel_Vectra_B_Kombi</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$350</td>
      <td>test</td>
      <td>kombi</td>
      <td>1999</td>
      <td>manuell</td>
      <td>101</td>
      <td>vectra</td>
      <td>150,000km</td>
      <td>5</td>
      <td>benzin</td>
      <td>opel</td>
      <td>nein</td>
      <td>2016-03-16 00:00:00</td>
      <td>0</td>
      <td>57299</td>
      <td>2016-03-18 05:29:37</td>
    </tr>
    <tr>
      <th>17</th>
      <td>2016-03-29 11:46:22</td>
      <td>Volkswagen_Scirocco_2_G60</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$5,500</td>
      <td>test</td>
      <td>coupe</td>
      <td>1990</td>
      <td>manuell</td>
      <td>205</td>
      <td>scirocco</td>
      <td>150,000km</td>
      <td>6</td>
      <td>benzin</td>
      <td>volkswagen</td>
      <td>nein</td>
      <td>2016-03-29 00:00:00</td>
      <td>0</td>
      <td>74821</td>
      <td>2016-04-05 20:46:26</td>
    </tr>
    <tr>
      <th>18</th>
      <td>2016-03-26 19:57:44</td>
      <td>Verkaufen_mein_bmw_e36_320_i_touring</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$300</td>
      <td>control</td>
      <td>bus</td>
      <td>1995</td>
      <td>manuell</td>
      <td>150</td>
      <td>3er</td>
      <td>150,000km</td>
      <td>0</td>
      <td>benzin</td>
      <td>bmw</td>
      <td>NaN</td>
      <td>2016-03-26 00:00:00</td>
      <td>0</td>
      <td>54329</td>
      <td>2016-04-02 12:16:41</td>
    </tr>
    <tr>
      <th>19</th>
      <td>2016-03-17 13:36:21</td>
      <td>mazda_tribute_2.0_mit_gas_und_tuev_neu_2018</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$4,150</td>
      <td>control</td>
      <td>suv</td>
      <td>2004</td>
      <td>manuell</td>
      <td>124</td>
      <td>andere</td>
      <td>150,000km</td>
      <td>2</td>
      <td>lpg</td>
      <td>mazda</td>
      <td>nein</td>
      <td>2016-03-17 00:00:00</td>
      <td>0</td>
      <td>40878</td>
      <td>2016-03-17 14:45:58</td>
    </tr>
    <tr>
      <th>20</th>
      <td>2016-03-05 19:57:31</td>
      <td>Audi_A4_Avant_1.9_TDI_*6_Gang*AHK*Klimatronik*...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$3,500</td>
      <td>test</td>
      <td>kombi</td>
      <td>2003</td>
      <td>manuell</td>
      <td>131</td>
      <td>a4</td>
      <td>150,000km</td>
      <td>5</td>
      <td>diesel</td>
      <td>audi</td>
      <td>NaN</td>
      <td>2016-03-05 00:00:00</td>
      <td>0</td>
      <td>53913</td>
      <td>2016-03-07 05:46:46</td>
    </tr>
    <tr>
      <th>21</th>
      <td>2016-03-06 19:07:10</td>
      <td>Porsche_911_Carrera_4S_Cabrio</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$41,500</td>
      <td>test</td>
      <td>cabrio</td>
      <td>2004</td>
      <td>manuell</td>
      <td>320</td>
      <td>911</td>
      <td>150,000km</td>
      <td>4</td>
      <td>benzin</td>
      <td>porsche</td>
      <td>nein</td>
      <td>2016-03-06 00:00:00</td>
      <td>0</td>
      <td>65428</td>
      <td>2016-04-05 23:46:19</td>
    </tr>
    <tr>
      <th>22</th>
      <td>2016-03-28 20:50:54</td>
      <td>MINI_Cooper_S_Cabrio</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$25,450</td>
      <td>control</td>
      <td>cabrio</td>
      <td>2015</td>
      <td>manuell</td>
      <td>184</td>
      <td>cooper</td>
      <td>10,000km</td>
      <td>1</td>
      <td>benzin</td>
      <td>mini</td>
      <td>nein</td>
      <td>2016-03-28 00:00:00</td>
      <td>0</td>
      <td>44789</td>
      <td>2016-04-01 06:45:30</td>
    </tr>
    <tr>
      <th>23</th>
      <td>2016-03-10 19:55:34</td>
      <td>Peugeot_Boxer_2_2_HDi_120_Ps_9_Sitzer_inkl_Klima</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$7,999</td>
      <td>control</td>
      <td>bus</td>
      <td>2010</td>
      <td>manuell</td>
      <td>120</td>
      <td>NaN</td>
      <td>150,000km</td>
      <td>2</td>
      <td>diesel</td>
      <td>peugeot</td>
      <td>nein</td>
      <td>2016-03-10 00:00:00</td>
      <td>0</td>
      <td>30900</td>
      <td>2016-03-17 08:45:17</td>
    </tr>
    <tr>
      <th>24</th>
      <td>2016-04-03 11:57:02</td>
      <td>BMW_535i_xDrive_Sport_Aut.</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$48,500</td>
      <td>control</td>
      <td>limousine</td>
      <td>2014</td>
      <td>automatik</td>
      <td>306</td>
      <td>5er</td>
      <td>30,000km</td>
      <td>12</td>
      <td>benzin</td>
      <td>bmw</td>
      <td>nein</td>
      <td>2016-04-03 00:00:00</td>
      <td>0</td>
      <td>22547</td>
      <td>2016-04-07 13:16:50</td>
    </tr>
    <tr>
      <th>25</th>
      <td>2016-03-21 21:56:18</td>
      <td>Ford_escort_kombi_an_bastler_mit_ghia_ausstattung</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$90</td>
      <td>control</td>
      <td>kombi</td>
      <td>1996</td>
      <td>manuell</td>
      <td>116</td>
      <td>NaN</td>
      <td>150,000km</td>
      <td>4</td>
      <td>benzin</td>
      <td>ford</td>
      <td>ja</td>
      <td>2016-03-21 00:00:00</td>
      <td>0</td>
      <td>27574</td>
      <td>2016-04-01 05:16:49</td>
    </tr>
    <tr>
      <th>26</th>
      <td>2016-04-03 22:46:28</td>
      <td>Volkswagen_Polo_Fox</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$777</td>
      <td>control</td>
      <td>kleinwagen</td>
      <td>1992</td>
      <td>manuell</td>
      <td>54</td>
      <td>polo</td>
      <td>125,000km</td>
      <td>2</td>
      <td>benzin</td>
      <td>volkswagen</td>
      <td>nein</td>
      <td>2016-04-03 00:00:00</td>
      <td>0</td>
      <td>38110</td>
      <td>2016-04-05 23:46:48</td>
    </tr>
    <tr>
      <th>27</th>
      <td>2016-03-27 18:45:01</td>
      <td>Hat_einer_Ahnung_mit_Ford_Galaxy_HILFE</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$0</td>
      <td>control</td>
      <td>NaN</td>
      <td>2005</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>150,000km</td>
      <td>0</td>
      <td>NaN</td>
      <td>ford</td>
      <td>NaN</td>
      <td>2016-03-27 00:00:00</td>
      <td>0</td>
      <td>66701</td>
      <td>2016-03-27 18:45:01</td>
    </tr>
    <tr>
      <th>28</th>
      <td>2016-03-19 21:56:19</td>
      <td>MINI_Cooper_D</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$5,250</td>
      <td>control</td>
      <td>kleinwagen</td>
      <td>2007</td>
      <td>manuell</td>
      <td>110</td>
      <td>cooper</td>
      <td>150,000km</td>
      <td>7</td>
      <td>diesel</td>
      <td>mini</td>
      <td>ja</td>
      <td>2016-03-19 00:00:00</td>
      <td>0</td>
      <td>15745</td>
      <td>2016-04-07 14:58:48</td>
    </tr>
    <tr>
      <th>29</th>
      <td>2016-04-02 12:45:44</td>
      <td>Mercedes_Benz_E_320_T_CDI_Avantgarde_DPF7_Sitz...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$4,999</td>
      <td>test</td>
      <td>kombi</td>
      <td>2004</td>
      <td>automatik</td>
      <td>204</td>
      <td>e_klasse</td>
      <td>150,000km</td>
      <td>10</td>
      <td>diesel</td>
      <td>mercedes_benz</td>
      <td>nein</td>
      <td>2016-04-02 00:00:00</td>
      <td>0</td>
      <td>47638</td>
      <td>2016-04-02 12:45:44</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>49970</th>
      <td>2016-03-21 22:47:37</td>
      <td>c4_Grand_Picasso_mit_Automatik_Leder_Navi_Temp...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$15,800</td>
      <td>control</td>
      <td>bus</td>
      <td>2010</td>
      <td>automatik</td>
      <td>136</td>
      <td>c4</td>
      <td>60,000km</td>
      <td>4</td>
      <td>diesel</td>
      <td>citroen</td>
      <td>nein</td>
      <td>2016-03-21 00:00:00</td>
      <td>0</td>
      <td>14947</td>
      <td>2016-04-07 04:17:34</td>
    </tr>
    <tr>
      <th>49971</th>
      <td>2016-03-29 14:54:12</td>
      <td>W.Lupo_1.0</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$950</td>
      <td>test</td>
      <td>kleinwagen</td>
      <td>2001</td>
      <td>manuell</td>
      <td>50</td>
      <td>lupo</td>
      <td>150,000km</td>
      <td>4</td>
      <td>benzin</td>
      <td>volkswagen</td>
      <td>nein</td>
      <td>2016-03-29 00:00:00</td>
      <td>0</td>
      <td>65197</td>
      <td>2016-03-29 20:41:51</td>
    </tr>
    <tr>
      <th>49972</th>
      <td>2016-03-26 22:25:23</td>
      <td>Mercedes_Benz_Vito_115_CDI_Extralang_Aut.</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$3,300</td>
      <td>control</td>
      <td>bus</td>
      <td>2004</td>
      <td>automatik</td>
      <td>150</td>
      <td>vito</td>
      <td>150,000km</td>
      <td>10</td>
      <td>diesel</td>
      <td>mercedes_benz</td>
      <td>ja</td>
      <td>2016-03-26 00:00:00</td>
      <td>0</td>
      <td>65326</td>
      <td>2016-03-28 11:28:18</td>
    </tr>
    <tr>
      <th>49973</th>
      <td>2016-03-27 05:32:39</td>
      <td>Mercedes_Benz_SLK_200_Kompressor</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$6,000</td>
      <td>control</td>
      <td>cabrio</td>
      <td>2004</td>
      <td>manuell</td>
      <td>163</td>
      <td>slk</td>
      <td>150,000km</td>
      <td>11</td>
      <td>benzin</td>
      <td>mercedes_benz</td>
      <td>nein</td>
      <td>2016-03-27 00:00:00</td>
      <td>0</td>
      <td>53567</td>
      <td>2016-03-27 08:25:24</td>
    </tr>
    <tr>
      <th>49974</th>
      <td>2016-03-20 10:52:31</td>
      <td>Golf_1_Cabrio_Tuev_Neu_viele_Extras_alles_eing...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$0</td>
      <td>control</td>
      <td>cabrio</td>
      <td>1983</td>
      <td>manuell</td>
      <td>70</td>
      <td>golf</td>
      <td>150,000km</td>
      <td>2</td>
      <td>benzin</td>
      <td>volkswagen</td>
      <td>nein</td>
      <td>2016-03-20 00:00:00</td>
      <td>0</td>
      <td>8209</td>
      <td>2016-03-27 19:48:16</td>
    </tr>
    <tr>
      <th>49975</th>
      <td>2016-03-27 20:51:39</td>
      <td>Honda_Jazz_1.3_DSi_i_VTEC_IMA_CVT_Comfort</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$9,700</td>
      <td>control</td>
      <td>kleinwagen</td>
      <td>2012</td>
      <td>automatik</td>
      <td>88</td>
      <td>jazz</td>
      <td>100,000km</td>
      <td>11</td>
      <td>hybrid</td>
      <td>honda</td>
      <td>nein</td>
      <td>2016-03-27 00:00:00</td>
      <td>0</td>
      <td>84385</td>
      <td>2016-04-05 19:45:34</td>
    </tr>
    <tr>
      <th>49976</th>
      <td>2016-03-19 18:56:05</td>
      <td>Audi_80_Avant_2.6_E__Vollausstattung!!_Einziga...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$5,900</td>
      <td>test</td>
      <td>kombi</td>
      <td>1992</td>
      <td>automatik</td>
      <td>150</td>
      <td>80</td>
      <td>150,000km</td>
      <td>12</td>
      <td>benzin</td>
      <td>audi</td>
      <td>nein</td>
      <td>2016-03-19 00:00:00</td>
      <td>0</td>
      <td>36100</td>
      <td>2016-04-07 06:16:44</td>
    </tr>
    <tr>
      <th>49977</th>
      <td>2016-03-31 18:37:18</td>
      <td>Mercedes_Benz_C200_Cdi_W203</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$5,500</td>
      <td>control</td>
      <td>limousine</td>
      <td>2003</td>
      <td>manuell</td>
      <td>116</td>
      <td>c_klasse</td>
      <td>150,000km</td>
      <td>2</td>
      <td>diesel</td>
      <td>mercedes_benz</td>
      <td>nein</td>
      <td>2016-03-31 00:00:00</td>
      <td>0</td>
      <td>33739</td>
      <td>2016-04-06 12:16:11</td>
    </tr>
    <tr>
      <th>49978</th>
      <td>2016-04-04 10:37:14</td>
      <td>Mercedes_Benz_E_200_Classic</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$900</td>
      <td>control</td>
      <td>limousine</td>
      <td>1996</td>
      <td>automatik</td>
      <td>136</td>
      <td>e_klasse</td>
      <td>150,000km</td>
      <td>9</td>
      <td>benzin</td>
      <td>mercedes_benz</td>
      <td>ja</td>
      <td>2016-04-04 00:00:00</td>
      <td>0</td>
      <td>24405</td>
      <td>2016-04-06 12:44:20</td>
    </tr>
    <tr>
      <th>49979</th>
      <td>2016-03-20 18:38:40</td>
      <td>Volkswagen_Polo_1.6_TDI_Style</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$11,000</td>
      <td>test</td>
      <td>kleinwagen</td>
      <td>2011</td>
      <td>manuell</td>
      <td>90</td>
      <td>polo</td>
      <td>70,000km</td>
      <td>11</td>
      <td>diesel</td>
      <td>volkswagen</td>
      <td>nein</td>
      <td>2016-03-20 00:00:00</td>
      <td>0</td>
      <td>48455</td>
      <td>2016-04-07 01:45:12</td>
    </tr>
    <tr>
      <th>49980</th>
      <td>2016-03-12 10:55:54</td>
      <td>Ford_Escort_Turnier_16V</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$400</td>
      <td>control</td>
      <td>kombi</td>
      <td>1995</td>
      <td>manuell</td>
      <td>105</td>
      <td>escort</td>
      <td>125,000km</td>
      <td>3</td>
      <td>benzin</td>
      <td>ford</td>
      <td>NaN</td>
      <td>2016-03-12 00:00:00</td>
      <td>0</td>
      <td>56218</td>
      <td>2016-04-06 17:16:49</td>
    </tr>
    <tr>
      <th>49981</th>
      <td>2016-03-15 09:38:21</td>
      <td>Opel_Astra_Kombi_mit_Anhaengerkupplung</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$2,000</td>
      <td>control</td>
      <td>kombi</td>
      <td>1998</td>
      <td>manuell</td>
      <td>115</td>
      <td>astra</td>
      <td>150,000km</td>
      <td>12</td>
      <td>benzin</td>
      <td>opel</td>
      <td>nein</td>
      <td>2016-03-15 00:00:00</td>
      <td>0</td>
      <td>86859</td>
      <td>2016-04-05 17:21:46</td>
    </tr>
    <tr>
      <th>49982</th>
      <td>2016-03-29 18:51:08</td>
      <td>Skoda_Fabia_4_Tuerer_Bj:2004__85.000Tkm</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$1,950</td>
      <td>control</td>
      <td>kleinwagen</td>
      <td>2004</td>
      <td>manuell</td>
      <td>0</td>
      <td>fabia</td>
      <td>90,000km</td>
      <td>7</td>
      <td>benzin</td>
      <td>skoda</td>
      <td>NaN</td>
      <td>2016-03-29 00:00:00</td>
      <td>0</td>
      <td>45884</td>
      <td>2016-03-29 18:51:08</td>
    </tr>
    <tr>
      <th>49983</th>
      <td>2016-03-06 12:43:04</td>
      <td>Ford_focus_99</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$600</td>
      <td>test</td>
      <td>kleinwagen</td>
      <td>1999</td>
      <td>manuell</td>
      <td>101</td>
      <td>focus</td>
      <td>150,000km</td>
      <td>4</td>
      <td>benzin</td>
      <td>ford</td>
      <td>NaN</td>
      <td>2016-03-06 00:00:00</td>
      <td>0</td>
      <td>52477</td>
      <td>2016-03-09 06:16:08</td>
    </tr>
    <tr>
      <th>49984</th>
      <td>2016-03-31 22:48:48</td>
      <td>Student_sucht_ein__Anfaengerauto___ab_2000_BJ_...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$0</td>
      <td>test</td>
      <td>NaN</td>
      <td>2000</td>
      <td>NaN</td>
      <td>0</td>
      <td>NaN</td>
      <td>150,000km</td>
      <td>0</td>
      <td>NaN</td>
      <td>sonstige_autos</td>
      <td>NaN</td>
      <td>2016-03-31 00:00:00</td>
      <td>0</td>
      <td>12103</td>
      <td>2016-04-02 19:44:53</td>
    </tr>
    <tr>
      <th>49985</th>
      <td>2016-04-02 16:38:23</td>
      <td>Verkaufe_meinen_vw_vento!</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$1,000</td>
      <td>control</td>
      <td>NaN</td>
      <td>1995</td>
      <td>automatik</td>
      <td>0</td>
      <td>NaN</td>
      <td>150,000km</td>
      <td>0</td>
      <td>benzin</td>
      <td>volkswagen</td>
      <td>NaN</td>
      <td>2016-04-02 00:00:00</td>
      <td>0</td>
      <td>30900</td>
      <td>2016-04-06 15:17:52</td>
    </tr>
    <tr>
      <th>49986</th>
      <td>2016-04-04 20:46:02</td>
      <td>Chrysler_300C_3.0_CRD_DPF_Automatik_Voll_Ausst...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$15,900</td>
      <td>control</td>
      <td>limousine</td>
      <td>2010</td>
      <td>automatik</td>
      <td>218</td>
      <td>300c</td>
      <td>125,000km</td>
      <td>11</td>
      <td>diesel</td>
      <td>chrysler</td>
      <td>nein</td>
      <td>2016-04-04 00:00:00</td>
      <td>0</td>
      <td>73527</td>
      <td>2016-04-06 23:16:00</td>
    </tr>
    <tr>
      <th>49987</th>
      <td>2016-03-22 20:47:27</td>
      <td>Audi_A3_Limousine_2.0_TDI_DPF_Ambition__NAVI__...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$21,990</td>
      <td>control</td>
      <td>limousine</td>
      <td>2013</td>
      <td>manuell</td>
      <td>150</td>
      <td>a3</td>
      <td>50,000km</td>
      <td>11</td>
      <td>diesel</td>
      <td>audi</td>
      <td>nein</td>
      <td>2016-03-22 00:00:00</td>
      <td>0</td>
      <td>94362</td>
      <td>2016-03-26 22:46:06</td>
    </tr>
    <tr>
      <th>49988</th>
      <td>2016-03-28 19:49:51</td>
      <td>BMW_330_Ci</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$9,550</td>
      <td>control</td>
      <td>coupe</td>
      <td>2001</td>
      <td>manuell</td>
      <td>231</td>
      <td>3er</td>
      <td>150,000km</td>
      <td>10</td>
      <td>benzin</td>
      <td>bmw</td>
      <td>nein</td>
      <td>2016-03-28 00:00:00</td>
      <td>0</td>
      <td>83646</td>
      <td>2016-04-07 02:17:40</td>
    </tr>
    <tr>
      <th>49989</th>
      <td>2016-03-11 19:50:37</td>
      <td>VW_Polo_zum_Ausschlachten_oder_Wiederaufbau</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$150</td>
      <td>test</td>
      <td>kleinwagen</td>
      <td>1997</td>
      <td>manuell</td>
      <td>0</td>
      <td>polo</td>
      <td>150,000km</td>
      <td>5</td>
      <td>benzin</td>
      <td>volkswagen</td>
      <td>ja</td>
      <td>2016-03-11 00:00:00</td>
      <td>0</td>
      <td>21244</td>
      <td>2016-03-12 10:17:55</td>
    </tr>
    <tr>
      <th>49990</th>
      <td>2016-03-21 19:54:19</td>
      <td>Mercedes_Benz_A_200__BlueEFFICIENCY__Urban</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$17,500</td>
      <td>test</td>
      <td>limousine</td>
      <td>2012</td>
      <td>manuell</td>
      <td>156</td>
      <td>a_klasse</td>
      <td>30,000km</td>
      <td>12</td>
      <td>benzin</td>
      <td>mercedes_benz</td>
      <td>nein</td>
      <td>2016-03-21 00:00:00</td>
      <td>0</td>
      <td>58239</td>
      <td>2016-04-06 22:46:57</td>
    </tr>
    <tr>
      <th>49991</th>
      <td>2016-03-06 15:25:19</td>
      <td>Kleinwagen</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$500</td>
      <td>control</td>
      <td>NaN</td>
      <td>2016</td>
      <td>manuell</td>
      <td>0</td>
      <td>twingo</td>
      <td>150,000km</td>
      <td>0</td>
      <td>benzin</td>
      <td>renault</td>
      <td>NaN</td>
      <td>2016-03-06 00:00:00</td>
      <td>0</td>
      <td>61350</td>
      <td>2016-03-06 18:24:19</td>
    </tr>
    <tr>
      <th>49992</th>
      <td>2016-03-10 19:37:38</td>
      <td>Fiat_Grande_Punto_1.4_T_Jet_16V_Sport</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$4,800</td>
      <td>control</td>
      <td>kleinwagen</td>
      <td>2009</td>
      <td>manuell</td>
      <td>120</td>
      <td>andere</td>
      <td>125,000km</td>
      <td>9</td>
      <td>lpg</td>
      <td>fiat</td>
      <td>nein</td>
      <td>2016-03-10 00:00:00</td>
      <td>0</td>
      <td>68642</td>
      <td>2016-03-13 01:44:51</td>
    </tr>
    <tr>
      <th>49993</th>
      <td>2016-03-15 18:47:35</td>
      <td>Audi_A3__1_8l__Silber;_schoenes_Fahrzeug</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$1,650</td>
      <td>control</td>
      <td>kleinwagen</td>
      <td>1997</td>
      <td>manuell</td>
      <td>0</td>
      <td>NaN</td>
      <td>150,000km</td>
      <td>7</td>
      <td>benzin</td>
      <td>audi</td>
      <td>NaN</td>
      <td>2016-03-15 00:00:00</td>
      <td>0</td>
      <td>65203</td>
      <td>2016-04-06 19:46:53</td>
    </tr>
    <tr>
      <th>49994</th>
      <td>2016-03-22 17:36:42</td>
      <td>Audi_A6__S6__Avant_4.2_quattro_eventuell_Tausc...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$5,000</td>
      <td>control</td>
      <td>kombi</td>
      <td>2001</td>
      <td>automatik</td>
      <td>299</td>
      <td>a6</td>
      <td>150,000km</td>
      <td>1</td>
      <td>benzin</td>
      <td>audi</td>
      <td>nein</td>
      <td>2016-03-22 00:00:00</td>
      <td>0</td>
      <td>46537</td>
      <td>2016-04-06 08:16:39</td>
    </tr>
    <tr>
      <th>49995</th>
      <td>2016-03-27 14:38:19</td>
      <td>Audi_Q5_3.0_TDI_qu._S_tr.__Navi__Panorama__Xenon</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$24,900</td>
      <td>control</td>
      <td>limousine</td>
      <td>2011</td>
      <td>automatik</td>
      <td>239</td>
      <td>q5</td>
      <td>100,000km</td>
      <td>1</td>
      <td>diesel</td>
      <td>audi</td>
      <td>nein</td>
      <td>2016-03-27 00:00:00</td>
      <td>0</td>
      <td>82131</td>
      <td>2016-04-01 13:47:40</td>
    </tr>
    <tr>
      <th>49996</th>
      <td>2016-03-28 10:50:25</td>
      <td>Opel_Astra_F_Cabrio_Bertone_Edition___TÜV_neu+...</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$1,980</td>
      <td>control</td>
      <td>cabrio</td>
      <td>1996</td>
      <td>manuell</td>
      <td>75</td>
      <td>astra</td>
      <td>150,000km</td>
      <td>5</td>
      <td>benzin</td>
      <td>opel</td>
      <td>nein</td>
      <td>2016-03-28 00:00:00</td>
      <td>0</td>
      <td>44807</td>
      <td>2016-04-02 14:18:02</td>
    </tr>
    <tr>
      <th>49997</th>
      <td>2016-04-02 14:44:48</td>
      <td>Fiat_500_C_1.2_Dualogic_Lounge</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$13,200</td>
      <td>test</td>
      <td>cabrio</td>
      <td>2014</td>
      <td>automatik</td>
      <td>69</td>
      <td>500</td>
      <td>5,000km</td>
      <td>11</td>
      <td>benzin</td>
      <td>fiat</td>
      <td>nein</td>
      <td>2016-04-02 00:00:00</td>
      <td>0</td>
      <td>73430</td>
      <td>2016-04-04 11:47:27</td>
    </tr>
    <tr>
      <th>49998</th>
      <td>2016-03-08 19:25:42</td>
      <td>Audi_A3_2.0_TDI_Sportback_Ambition</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$22,900</td>
      <td>control</td>
      <td>kombi</td>
      <td>2013</td>
      <td>manuell</td>
      <td>150</td>
      <td>a3</td>
      <td>40,000km</td>
      <td>11</td>
      <td>diesel</td>
      <td>audi</td>
      <td>nein</td>
      <td>2016-03-08 00:00:00</td>
      <td>0</td>
      <td>35683</td>
      <td>2016-04-05 16:45:07</td>
    </tr>
    <tr>
      <th>49999</th>
      <td>2016-03-14 00:42:12</td>
      <td>Opel_Vectra_1.6_16V</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$1,250</td>
      <td>control</td>
      <td>limousine</td>
      <td>1996</td>
      <td>manuell</td>
      <td>101</td>
      <td>vectra</td>
      <td>150,000km</td>
      <td>1</td>
      <td>benzin</td>
      <td>opel</td>
      <td>nein</td>
      <td>2016-03-13 00:00:00</td>
      <td>0</td>
      <td>45897</td>
      <td>2016-04-06 21:18:48</td>
    </tr>
  </tbody>
</table>
<p>50000 rows × 20 columns</p>
</div>




```python
print(autos.info())
print(autos.head())
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 50000 entries, 0 to 49999
    Data columns (total 20 columns):
    dateCrawled            50000 non-null object
    name                   50000 non-null object
    seller                 50000 non-null object
    offerType              50000 non-null object
    price                  50000 non-null object
    abtest                 50000 non-null object
    vehicleType            44905 non-null object
    yearOfRegistration     50000 non-null int64
    gearbox                47320 non-null object
    powerPS                50000 non-null int64
    model                  47242 non-null object
    odometer               50000 non-null object
    monthOfRegistration    50000 non-null int64
    fuelType               45518 non-null object
    brand                  50000 non-null object
    notRepairedDamage      40171 non-null object
    dateCreated            50000 non-null object
    nrOfPictures           50000 non-null int64
    postalCode             50000 non-null int64
    lastSeen               50000 non-null object
    dtypes: int64(5), object(15)
    memory usage: 7.6+ MB
    None
               dateCrawled                                               name  \
    0  2016-03-26 17:47:46                   Peugeot_807_160_NAVTECH_ON_BOARD   
    1  2016-04-04 13:38:56         BMW_740i_4_4_Liter_HAMANN_UMBAU_Mega_Optik   
    2  2016-03-26 18:57:24                         Volkswagen_Golf_1.6_United   
    3  2016-03-12 16:58:10  Smart_smart_fortwo_coupe_softouch/F1/Klima/Pan...   
    4  2016-04-01 14:38:50  Ford_Focus_1_6_Benzin_TÜV_neu_ist_sehr_gepfleg...   
    
       seller offerType   price   abtest vehicleType  yearOfRegistration  \
    0  privat   Angebot  $5,000  control         bus                2004   
    1  privat   Angebot  $8,500  control   limousine                1997   
    2  privat   Angebot  $8,990     test   limousine                2009   
    3  privat   Angebot  $4,350  control  kleinwagen                2007   
    4  privat   Angebot  $1,350     test       kombi                2003   
    
         gearbox  powerPS   model   odometer  monthOfRegistration fuelType  \
    0    manuell      158  andere  150,000km                    3      lpg   
    1  automatik      286     7er  150,000km                    6   benzin   
    2    manuell      102    golf   70,000km                    7   benzin   
    3  automatik       71  fortwo   70,000km                    6   benzin   
    4    manuell        0   focus  150,000km                    7   benzin   
    
            brand notRepairedDamage          dateCreated  nrOfPictures  \
    0     peugeot              nein  2016-03-26 00:00:00             0   
    1         bmw              nein  2016-04-04 00:00:00             0   
    2  volkswagen              nein  2016-03-26 00:00:00             0   
    3       smart              nein  2016-03-12 00:00:00             0   
    4        ford              nein  2016-04-01 00:00:00             0   
    
       postalCode             lastSeen  
    0       79588  2016-04-06 06:45:54  
    1       71034  2016-04-06 14:45:08  
    2       35394  2016-04-06 20:15:37  
    3       33729  2016-03-15 03:16:28  
    4       39218  2016-04-01 14:38:50  



```python
autos.describe(include = 'all')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>dateCrawled</th>
      <th>name</th>
      <th>seller</th>
      <th>offerType</th>
      <th>price</th>
      <th>abtest</th>
      <th>vehicleType</th>
      <th>yearOfRegistration</th>
      <th>gearbox</th>
      <th>powerPS</th>
      <th>model</th>
      <th>odometer</th>
      <th>monthOfRegistration</th>
      <th>fuelType</th>
      <th>brand</th>
      <th>notRepairedDamage</th>
      <th>dateCreated</th>
      <th>nrOfPictures</th>
      <th>postalCode</th>
      <th>lastSeen</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>50000</td>
      <td>50000</td>
      <td>50000</td>
      <td>50000</td>
      <td>50000</td>
      <td>50000</td>
      <td>44905</td>
      <td>50000.000000</td>
      <td>47320</td>
      <td>50000.000000</td>
      <td>47242</td>
      <td>50000</td>
      <td>50000.000000</td>
      <td>45518</td>
      <td>50000</td>
      <td>40171</td>
      <td>50000</td>
      <td>50000.0</td>
      <td>50000.000000</td>
      <td>50000</td>
    </tr>
    <tr>
      <th>unique</th>
      <td>48213</td>
      <td>38754</td>
      <td>2</td>
      <td>2</td>
      <td>2357</td>
      <td>2</td>
      <td>8</td>
      <td>NaN</td>
      <td>2</td>
      <td>NaN</td>
      <td>245</td>
      <td>13</td>
      <td>NaN</td>
      <td>7</td>
      <td>40</td>
      <td>2</td>
      <td>76</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>39481</td>
    </tr>
    <tr>
      <th>top</th>
      <td>2016-03-09 11:54:38</td>
      <td>Ford_Fiesta</td>
      <td>privat</td>
      <td>Angebot</td>
      <td>$0</td>
      <td>test</td>
      <td>limousine</td>
      <td>NaN</td>
      <td>manuell</td>
      <td>NaN</td>
      <td>golf</td>
      <td>150,000km</td>
      <td>NaN</td>
      <td>benzin</td>
      <td>volkswagen</td>
      <td>nein</td>
      <td>2016-04-03 00:00:00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2016-04-07 06:17:27</td>
    </tr>
    <tr>
      <th>freq</th>
      <td>3</td>
      <td>78</td>
      <td>49999</td>
      <td>49999</td>
      <td>1421</td>
      <td>25756</td>
      <td>12859</td>
      <td>NaN</td>
      <td>36993</td>
      <td>NaN</td>
      <td>4024</td>
      <td>32424</td>
      <td>NaN</td>
      <td>30107</td>
      <td>10687</td>
      <td>35232</td>
      <td>1946</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>8</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2005.073280</td>
      <td>NaN</td>
      <td>116.355920</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5.723360</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>50813.627300</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>std</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>105.712813</td>
      <td>NaN</td>
      <td>209.216627</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.711984</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>25779.747957</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>min</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1000.000000</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>1067.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1999.000000</td>
      <td>NaN</td>
      <td>70.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>30451.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2003.000000</td>
      <td>NaN</td>
      <td>105.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>49577.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2008.000000</td>
      <td>NaN</td>
      <td>150.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>71540.000000</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>max</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>9999.000000</td>
      <td>NaN</td>
      <td>17700.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>12.000000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>99998.000000</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



The columns number of pictures, postal code, monthOfRegistration, powerPS, yearOfRegistration,  only has one value (0). I will eventually drop that column from the data set. 

Price and odometer are listed as strings. I will change these to a float. 

Seller, offerType, abtest, gearbox, and notRepairedDamage only have two unique values. 

Our dataset has 50,000 entries and 20 columns. Some columns have null values. Most columns are made up of strings. The column names use camelcase instead of snakecase. 

### Cleaning pt 1: Converting from strings to numeric

As mentioned before, both price and odometer columns are strings, but they should be numeric. For both of these columns, I will remove any non-numeric characters and convert the column to a numeric type. I will also rename the odometer column showing the proper units. 


```python
autos["price"].head()
```




    0    $5,000
    1    $8,500
    2    $8,990
    3    $4,350
    4    $1,350
    Name: price, dtype: object



For the price column, I will remove the comma and the dollar sign. 


```python
autos["price"] = autos["price"].str.replace("$", "").str.replace(",", "").astype(float)

autos["price"].head()
```




    0    5000.0
    1    8500.0
    2    8990.0
    3    4350.0
    4    1350.0
    Name: price, dtype: float64



Let's do the same with the odometer column. 


```python
autos["odometer"].head()
```




    0    150,000km
    1    150,000km
    2     70,000km
    3     70,000km
    4    150,000km
    Name: odometer, dtype: object




```python
autos["odometer"] = autos["odometer"].str.replace("km", "").str.replace(",", "").astype(float)

autos.rename({"odometer": "odometer_km"}, axis =1 , inplace = True)

autos["odometer_km"].head()
```




    0    150000.0
    1    150000.0
    2     70000.0
    3     70000.0
    4    150000.0
    Name: odometer_km, dtype: float64



I will now look at the odometer_km column in more detail, trying to find outliers. 


```python
print(autos["odometer_km"].unique().shape)
print('\n')
print(autos["odometer_km"].describe())
print('\n')
print(autos["odometer_km"].value_counts().sort_index(ascending = True))
```

    (13,)
    
    
    count     50000.000000
    mean     125732.700000
    std       40042.211706
    min        5000.000000
    25%      125000.000000
    50%      150000.000000
    75%      150000.000000
    max      150000.000000
    Name: odometer_km, dtype: float64
    
    
    5000.0        967
    10000.0       264
    20000.0       784
    30000.0       789
    40000.0       819
    50000.0      1027
    60000.0      1164
    70000.0      1230
    80000.0      1436
    90000.0      1757
    100000.0     2169
    125000.0     5170
    150000.0    32424
    Name: odometer_km, dtype: int64


Everything looks reasonable for this column. 

I will now do the same thing for the price column


```python
print(autos["price"].unique().shape)
print('\n')
# percentile list 
perc =[0.05, .10, .25, 0.50, .75, .90, 0.95]
print(autos["price"].describe(percentiles = perc))
print('\n')
print(autos["price"].value_counts().sort_index(ascending = True).head(15))
print('\n')
print(autos["price"].value_counts().sort_index(ascending = False).head(15))
```

    (1615,)
    
    
    count    45207.000000
    mean      4578.824076
    std       4443.771737
    min        200.000000
    5%         450.000000
    10%        630.000000
    25%       1249.000000
    50%       2900.000000
    75%       6500.000000
    90%      11500.000000
    95%      14600.000000
    max      19900.000000
    Name: price, dtype: float64
    
    
    200.0    266
    205.0      1
    210.0      1
    215.0      2
    217.0      1
    219.0      1
    220.0     33
    222.0     12
    225.0      8
    230.0     12
    235.0      2
    238.0      1
    240.0      3
    248.0      1
    249.0     13
    Name: price, dtype: int64
    
    
    19900.0    50
    19890.0     2
    19850.0     4
    19800.0    20
    19780.0     1
    19777.0     1
    19750.0     3
    19700.0     4
    19699.0     1
    19690.0     1
    19666.0     1
    19650.0     3
    19600.0     6
    19599.0     1
    19550.0     1
    Name: price, dtype: int64


Now we see some oddities. We have 1421 instances where the car is listed as being sold for free. We also have 1 instance where the car was sold for 99 million. This seems odd. 

The median price is 2950. I am going to remove rows with the following conditions: if the price is less than 200 (5th percentile), or is the price is greater than 19,900 (95th percentile). 


```python
autos = autos[autos["price"].between(200, 19900)]
print('\n')
print(autos["price"].unique().shape)
print('\n')
# percentile list 
perc =[0.05, .10, .25, 0.50, .75, .90, 0.95]
print(autos["price"].describe(percentiles = perc))
print('\n')
print(autos["price"].value_counts().sort_index(ascending = True).head(5))
print('\n')
print(autos["price"].value_counts().sort_index(ascending = False).head(5))
```

    
    
    (1615,)
    
    
    count    45207.000000
    mean      4578.824076
    std       4443.771737
    min        200.000000
    5%         450.000000
    10%        630.000000
    25%       1249.000000
    50%       2900.000000
    75%       6500.000000
    90%      11500.000000
    95%      14600.000000
    max      19900.000000
    Name: price, dtype: float64
    
    
    200.0    266
    205.0      1
    210.0      1
    215.0      2
    217.0      1
    Name: price, dtype: int64
    
    
    19900.0    50
    19890.0     2
    19850.0     4
    19800.0    20
    19780.0     1
    Name: price, dtype: int64


Our median price is now 2900. We now have 45207 rows in our dataframe. 

I will now look at the registration year column and try to find outliers. 


```python
print(autos["yearOfRegistration"].unique().shape)
print('\n')
print(autos["yearOfRegistration"].describe())
print('\n')
print(autos["yearOfRegistration"].value_counts().sort_index(ascending = True).head(5))
print('\n')
print(autos["yearOfRegistration"].value_counts().sort_index(ascending = False).head(5))
```

    (87,)
    
    
    count    45207.000000
    mean      2004.322848
    std         82.234293
    min       1000.000000
    25%       1999.000000
    50%       2003.000000
    75%       2008.000000
    max       9999.000000
    Name: yearOfRegistration, dtype: float64
    
    
    1000    1
    1001    1
    1111    1
    1800    2
    1910    2
    Name: yearOfRegistration, dtype: int64
    
    
    9999    3
    8888    1
    5911    1
    5000    3
    4800    1
    Name: yearOfRegistration, dtype: int64


This looks odd. I don't believe that cars were invented in 1001. I will remove all rows outside of these bounds: prior to 1900 and after 2020. 


```python
autos = autos[autos["yearOfRegistration"].between(1900, 2020)]
```


```python
print(autos["yearOfRegistration"].unique().shape)
print('\n')
print(autos["yearOfRegistration"].describe())
print('\n')
print(autos["yearOfRegistration"].value_counts().sort_index(ascending = True).head(5))
print('\n')
print(autos["yearOfRegistration"].value_counts().sort_index(ascending = False).head(5))
print('\n')
print(autos["yearOfRegistration"].value_counts(normalize=True))
```

    (75,)
    
    
    count    45190.000000
    mean      2003.246625
    std          7.245480
    min       1910.000000
    25%       1999.000000
    50%       2003.000000
    75%       2008.000000
    max       2019.000000
    Name: yearOfRegistration, dtype: float64
    
    
    1910    2
    1927    1
    1929    1
    1934    2
    1937    3
    Name: yearOfRegistration, dtype: int64
    
    
    2019       1
    2018     460
    2017    1362
    2016    1129
    2015     138
    Name: yearOfRegistration, dtype: int64
    
    
    2000    0.066630
    2005    0.063687
    1999    0.062802
    2003    0.059261
    2004    0.059040
    2006    0.058066
    2001    0.057513
    2002    0.054393
    1998    0.050365
    2007    0.048595
    2008    0.046316
    2009    0.042886
    1997    0.040850
    2010    0.030228
    2017    0.030139
    2011    0.028922
    1996    0.028657
    2016    0.024983
    1995    0.024607
    2012    0.021531
    1994    0.012945
    2013    0.011197
    2018    0.010179
    1993    0.008852
    1992    0.007634
    1991    0.007148
    2014    0.007125
    1990    0.006948
    1989    0.003696
    2015    0.003054
              ...   
    1977    0.000443
    1973    0.000443
    1960    0.000398
    1976    0.000398
    1968    0.000376
    1975    0.000376
    1974    0.000376
    1966    0.000354
    1969    0.000332
    1965    0.000288
    1964    0.000243
    1963    0.000111
    1961    0.000111
    1959    0.000111
    1956    0.000089
    1962    0.000089
    1937    0.000066
    1958    0.000066
    1910    0.000044
    1954    0.000044
    1934    0.000044
    1927    0.000022
    2019    0.000022
    1938    0.000022
    1941    0.000022
    1929    0.000022
    1953    0.000022
    1948    0.000022
    1950    0.000022
    1952    0.000022
    Name: yearOfRegistration, Length: 75, dtype: float64


This looks better. It looks like a majority of our cars were registered between 1997-2010. 

#### Using Aggregation on The Brand Column

 I will now explore the brand column


```python
print(autos["brand"].unique().shape)
print('\n')
print(autos["brand"].describe())
print('\n')
print(autos["brand"].value_counts())
```

    (40,)
    
    
    count          45190
    unique            40
    top       volkswagen
    freq            9754
    Name: brand, dtype: object
    
    
    volkswagen        9754
    opel              5059
    bmw               4784
    mercedes_benz     4126
    audi              3643
    ford              3197
    renault           2247
    peugeot           1405
    fiat              1211
    seat               881
    skoda              746
    nissan             712
    mazda              709
    smart              690
    citroen            670
    toyota             602
    hyundai            471
    volvo              423
    mini               385
    mitsubishi         381
    honda              381
    sonstige_autos     375
    kia                329
    alfa_romeo         313
    suzuki             274
    chevrolet          255
    chrysler           167
    dacia              129
    daihatsu           119
    subaru              96
    jeep                90
    porsche             86
    saab                78
    daewoo              74
    land_rover          68
    rover               63
    trabant             61
    jaguar              56
    lancia              51
    lada                29
    Name: brand, dtype: int64


It looks like we have 40 brands. I will aggregate by the top 6 brands. 


```python
pop_brands = autos["brand"].value_counts()
print(pop_brands[2])
print(pop_brands.index)
print(pop_brands.index[2])
type(pop_brands)

brand_agg = {}
brand_mil = {}

for i in range (0,6):
    brand_bool = autos["brand"] == pop_brands.index[i]
    brand_df = autos[brand_bool]
    mean_price = round(brand_df["price"].mean())
    mean_mileage = round(brand_df["odometer_km"].mean())
    
    brand_agg[pop_brands.index[i]] = mean_price
    brand_mil[pop_brands.index[i]] = mean_mileage
    
brand_agg
```

    4784
    Index(['volkswagen', 'opel', 'bmw', 'mercedes_benz', 'audi', 'ford', 'renault',
           'peugeot', 'fiat', 'seat', 'skoda', 'nissan', 'mazda', 'smart',
           'citroen', 'toyota', 'hyundai', 'volvo', 'mini', 'mitsubishi', 'honda',
           'sonstige_autos', 'kia', 'alfa_romeo', 'suzuki', 'chevrolet',
           'chrysler', 'dacia', 'daihatsu', 'subaru', 'jeep', 'porsche', 'saab',
           'daewoo', 'land_rover', 'rover', 'trabant', 'jaguar', 'lancia', 'lada'],
          dtype='object')
    bmw





    {'audi': 6448.0,
     'bmw': 6318.0,
     'ford': 3328.0,
     'mercedes_benz': 5975.0,
     'opel': 2890.0,
     'volkswagen': 4608.0}



The dictionary above shows the most popular brands and the mean price of each. It looks like Audi, BMW, and Mercedes are the most expensive.

For these top 6 brands, I will also aggregate to understand the average mileage to see if there is any visible link between mileage and price. 


```python
brand_mil
```




    {'audi': 137643.0,
     'bmw': 137591.0,
     'ford': 125752.0,
     'mercedes_benz': 136918.0,
     'opel': 130025.0,
     'volkswagen': 131760.0}



I will now convert both dictionaries into series objects, and then put them into a dataframe. 


```python
price_series = pd.Series(brand_agg)
print(price_series)
print('\n')
mileage_series = pd.Series(brand_mil)
print(mileage_series)
print('\n')
df = pd.DataFrame(price_series, columns=['mean_price'])
df['mean_mileage'] = mileage_series
df

```

    audi             6448.0
    bmw              6318.0
    ford             3328.0
    mercedes_benz    5975.0
    opel             2890.0
    volkswagen       4608.0
    dtype: float64
    
    
    audi             137643.0
    bmw              137591.0
    ford             125752.0
    mercedes_benz    136918.0
    opel             130025.0
    volkswagen       131760.0
    dtype: float64
    
    





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mean_price</th>
      <th>mean_mileage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>audi</th>
      <td>6448.0</td>
      <td>137643.0</td>
    </tr>
    <tr>
      <th>bmw</th>
      <td>6318.0</td>
      <td>137591.0</td>
    </tr>
    <tr>
      <th>ford</th>
      <td>3328.0</td>
      <td>125752.0</td>
    </tr>
    <tr>
      <th>mercedes_benz</th>
      <td>5975.0</td>
      <td>136918.0</td>
    </tr>
    <tr>
      <th>opel</th>
      <td>2890.0</td>
      <td>130025.0</td>
    </tr>
    <tr>
      <th>volkswagen</th>
      <td>4608.0</td>
      <td>131760.0</td>
    </tr>
  </tbody>
</table>
</div>



From the eyeball test, there doesn't seem to be much of an association between mileage and price. 
