# sot-app

# Sea of Thieves App

Sea of Thieves App to aplikacja webowa oparta na frameworku Django, która umożliwia graczom Sea of Thieves założenie konta, zaimportowanie swoich statystyk z gry oraz utworzenie lobby bądź znalezienie innych graczy do rozgrywki. Projekt nie jest juz rozwiajny z racji wieku i przeskoku technologicznego.

## Funkcje

- **Rejestracja i Logowanie:** Gracze mogą założyć konto, logować się i zarządzać swoim profilem.
  
- **Importowanie Statystyk:** Możliwość importowania statystyk, takich jak ilość zdobytych skarbów, z gry Sea of Thieves.

- **Tworzenie Lobby:** Gracze mogą tworzyć własne lobby, ustalając preferencje dla rozgrywki.

- **Znajdowanie Graczy:** Możliwość przeglądania dostępnych lobby i dołączania do gry z innymi graczami.

## Instalacja

1. Sklonuj repozytorium:

    ```bash
    git clone https://github.com/twoje-konto/sot-app.git
    cd sot-app
    ```

2. Zainstaluj zależności:

    ```bash
    pip install -r requirements.txt
    ```

3. Wykonaj migracje:

    ```bash
    python manage.py migrate
    ```

4. Uruchom serwer deweloperski:

    ```bash
    python manage.py runserver
    ```

Aplikacja będzie dostępna pod adresem `http://localhost:8000/`.

## Kontrybucje

Jesteśmy otwarci na kontrybucje! Jeśli masz pomysły na nowe funkcje, poprawki błędów lub inne ulepszenia, śmiało twórz zgłoszenia `issue` lub przesyłaj `pull request`.

## Autorzy

- Imię Nazwisko Artur Kunicki


Dziękujemy za korzystanie z Sea of Thieves App! Życzymy przyjemnych rozgrywek!
