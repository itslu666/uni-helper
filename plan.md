rec button
dragndrop feld für audio/vid
textfeld für zusammenfassung
feld für alle vorlesungen (ordner struktur):
- vorlesungen (ordner)
    - zusammenfassung
    - quiz
    - flashcards
    - transkript

button für flashcards und quiz
chatbot feld 
(json für memory von bot zusammenhang zur vorlesung)

datenstruktur zum speichern von vorlesungen
pattern für quiz und flashcard schreiben (immer nach einem schema)

lecture pattern umschreiben sodass mermaid charts

rec/dnd fenster drop down für ai aussuchen (fabric -L)

```mermaid
graph TD;
id1(User gibt API key ein)
id2(User drückt auf rec)
id3(User drückt auf import/Dropdown)
id4(Whisper transkribiert audio)
id5(transkribierter text nach fabric lecture pattern / wird in app mit flush geprintet)
id6(button zusammenfassen)
id7(button quiz)
id8(button flashcards)
id9(fabric lecture pattern)
id10(fabric quiz pattern)
id11(fabric flashcards pattern)
id12(zusammenfassung mit flush anzeigen)
id13(quiz mit flush anzeigen)
id14(flashcards UI anzeigen)
id15(UI wechselt zu library view)

id1-->id2-->id4
id1-->id3-->id4
id4-->id5
id5-->id6-->id9-->id12-->id15
id5-->id7-->id10-->id13-->id15
id5-->id8-->id11-->id14-->id15
```
