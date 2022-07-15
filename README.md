# nyc-taxi-data

## Einleitung
- ### Ziel
  - Das Projekt wurde innerhalb des Moduls "Künstlich Intelligenz" an der IBS IT & Business School durchgeführt. Ziel der Arbeit ist dabei die Beantwortung von Fragestellungen durch Anwendung von erlernten theoretischen Konzepten. Eine Verknüpfung und daraus entstehende Synergie ergibt sich durch die Anwendung in der Praxis. In diesem spezifischen Fall die NYC Taxi Daten. 
  - #### Fragestellung
    - Fragestellung 1: Prognostizieren von der Dauer einer Fahrt: Wie lange dauert wahrscheinlich eine Fahrt, wenn ich in einer bestimmten Zone zu einer bestimmten Zeit einsteige?
    - Fragestellung 2: Prognostizieren von Fahrtkosten: Wie teuer ist eine Fahrt, wenn ich in einer bestimmten Zone zu einer bestimmten Zeit einsteige?


- ### Datenquelle:
  - Die Datenquelle ist die offizielle Seite der NYC Taxi & Limousine Commission. Seit 2009 bis 2022 werden die Daten gepflegt. Sie kann  [hier](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page) abgerufen werden. Die Daten sind Parquet Dateien.

- ### Datenqualität
  - Die Datenqualität muss überprüft werden. Aussagen zur Qualität einer Information beziehen sich zum Beispiel darauf, wie genau diese die Realität ‚beschreibt‘ oder wie verlässlich sie ist, inwieweit sie also als Grundlage für eine Planung des eigenen Handelns verwendbar ist. 

- ### Datenanalyse
  - Vor der Aufbereitung wurde von uns ganz gezielt erst eine Analyse durchlaufen. Dabei mussten Einflussfaktoren die extern sind mit in Betracht gezogen werden. Darunter zum Beispiel auch Corona. Auch das Wetter wäre ein möglicher externer Einflussfaktor. 

- ### Datenaufbereitung
  - Anhand der Datenqualität müssen im Vorfeld Kriterien zur Bewertung definiert werden. Nachfolgend muss das Ergebnis für die Analyse verwendet werden.

- ### Datenvisualisierung
  - Es wurde zur Visualisierung folium verwendet. Dieses Framework ist ein Python Package, das die Darstellung von Daten in Karten und Karteikarten ermöglicht. folium baut auf den Stärken des Python-Ökosystems bei der Datenverarbeitung und den Stärken der Leaflet.js-Bibliothek beim Mapping auf. Manipulationen der Daten in Python und visualisieren auf einer Leaflet-Karte mit Folium ist somit möglich.


## Projekt Struktur
- ### [Scatter](notebooks/scatter.ipynb)
  - Analyse durch Verwendung von Boxplots, Grafiken und Scatterplots.
- ### [Machine Learning](notebooks/ml_all_duration.ipynb): 
  - Prognosemodelle für Bestimmung von der Dauer und Preis einer Fahrt.
- ### [Map](notebooks/plswork.ipynb)
  - Analyse auf einer Karte.
