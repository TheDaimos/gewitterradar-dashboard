<div align="center">

<img src="https://raw.githubusercontent.com/TheDaimos/gewitterradar-dashboard/main/dist/assets/gewitterradar-brand-icon.png" width="170" alt="Gewitterradar Logo">

# Gewitterradar — Dashboard

### Live-Blitz- und Gewitterdarstellung für Home Assistant

<img src="https://raw.githubusercontent.com/TheDaimos/gewitterradar-dashboard/main/dist/assets/gewitterradar-about-hero-v2.webp" width="920" alt="Gewitterradar · Gewitterlandschaft">

**Dashboard-/Lovelace-Auslieferung · HACS · V4.07-Package · weltweite Referenzorte · 120-Minuten-Verlauf**

![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Dashboard-41BDF5?logo=home-assistant&logoColor=white)
![HACS](https://img.shields.io/badge/HACS-Dashboard-41BDF5)
![Version](https://img.shields.io/badge/Gewitterradar-V4.09-c9a45b)
![Stable](https://img.shields.io/badge/Public%20Stable-V4.09-lightgrey)

</div>

---

> [!IMPORTANT]
> **Du bist im Repository der Dashboard-/Package-Variante von Gewitterradar.**  
> Wenn du genau diese Variante installieren möchtest, findest du hier den vollständigen Ablauf von HACS bis zur fertigen View.  
> Für neue Installationen gibt es zusätzlich die native Home-Assistant-Integration im Hauptrepository [`TheDaimos/gewitterradar`](https://github.com/TheDaimos/gewitterradar).

<table>
<tr>
<td width="50%" valign="top">

### 🗺️ Dashboard-Variante

- Installation über HACS als **Dashboard**
- JavaScript-Ressource aus HACS
- V4.07-YAML-Package
- bekannte `lightning_detection_*`-Helfer
- eigener Dashboard-Referenztracker
- vollständige Gewitterradar-Karte

</td>
<td width="50%" valign="top">

### ⚡ Datenquelle

Gewitterradar visualisiert Live-Blitze aus der Home-Assistant-Integration **Blitzortung.org**.

Gewitterradar ersetzt Blitzortung.org **nicht**. Die Blitzortung-Integration muss vorhanden und funktionsfähig sein.

</td>
</tr>
</table>

## Schnellnavigation

**[Installation](#installation--dashboard-variante)** · **[Package aktivieren](#2-v407-package-aktivieren)** · **[Ressource prüfen](#3-javascript-ressource-prüfen)** · **[View einrichten](#4-gewitterradar-view-einrichten)** · **[Blitzortung koppeln](#bezugsstandort-und-blitzortung)** · **[Recorder schützen](#recorder-schutz-empfohlen)** · **[Fehlersuche](#fehlersuche)**

> 🇬🇧 English installation guide: **[`docs/INSTALLATION_EN.md`](docs/INSTALLATION_EN.md)**

---

# Installation – Dashboard-Variante

## Voraussetzungen

- Home Assistant
- HACS
- Home-Assistant-Integration **Blitzortung.org** als Live-Datenquelle
- Zugriff auf `/config/`, da das V4.07-Package manuell nach `/config/packages/` kopiert wird

---

## 1. Repository in HACS hinzufügen

Öffne in Home Assistant:

**HACS → Benutzerdefinierte Repositories**

und füge dieses Repository hinzu:

```text
https://github.com/TheDaimos/gewitterradar-dashboard
```

Als Typ auswählen:

```text
Dashboard
```

Danach **Gewitterradar** installieren bzw. aktualisieren.

HACS legt die Dateien normalerweise hier ab:

```text
/config/www/community/gewitterradar-dashboard/
```

---

## 2. V4.07-Package aktivieren

> [!WARNING]
> Dieser Schritt ist bei der Dashboard-Variante erforderlich. HACS-Dashboard-Repositories können Konfigurationsdateien nicht automatisch nach `/config/packages/` installieren.

Kopiere:

```text
/config/www/community/gewitterradar-dashboard/app_gewitterradar_v4_07_pkg.yaml
```

nach:

```text
/config/packages/app_gewitterradar_v4_07_pkg.yaml
```

### Falls Home-Assistant-Packages noch nicht aktiviert sind

In `configuration.yaml` ergänzen:

```yaml
homeassistant:
  packages: !include_dir_named packages
```

> [!CAUTION]
> Falls bereits ein `homeassistant:`-Block existiert, den Eintrag dort ergänzen. **Keinen zweiten `homeassistant:`-Hauptschlüssel anlegen.**

Anschließend Home Assistant **vollständig neu starten**.

### Wichtig bei einem Wechsel von V4.06 auf V4.07

Für V4.07 wird verwendet:

```text
app_gewitterradar_v4_07_pkg.yaml
```

Das historische V4.06-Package bleibt nur als Rückfall-/Migrationsdatei erhalten.

> [!IMPORTANT]
> **V4.06 und V4.07 niemals gleichzeitig als aktive Packages laden.** Beide definieren dieselben `lightning_detection_*`-Helfer.

Kanonische V4.07-Package-Prüfsumme:

```text
SHA256: 1b705c5686e6a7be6dfb36717903df551d4f9f93787c39bd12bddf00aefae694
```

---

## 3. JavaScript-Ressource prüfen

Öffne:

**Einstellungen → Dashboards → Ressourcen**

und prüfe, dass folgende Ressource als **JavaScript-Modul** geladen wird:

```text
/hacsfiles/gewitterradar-dashboard/gewitterradar.js
```

<table>
<tr>
<td><strong>URL</strong></td>
<td><code>/hacsfiles/gewitterradar-dashboard/gewitterradar.js</code></td>
</tr>
<tr>
<td><strong>Typ</strong></td>
<td><code>JavaScript-Modul</code></td>
</tr>
</table>

> [!IMPORTANT]
> Es darf nur **eine** Gewitterradar-JavaScript-Ressource aktiv sein. Alte Testpfade oder `/hacsfiles/gewitterradar/gewitterradar.js` nicht parallel laden.

---

## 4. Gewitterradar-View einrichten

Der HACS-Download installiert Karte und Assets, erzeugt aber **keine Dashboard-View automatisch**.

### Vollständiger, empfohlener View-Inhalt

Diesen Block kannst du direkt für die Gewitterradar-View übernehmen:

```yaml
title: Gewitterradar
path: gewitterradar
icon: mdi:weather-lightning
type: panel
cards:
  - type: vertical-stack
    cards:
      - type: custom:gewitterradar-card
        counter_entity: sensor.home_lightning_counter
        radius_entity: input_number.lightning_detection_observation_radius
        compass_mode_entity: input_boolean.lightning_detection_compass_nearest_strike
```

> [!TIP]
> Dieser Block gehört zur **Dashboard-/Package-Variante**. Deshalb werden hier bewusst die `lightning_detection_*`-Helfer aus dem V4.07-Package verwendet.

### Wenn dein Dashboard mit `views:` beginnt

Im Rohkonfigurationseditor des gesamten Dashboards sieht derselbe Abschnitt so aus:

```yaml
views:
  - title: Gewitterradar
    path: gewitterradar
    icon: mdi:weather-lightning
    type: panel
    cards:
      - type: vertical-stack
        cards:
          - type: custom:gewitterradar-card
            counter_entity: sensor.home_lightning_counter
            radius_entity: input_number.lightning_detection_observation_radius
            compass_mode_entity: input_boolean.lightning_detection_compass_nearest_strike
```

### Über die Home-Assistant-Oberfläche

1. Gewünschtes Dashboard öffnen.
2. **Dashboard bearbeiten** wählen.
3. Neue Ansicht anlegen.
4. Titel: **Gewitterradar**
5. Pfad: **gewitterradar**
6. Symbol: `mdi:weather-lightning`
7. Ansichtstyp: **Panel / eine Karte**
8. Eine **Manuelle Karte** hinzufügen.
9. Für die Karte diesen Inhalt verwenden:

```yaml
type: vertical-stack
cards:
  - type: custom:gewitterradar-card
    counter_entity: sensor.home_lightning_counter
    radius_entity: input_number.lightning_detection_observation_radius
    compass_mode_entity: input_boolean.lightning_detection_compass_nearest_strike
```

### Falls dein Blitzortung-Zähler anders heißt

Wenn dein Counter nicht

```text
sensor.home_lightning_counter
```

heißt, ersetze ausschließlich `counter_entity` durch die tatsächliche Entity-ID deines Systems.

---

# Was nach der Installation vorhanden sein sollte

<table>
<tr>
<td width="35%"><strong>HACS-Repository</strong></td>
<td><code>TheDaimos/gewitterradar-dashboard</code> als Dashboard</td>
</tr>
<tr>
<td><strong>Frontend-Ressource</strong></td>
<td><code>/hacsfiles/gewitterradar-dashboard/gewitterradar.js</code></td>
</tr>
<tr>
<td><strong>Package</strong></td>
<td><code>/config/packages/app_gewitterradar_v4_07_pkg.yaml</code></td>
</tr>
<tr>
<td><strong>Kartentyp</strong></td>
<td><code>custom:gewitterradar-card</code></td>
</tr>
<tr>
<td><strong>Referenztracker</strong></td>
<td><code>device_tracker.gewitterradar_dashboard</code></td>
</tr>
<tr>
<td><strong>Helfer</strong></td>
<td><code>lightning_detection_*</code> aus dem V4.07-Package</td>
</tr>
</table>

---

# Bezugsstandort und Blitzortung

Das V4.07-Dashboard-Package stellt einen eigenen Referenztracker bereit:

```text
device_tracker.gewitterradar_dashboard
```

## Für einen festen Heimatstandort

Wenn Blitzortung.org bereits korrekt auf deinen gewünschten festen Standort eingestellt ist, musst du zunächst nichts ändern.

## Für weltweite bzw. wechselnde Standorte

Wenn Gewitterradar den Referenzort dynamisch verschieben soll:

1. In der **Blitzortung.org-Integration** `device_tracker.gewitterradar_dashboard` einmalig als **Location entity** auswählen.
2. Danach Standorte direkt in Gewitterradar auswählen oder Koordinaten übernehmen.
3. Das Package aktualisiert den Gewitterradar-Tracker.
4. Blitzortung.org bleibt für Datenregion, Neuabonnement und Aktualisierungslatenz verantwortlich.

> [!NOTE]
> Gewitterradar verändert keine fremden Config Entries und schreibt nicht direkt in Home-Assistant-`.storage`.

---

# Recorder-Schutz empfohlen

Blitzortung kann sehr viele kurzlebige Entitäten und Zustandsänderungen erzeugen. Um unnötiges Datenbank- und Backup-Wachstum zu vermeiden, wird empfohlen, diese Live-Daten vom Home-Assistant-Recorder auszunehmen.

In `configuration.yaml`:

```yaml
recorder:
  exclude:
    entity_globs:
      - "geo_location.lightning_strike*"
      - "sensor.*_lightning_distance"
      - "sensor.*_lightning_azimuth"
      - "sensor.*_lightning_counter"
```

> [!CAUTION]
> Falls bereits ein `recorder:`-Block vorhanden ist, die Einträge dort ergänzen. **Keinen zweiten `recorder:`-Hauptschlüssel anlegen.**

Die Live-Zustände bleiben für Gewitterradar verfügbar. Bereits gespeicherte historische Daten werden dadurch nicht automatisch entfernt.

Mehr dazu: **[`docs/RECORDER.md`](docs/RECORDER.md)**

---

# Fehlersuche

<details>
<summary><strong>„Custom element doesn't exist: gewitterradar-card“</strong></summary>

<br>

Prüfe unter **Einstellungen → Dashboards → Ressourcen**, ob exakt diese Ressource vorhanden ist:

```text
/hacsfiles/gewitterradar-dashboard/gewitterradar.js
```

Typ: **JavaScript-Modul**.

Danach Browser bzw. Home-Assistant-App vollständig neu laden. Bei Bedarf einen Hard-Reload durchführen.

</details>

<details>
<summary><strong>Die Karte erscheint, aber Einstellungen oder Radien fehlen</strong></summary>

<br>

Prüfe, ob das V4.07-Package tatsächlich unter

```text
/config/packages/app_gewitterradar_v4_07_pkg.yaml
```

liegt, ob Packages in `configuration.yaml` aktiviert sind und ob Home Assistant danach vollständig neu gestartet wurde.

Außerdem sicherstellen, dass nicht gleichzeitig das V4.06-Package aktiv ist.

</details>

<details>
<summary><strong>Die Karte zeigt keine Live-Blitze</strong></summary>

<br>

Prüfe zuerst die Blitzortung.org-Integration. Gewitterradar benötigt deren Live-Entitäten, insbesondere:

```text
geo_location.lightning_strike*
```

sowie den zugehörigen Lightning-Counter.

Falls dein Counter anders heißt, passe `counter_entity` in der View an.

</details>

<details>
<summary><strong>Nach einem Update sehe ich weiterhin eine alte Version</strong></summary>

<br>

Prüfe, dass nur **eine** Gewitterradar-JavaScript-Ressource aktiv ist und keine alten Test-/Repository-Pfade parallel geladen werden.

Danach Browsercache neu laden.

</details>

<details>
<summary><strong>V4.06 und V4.07 verhalten sich widersprüchlich</strong></summary>

<br>

Prüfe unter `/config/packages/`, ob versehentlich beide Package-Versionen aktiv sind. V4.06 und V4.07 dürfen nicht gleichzeitig geladen werden.

</details>

---

# Funktionen

<table>
<tr>
<td width="50%" valign="top">

### 🌩️ Gewitterdarstellung

- Live-Blitzpositionen
- Beobachtungs-, Gewitter- und Gefahrenradius
- Einzelblitze und dynamische Gruppierung
- 120-Minuten-Historie
- Aktivitäts- und Gefahrenanzeige

</td>
<td width="50%" valign="top">

### 🧭 Navigation und Analyse

- mehrere Kompassdesigns
- nächster bzw. letzter Blitz
- Trend-Medaillon
- weltweite Orts-/PLZ-Suche
- direkte Koordinateneingabe
- gespeicherte Orte

</td>
</tr>
<tr>
<td valign="top">

### 🌍 Oberfläche

- Desktop, Tablet und Mobilgeräte
- 15 Sprachen
- 4 deutsche Dialektvarianten
- integrierte Hilfe und Hinweise

</td>
<td valign="top">

### ⚙️ Dashboard-Package

- bekannte `lightning_detection_*`-Helfer
- V4.07-Referenztracker
- definierter V4.06-Rückfallpfad
- HACS-Dashboard-Auslieferung

</td>
</tr>
</table>

---

# Native Integration

<details>
<summary><strong>Native Home-Assistant-Integration anzeigen</strong></summary>

<br>

Für neue Installationen steht zusätzlich die native Gewitterradar-Integration zur Verfügung. Sie benötigt kein `lightning_detection_*`-YAML-Package und verwaltet ihre Einstellungen über native Home-Assistant-Entitäten.

Repository:

```text
https://github.com/TheDaimos/gewitterradar
```

HACS-Typ:

```text
Integration
```

Vollständige Anleitung:

**[`TheDaimos/gewitterradar`](https://github.com/TheDaimos/gewitterradar)**

</details>

---

# Bestehende Installationen und Migration

<details>
<summary><strong>Hinweise zu älteren Dashboard-Installationen</strong></summary>

<br>

Bei älteren Installationen besonders prüfen:

- altes Dashboard-Repository `TheDaimos/gewitterradar` nicht zusätzlich laden;
- für diese Auslieferung `TheDaimos/gewitterradar-dashboard` verwenden;
- keine parallelen alten Gewitterradar-JavaScript-Ressourcen;
- V4.06- und V4.07-Package nicht gleichzeitig aktiv.

Weitere Informationen: **[`docs/REPOSITORY_RENAME.md`](docs/REPOSITORY_RENAME.md)**

</details>

---

# Dokumentation

<table>
<tr>
<td><strong>Installation – Deutsch</strong></td>
<td><a href="docs/INSTALLATION_DE.md">docs/INSTALLATION_DE.md</a></td>
</tr>
<tr>
<td><strong>Installation – English</strong></td>
<td><a href="docs/INSTALLATION_EN.md">docs/INSTALLATION_EN.md</a></td>
</tr>
<tr>
<td><strong>Recorder</strong></td>
<td><a href="docs/RECORDER.md">docs/RECORDER.md</a></td>
</tr>
<tr>
<td><strong>Repository-Migration</strong></td>
<td><a href="docs/REPOSITORY_RENAME.md">docs/REPOSITORY_RENAME.md</a></td>
</tr>
<tr>
<td><strong>Release Notes</strong></td>
<td><a href="RELEASE_NOTES_V4_09.md">RELEASE_NOTES_V4_09.md</a></td>
</tr>
</table>

---

<details>
<summary><strong>Entwicklungs-, Prüf- und Release-Informationen</strong></summary>

<br>

Aktueller öffentlicher Dashboard-Stand: **V4.09**

Dieses Repository ist die abgeleitete Dashboard-/HACS-Auslieferung des kanonischen Gewitterradar-Projekts:

```text
TheDaimos/gewitterradar
```

Kanonischer V4.09-Commit: `a6a5b68ebc289f04217bc5abb55c46422dce4e4c`

V4.09-Payload-Identitäten:

```text
dist/gewitterradar.js
SHA256: c9f01617d3a19519ecc44f84a7bf71aa3056dee57245af860becd893c652fce2

dist/locales/about-locales.js
SHA256: dc6506291dd4cfe75e3b9c829fb42f21062511fb574d335af438e6c42711802e

dist/app_gewitterradar_v4_07_pkg.yaml
SHA256: 1b705c5686e6a7be6dfb36717903df551d4f9f93787c39bd12bddf00aefae694
```

V4.09 ist bytegleich aus dem exakt veröffentlichten kanonischen Gewitterradar-V4.09-Frontend abgeleitet. Das weiterhin verwendete V4.07-YAML-Package bleibt unverändert; frühere Tags und eingefrorene Release-Branches bleiben unverändert.

</details>

---

# Lizenz

Für dieses abgeleitete Dashboard-Repository wurde bislang keine separate Softwarelizenz ausgewählt. Bis eine Lizenz ergänzt wird, gelten die üblichen urheberrechtlichen Standardregeln für den Repository-Inhaber.
