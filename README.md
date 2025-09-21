# Kahvila-arvostelusivu

# Toiminnot
- Ideana se, että käyttäjät pystyvät arvostella kahviloita.
- Käyttäjät voivat luoda oman tunnuksen ja salasanan, sekä lisätä profiilikuvan.
- Käyttäjä voi lisätä kuvia arvosteluunsa.
- Käyttäjä voi muokata omaa julkaisuaan, lisätä sille tägejä (edullinen, pk-seutu, tunnelmallinen), ja poistaa sen.
- Käyttäjä voi kommentoida muiten julkaisuja ja etsiä niitä hakukentästä tägien avulla.
- Käyttäjä saa ilmoituksia liittyen julkaisuihinsa (tykkäykset, kommentit).
- Käyttäjäsivulla voi nähdä tilastoja käyttäjän aktiivisuudesta ja luotettavuudesta.

- Pääasiallinen tietokohde on arvostelu ja toissijainen tietokohde on kommentointi.


# Testausohje

Vamista, että sinulla on seuraavat asennukset:
- python
- pip
- sqlite3
- flask

Kloonaa repositorio:
git clone https://github.com/jade-ho/kahvila-arvostelu.git
cd kahvila-arvostelu

Aja seuraavat komennot:
python -m venv venv
source venv/bin/activate

Luo tietokanta database.db seuraavilla komennoilla:
sqlite3 database.db < schema.sql

Suorita lopuksi flask run ja siirry sen luomaan osoitteeseen.
