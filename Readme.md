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

**Aufgabe 1: Sortieren (100 Punkte)**

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