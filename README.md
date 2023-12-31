# Puistosovellus

## Kuvaus

Web-sovellus jonka avulla käyttäjät pääsevät tarkastelemaan kartalta
Helsingin eri puistoja, antamaan niille arvosteluita, kommentteja ja
seuraamaan kävijämääriä. 

Sovellus sisältää seuraavia ominaisuuksia:
- Käyttäjät kirjautuvat palveluun käyttäjätunnuksella ja salasanalla
- Käyttäjätyyppejä ovat pääkäyttäjät ja normaalit käyttäjät
- Normaalit käyttäjät voivat:
  - Nähdä puistot kartalla ja tarkastella niiden kuvauksia, arvosteluita ja kommentteja
  - Lisätä arvosteluita ja kommentteja
  - Lisätä merkinnän, että ovat puistossa, jolloin muut käyttäjät voivat nähdä kuinka monta henkilöä puistossa on
  - Poistaa merkinnän, kun ovat lähteneet puistosta
  - Hakea puistoja arvosteluiden ja luokituksen perusteella
- Pääkäyttäjät voivat:
  - Tehdä kaiken mitä normaalit käyttäjät
  - Lisätä puistoja ja niille kuvaukset
  - Poistaa käyttäjän kommentin ja arvion
  - Luokitella puistoja erilaisiin ryhmiin


## Sovelluksen nykyinen tilanne
- Käyttäjä pystyy etusivulta luomaan uuden käyttätunnuksen, joka tallennetaan tietokantaan
- Olemassa olevalla käyttäjätunnuksella pystyy kirjautumaan sisään
- Jos annettu käyttäjätunnus tai salasana ei täsmää tietokannassa oleviin tietoihin, niin sivu antaa virheen
- Jos sama käyttäjätunnus yritetään lisätä tietokantaan, niin sivu antaa virheen
- Sivu tunnistaa, jos käyttäjä on aiemmin jo kirjautunut sisään
- Tietokannassa on taulu users, johon tallennetaan tietoa uuden tunnuksen luomisen yhteydessä ja josta haetaan tietoa kirjautumisen yhteydessä
- Tietokannassa on myös taulut parks ja reviews, joihin tullaan seuraavaksi lisäämään toiminnallisuutta
- Seuraavaksi myös lisätään sisältöä parks.html ja muille sivuille, joiden kautta pääsee tarkastelemaan tietokannassa olevia puistoista ja arvosteluista sekä lisäämään arvosteluita

## Kuinka käyttää ja testata sovellusta komentoriviltä
**1)** Aluksi kopioi projekti koneellesi GitHubista


**2)** Luo Pythonin virtuaaliympäristö projektikansioon:

```bash
python3 -m venv venv
```

**3)** Ja käynnistä virtuaaliympäristö:

```bash
source venv/bin/activate
```

**4)** Ympäristön riippuvuudet löytyvät tiedostosta [requirements.txt](./requirements.txt). 
Nämä voit asentaa kerralla:

```bash
pip install -r requirements.txt
```

**5)** Koodi käyttää ympäristömuuttujia, jotka on tallennettu *.env* tiedostoon. GitHubiin tiedostoa ei ole kuitenkaan jaettu, mutta sieltä löytyy tiedosto [.env.example](./.env.example), josta voit nähdä mitä ympäristömuuttujia on käytetty. Voit nimetä tiedoston uudestaan *.env* ja päivittää rivin *DATABASE_URL=postgresql:///user*, niin että *user* on käyttäjätunuksesi/tietokannan nimi.

**6)** Käytössä on Postgres-tietokanta. Skeema löytyy tiedostosta [schema.sql](./schema.sql). Pääset luomaan taulut tietokantaan:

```bash
psql < schema.sql
```

**7)** Tämän jälkeen pääset käynnistämään ohjelman virtuaaliympäristöstä:

```bash
flask run
```
