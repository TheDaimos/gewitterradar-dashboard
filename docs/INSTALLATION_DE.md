# Gewitterradar V4.07.57 – Installation (DE)

Diese Anleitung gilt für die **Dashboard-/Lovelace-Auslieferung** von Gewitterradar aus `TheDaimos/gewitterradar-dashboard`.

## Voraussetzungen

- laufende Home-Assistant-Installation;
- Blitzortung.org-Integration als Quelle der Live-Blitzdaten;
- HACS für die normale Installation;
- Zugriff auf `/config/`, da das Gewitterradar-Package manuell nach `/config/packages/` kopiert werden muss.

## 1. Gewitterradar über HACS installieren

1. `https://github.com/TheDaimos/gewitterradar-dashboard` in HACS als benutzerdefiniertes Repository vom Typ **Dashboard** hinzufügen.
2. **Gewitterradar** installieren bzw. aktualisieren.
3. Unter **Einstellungen → Dashboards → Ressourcen** prüfen, dass folgende Ressource als **JavaScript-Modul** geladen wird:

```text
/hacsfiles/gewitterradar-dashboard/gewitterradar.js
```

Die zugehörigen Dateien liegen normalerweise unter:

```text
/config/www/community/gewitterradar-dashboard/
```

## 2. V4.07-Package manuell aktivieren

HACS-Dashboard-Repositories können Konfigurationsdateien nicht direkt nach `/config/packages/` installieren. Dieser Schritt ist deshalb bewusst manuell.

Kopiere:

```text
/config/www/community/gewitterradar-dashboard/app_gewitterradar_v4_07_pkg.yaml
```

nach:

```text
/config/packages/app_gewitterradar_v4_07_pkg.yaml
```

Falls Packages noch nicht aktiviert sind, in `configuration.yaml` ergänzen:

```yaml
homeassistant:
  packages: !include_dir_named packages
```

Existiert bereits ein `homeassistant:`-Block, den Eintrag dort ergänzen. **Keinen zweiten `homeassistant:`-Hauptschlüssel anlegen.**

Anschließend Home Assistant vollständig neu starten.

### Wichtig bei Updates von V4.06

Für V4.07 wird ausschließlich verwendet:

```text
app_gewitterradar_v4_07_pkg.yaml
```

Das historische `app_gewitterradar_v4_06_pkg.yaml` bleibt nur als Rückfall-/Migrationsdatei erhalten.

**V4.06 und V4.07 niemals gleichzeitig als aktive Packages laden.** Beide definieren dieselben `lightning_detection_*`-Helfer.

Kanonische V4.07-Paket-Prüfsumme:

```text
SHA256: 1b705c5686e6a7be6dfb36717903df551d4f9f93787c39bd12bddf00aefae694
```

## 3. Gewitterradar-View anlegen

Der HACS-Download installiert die Karte und ihre Assets, erstellt aber **keine Dashboard-View automatisch**.

### Über die Home-Assistant-Oberfläche

1. Gewünschtes Dashboard öffnen.
2. **Dashboard bearbeiten** wählen.
3. Neue Ansicht **Gewitterradar** anlegen.
4. Ansichtstyp **Panel / eine Karte** verwenden.
5. Optional `mdi:weather-lightning` als Symbol setzen.
6. Eine **Manuelle Karte** hinzufügen.
7. Folgende Kartenkonfiguration eintragen:

```yaml
type: custom:gewitterradar-card
```

Das ist die vollständige Minimal-Konfiguration. Das V4.07-Package stellt die benötigten Gewitterradar-Helfer bereit.

### Vollständiges YAML-Beispiel

```yaml
views:
  - title: Gewitterradar
    path: gewitterradar
    icon: mdi:weather-lightning
    type: panel
    cards:
      - type: custom:gewitterradar-card
```

Falls der Blitzortung-Zähler nicht `sensor.home_lightning_counter` heißt, kann er optional explizit angegeben werden:

```yaml
type: custom:gewitterradar-card
counter_entity: sensor.DEIN_LIGHTNING_COUNTER
```

## 4. Weltweiten Bezugsstandort mit Blitzortung koppeln

Das V4.07-Package stellt einen eigenen Referenztracker bereit:

```text
device_tracker.gewitterradar_dashboard
```

Diesen Tracker einmalig in der Blitzortung.org-Integration als **Location entity** auswählen.

Danach erfolgen Standortwechsel in Gewitterradar. Das Package aktualisiert den Gewitterradar-Tracker; Blitzortung.org bleibt für Datenregion, Neuabonnement und Aktualisierungslatenz verantwortlich.

Gewitterradar verändert keine fremden Config Entries und schreibt nicht direkt in Home-Assistant-`.storage`.

## 5. Recorder-Schutz – dringend empfohlen

Gewitterradar verarbeitet kurzlebige Blitzentitäten. Bei hoher Aktivität können sehr viele Zustandsänderungen entstehen. Für die Home-Assistant-Datenbank wird deshalb folgender Ausschluss empfohlen:

```yaml
recorder:
  exclude:
    entity_globs:
      - "geo_location.lightning_strike*"
      - "sensor.*_lightning_distance"
      - "sensor.*_lightning_azimuth"
      - "sensor.*_lightning_counter"
```

Bestehende `recorder:`-Konfiguration ergänzen und **keinen zweiten `recorder:`-Hauptschlüssel** anlegen.

Die Live-Zustände bleiben für Gewitterradar verfügbar. Bereits vorhandene historische Daten werden dadurch nicht automatisch gelöscht.

Siehe auch [`RECORDER.md`](RECORDER.md).

## 6. Alte Ressourcen entfernen

Es darf nur eine Gewitterradar-JavaScript-Ressource aktiv sein:

```text
/hacsfiles/gewitterradar-dashboard/gewitterradar.js
```

Historische oder Test-Ressourcen wie

```text
/hacsfiles/gewitterradar/gewitterradar.js
```

nicht parallel laden.

Nach einer Ressourcenänderung den Browser vollständig neu laden; bei hartnäckigem Cache einen Hard-Reload ausführen.

## 7. Prüfung nach Installation

Nach der Installation prüfen:

- Gewitterradar zeigt **V4.07.57**;
- `/hacsfiles/gewitterradar-dashboard/gewitterradar.js` ist die einzige aktive Gewitterradar-Ressource;
- `assets/` und `locales/about-locales.js` sind im HACS-Ordner vorhanden;
- `/config/packages/app_gewitterradar_v4_07_pkg.yaml` ist aktiv;
- V4.06-Package ist nicht gleichzeitig geladen;
- Karte und Radien werden dargestellt;
- Live-Blitze bzw. die vorhandene 120-Minuten-Historie erscheinen;
- Kompass, Medaillon und Verlauf funktionieren;
- weltweite Ortssuche und Koordinateneingabe funktionieren;
- `device_tracker.gewitterradar_dashboard` ändert bei einem Standortwechsel seine Koordinaten;
- Blitzortung.org verwendet diesen Tracker als Location Entity;
- Hilfe-/Hinweisbereich einschließlich Recorder-Hinweis ist verfügbar.

## 8. Repository-Umbenennung / ältere Installationen

Bei älteren Installationen den veralteten Dashboard-Eintrag `TheDaimos/gewitterradar` nicht zusätzlich laden. Für die Dashboard-Auslieferung wird `TheDaimos/gewitterradar-dashboard` verwendet.

Vor dem Wechsel alte JavaScript-Ressourcen und das aktive V4.06-Package prüfen und sauber ersetzen.

Details: [`REPOSITORY_RENAME.md`](REPOSITORY_RENAME.md)
