# Vaatimusmäärittely 

 

## Sovelluksen tarkoitus 

 

Sovelluksen tarkoituksena on auttaa tekemään toimiva salamurhaajapeli. Salamurhaajapeli on seurapeli, jossa paperilla toteutettavassa versiossa kirjataan osallistujien nimet lappuihin, laput sekoitetaan, ja peliin osallistuville jaetaan sellainen lappu, jossa ei ole omaa nimeä siten, että kukaan ei tiedä kenenkään toisen lapussa olevaa nimeä. Siitä, jonka nimi pelaajan lapussa on, tulee pelaajan kohde, ja tämä tulee ”salamurhata” yhdessä sovittavalla merkillä, esimerkiksi piirtämällä sormella X salamurhattavan selkään. Salamurhausta taas ei kukaan muu saa nähdä. Salamurhattu antaa lappunsa hänen murhaajalleen, joka näin saa taas uuden kohteen. Peli loppuu, kun pelaaja saa oman nimensä sisältävän lapun, jolloin jäljellä on enää yksi pelaaja. 

 

Kun arvonta tehdään paperilapuilla, niin pelistä ei välttämättä tule optimaalinen, jos ei ole pelin ulkopuolista pelinjohtajaa. Itse arvontatilanne voi pitkittyä, jos joku saa oman lappunsa, sillä silloin arvonta on aloitettava alusta. Paras pelin lähtötilanne syntyy silloin, kun kaikki pelaajat ovat yhdessä suuressa ”murhaus-loopissa”, eikä seurue jakaannu moneen pienempään looppiin. Jälkimmäisessä tapauksessa useat pelaajat voivat lopulta saada oman lappunsa, vaikka pelissä on vielä useampi pelaaja jäljellä, ja kesken pelin joudutaan suorittamaan uusia arvontoja jäljellä olevien kesken. 

 

Tekemällä arvonta sovelluksella voidaan näiltä ongelmilta välttyä, ja voidaan saada paras mahdollinen pelin lähtötilanne. Sovelluksen yksinkertaisimmassa versiossa sovellus antaa kullekin pelaajalle esimerkiksi oman nimensä kirjoittamalla ensimmäisen kohteensa, joka otetaan talteen esimerkiksi lapulle. 

 

## Käyttäjät 

 

Yksinkertaisimmassa versiossa sovelluksella on ainoastaan yksi käyttäjärooli eli _pelaaja_, ja kaikki pelaajat käyttävät tätä samaa käyttäjää samalta tietokoneelta vuorotellen. Myöhemmin pelaajat voivat liittää nimeensä salasanan, jotta muut eivät voi huijata, ja katsoa toisen pelaajan kohdetta. Sovellukseen saatetaan lisätä suuremmilla oikeuksilla varustettu _pelinjohtaja_, joka voi esimerkiksi poistaa henkilön pelistä. 

 

## Käyttöliittymäluonnos 

 

 

KUVA 

 

## Perusversion tarjoama toiminnallisuus 

 

### Aloitusnäkymä 

 

- Pelaajien nimet kirjoitetaan yksitellen, ja aina välissä painetaan OK. 

  - Nimen tulee olla uniikki, siinä on oltava vain kirjaimia tai välilyöntejä, ja sen tulee olla pituudeltaan vähintään 2 kirjainta  

- Kun kaikki pelaajat on kirjattu, painetaan VALMIS-painiketta, jolloin pelaajille arvotaan kohteet. 

 

### Pelinäkymä 

 

- Pelaaja voi kirjoittaa oman nimensä ja nähdä kohteensa. Sovellus siirtyy kohdenäkymään 

- Uusi peli -painikkeella voidaan aloittaa uusi peli puhtaalta pöydältä, ja palataan aloitusnäkymään 

 

### Kohdenäkymä 

 

- Pelaaja näkee oman kohteensa 

- Takaisin-painike vie Pelinäkymään, jolloin toinen pelaaja voit ottaa selvittää oman kohteensa 

 

## Jatkokehitysideoita 

 

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla: 

 

- Pelaaja määrittelee aloitusnäkymässä itselleen salasanan, ja tämä on kirjoitettava pelinäkymässä nähdäkseen kohteensa 

- Murhaukset voidaan kirjata sovellukseen 

  - Peli pitää kirjaa murhista ja näyttää tilaston eri pelaajien suorittamista murhista 

  - Sovellus näyttää jäljellä olevien pelaajien lukumäärän, mikäli heitä on yli 3 

  - Sovelluksessa voi tarkastella nykyisen ja menneiden pelien kulkua 

- Ennen pelin alkua pelaajatietojen muokkaus 

- Uutena käyttäjäroolina laajemmilla oikeuksilla varustettu pelinjohtaja, joka voi muokata pelin kulkua esimerkiksi 

  - arpomalla uudet kohteet 

  - lisätä pelaajia 

   - poistaa pelaajia. 

 
