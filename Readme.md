**INFO**
name.txt kann ein Output in einer txt datei gespeichert werden um das besser lesen zu können.
bsp. output.txt

**main**
Der Finale Branch, hier wird nur gemerget wenn alles funktioniert und getestet wurde. Dieser branch ist für die Abgabe gedacht.

**dev_branch**
Der dev_branch ist für vorabversionen gedacht, welche lauffähig sind und 'nur' noch eine genaueren Prüfung bedürfen um sie in *main* zu mergen.
Hier werden die Datensätze mit hochgeladen, welche für unsere Aufgabe verwendet werden sollen.

**test_branch**
Der test_branch ist für testversionen gedacht. Es können hier neue Datein angelegt werden oder sonstiges.

**test_code.py**
Die *test_code.py* ist eine Datei die zum testen benutzt wird. Sie ist nicht relevant für die Aufgabe und darf direkt gemerget werden OHNE kontrolle.
Es müsste nur jemand eben bescheid gegeben werden, der das ganze durchwinkt.

**Issue erstellen**
Geht auf [Git](https://github.com/) und erstellt ein Issue.
Klicke auf "Neues Issue erstellen", Fülle die Details des Issues aus: Gib dem Issue einen Titel und eine Beschreibung. Wenn du fertig bist, klicke auf "Submit new issue". Gebt dem ganzen noch ein Label (rechts zu finden) um das Problem leichter erkennbar zu machen.
Weißt einen Verantwortlichen zu (meist ihr selbst oder jemand, der euch helfen soll).

**Branch erstellen**
Klickt dann rechts noch auf *create branch* und gebt dem Branch einen Namen.
Es sollte sich ein neues Fenster öffnen **WICHTIG**: klickt auf **Change branch source** und wählt den dev_branch oder test_branch aus, je nachdem welchen Entwicklungsstand der Code hat.

**Branch mit GitDesktop pullen (lokal aktualisieren)**
Klicke auf den Dropdown-Pfeil neben dem aktuellen Branch-Namen, um eine Liste der verfügbaren Branches anzuzeigen. Wähle den Branch aus, den du aktualisieren möchtest.
Klicke auf den Button Fetch origin, um die Liste der verfügbaren Branches zu aktualisieren. Klicke auf den Button Pull origin, um den ausgewählten Branch zu aktualisieren.

**Branch mit GitDesktop pushen (online hochladen)**
Bevor du pushen kannst, ist es empfehlenswert, den Branch mit dem Remote-Repository zu synchronisieren, um sicherzustellen, dass die neuesten Änderungen vorhanden sind. Klickt dazu auf den Button "Fetch origin" in der oberen rechten Ecke des Fensters.
Klicke auf den Dropdown-Pfeil neben dem aktuellen Branch-Namen, um eine Liste der verfügbaren Branches anzuzeigen. Wähle den Branch aus, den du pushen möchtest. Das sollte im normalfall der sein, den ihr aus dem Issue erstellt habt. Schreibt ein Kommentar, um die Änderungen zu beschreiben, dass macht es den anderen leichter das ganze nachzuvollziehen.
Klickt auf den Button "Push origin", um den ausgewählten Branch zu pushen.

**Merge request erstellen**
Geht nach dem Push auf [Git](https://github.com/) und wählt das passende Rep.
Auf der Repository-Seite solltest du eine Option finden, um einen Merge Request (oder Pull Request) zu erstellen. Klicke darauf, um den Merge Request zu erstellen.
Am besten wählt ihr rechts oben noch einen Reviewer aus, der das ganze durchgeht und bestätigt.




**Aufgabe 1: Sortieren (100 Punkte)**\\
Implementieren Sie die beiden Sortierverfahren Mergesort und Quicksort fur das folgende ¨
Szenario:
In einer Tabelle ist eine (unsortierte) Liste von Namen (Vorname Nachname) gegeben. Vorname und Nachname sind jeweils Texte aus {a, ..., z}.
Sortieren Sie die Tabelle jeweils so, dass die Namen nach Nachnamen und bei gleichem
Nachnamen nach den Vornamen aufsteigend lexikographisch sortiert sind.
(vgl. https://de.wikipedia.org/wiki/Lexikographische Ordnung)
Die unsortierte Tabelle wird aus einer durch ein Programmargument anzugebenden Datei
gelesen. Jede Zeile der Datei enth¨alt einen Vornamen und einen Nachnamen, die durch ein
Leerzeichen getrennt sind. Am Ende kann die Eingabedatei eine leere Zeile enthalten, die
zu ignorieren ist. Die Ausgabe muss genauso formatiert sein wie die Eingabe, d.h. jede Zeile
besteht aus Vorname Nachname, die wieder durch ein Leerzeichen getrennt sind.
Beispiel:
axy aaa
xy a
x ab
yz z
xz z
Ergebnis:
xy a
axy aaa
x ab
xz z
yz z

**Aufgabe 2:**