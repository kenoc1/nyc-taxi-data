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
- ### [Data](data)
  - Unterteilt in 4 Kategorien:
  - external für externe Daten, wie geo.json oder hier wären auch Wetterdaten zu platzieren
  - interim für Daten, die während des Preprocessing generiert werden aber noch nicht vollständig preprocessed sind oder weitere Daten die zwischendurch benötigt werden
  - processed, hier sind die vorbereiteten Daten, die für die Modelle benötigt werden
  - raw, sind die Daten mit denen wir gestartet haben
- ### [Models](models):
  - Hier können Modelle zwischengespeichert werden für eine spätere Nutzung.
- ### [Notebooks](notebooks)
  - Eine Übersicht über die wesentlichen Arbeitsschritte, die wir in unserem Projekt gegangen sind
  - dabei gibt die Nummerierung Aufschluss über die Reihenfolge
  - Jedes Notebook behandelt einen Schritt im Prozess
  - Zunächst gibt es Data Preparation Notebook und ab Nummer 7 werden ML Modelle trainiert
- ### [references](references)
  - externe Dokumente zur Definition von bestimmten Werten
- ### [reports](reports)
  - hier werden reports abgespeichert, um zwischenstände zu visualisieren und wichtige Diagramme langfristig zu speichern
- ### [src](src)
  - Im src Ordner liegen noch Skripts, für die Datenbereinigung über alle Monate hinweg, damit nicht jeder Monat einzelnd berechnet werden muss
  - Die .py Files sind dafür da bestimmte Codeschnipsel häufig auszuführen