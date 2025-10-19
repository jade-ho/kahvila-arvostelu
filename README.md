# Kahvila-arvostelusivu

## Toiminnot
- Ideana se, että käyttäjät pystyvät arvostella kahviloita.
- Käyttäjät voivat luoda oman tunnuksen ja salasanan.
- Käyttäjä voi lisätä kuvia arvosteluunsa.
- Käyttäjä voi muokata omaa julkaisuaan, lisätä sille luokkia, kuten yleisarvosanan ja sijainnin, ja myös poistaa julkaisun.
- Käyttäjä voi kommentoida muiden julkaisuja ja etsiä niitä hakukentästä kuvauksen tai otsikon mukaan.
- Käyttäjä saa ilmoituksia liittyen julkaisuihinsa (tykkäykset, kommentit).
- Käyttäjäsivulla voi nähdä tilastoja käyttäjän aktiivisuudesta.
- Pääasiallinen tietokohde on arvostelu ja toissijainen tietokohde on kommentointi.


## Testausohje

Vamista, että sinulla on seuraavat asennukset:

```  
python
sqlite3
flask
```

Kloonaa repositorio:

```
git clone https://github.com/jade-ho/kahvila-arvostelu.git
```

Aja seuraavat komennot:

```
python -m venv venv
source venv/bin/activate
```

Luo tarvittavat tietokannat:
```
sqlite3 database.db < schema.sql
sqlite3 database.db < init.sql
```

Suorita lopuksi:
```
flask run
```

Mene osoitteeseen http://localhost:5000 .