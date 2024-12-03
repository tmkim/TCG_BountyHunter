11/25/2024 ~ Project start

> Initialized Environment
> Set up PSQL DB connection
    - .pgpass, .pg_service.conf
> Set up admin superuser
> Set up initial views and urls
> Set up initial models

> tcgbh/urls.py ; bounty/urls.py ; tcgbh/settings.py ; bounty/models.py ; bounty/views.py

11/26/2024

> Added methods to Card and Bounty models
> Added more specific views (card detail (Card Model), card bounty (Bounty Model))
> Made tool for converting CSV into JSON for updating database
    -- currently just test data. Going to determine if better to just migrate CSVs later
    -- added some dummy test data

12/1/2024
> Spent time fleshing out design on paper

12/2/2024
> Implement Generic views DetailView and ListView
    >> Update bounty/views, bounty/urls
    -- currently : show list of cards, can click, will give you details
    -- TODO : replace list of cards with photos of cards
            : clean up DetailView to show info neatly
> Make changes to database tables
