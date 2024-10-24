# MMSegmentation: Installation und Ausführung (Windows)

In dieser Anleitung wird erklärt, wie du MMSegmentation installieren kannst, und wie du die erfolgreiche Installation überprüfst, indem du ein Beispielskript ausführst. Es gibt zwei Möglichkeiten, die Umgebung einzurichten: **automatisch** über eine vorbereitete `requirements.txt`-Datei oder **manuell**, indem du jeden Schritt selbst ausführst. Beide Optionen sind im Folgenden detailliert beschrieben.

---

## Voraussetzungen

Diese Anleitung setzt voraus, dass du **Anaconda** oder eine seiner Varianten bereits auf deinem System installiert hast. Falls nicht, kannst du eine der folgenden Optionen installieren:

- **[Miniconda](https://docs.anaconda.com/miniconda/)**: Eine minimalistische Version von Anaconda, die nur die wichtigsten Befehle über die Kommandozeile (CLI) enthält.
- **[Miniforge](https://github.com/conda-forge/miniforge?tab=readme-ov-file)**: Eine vorkonfigurierte Variante, die den `conda-forge` Kanal und `mamba` (einen schnelleren Paketmanager) enthält.

---

# Installation der Conda-Umgebung

Es gibt zwei Methoden, um die Conda-Umgebung für MMSegmentation aufzusetzen:

1. **Automatisch**: Wenn du die Installation mit einem einzigen Befehl und der bereitgestellten `requirements.txt`-Datei durchführen möchtest, ist dies die schnellere und einfachere Option.
2. **Manuell**: Wenn du jeden Schritt einzeln ausführen möchtest, z.B. um besser zu verstehen, was installiert wird, folge der manuellen Methode.

---

## Automatisches Aufsetzen der Conda-Umgebung [GPU]

Die Datei `requirements.txt` enthält bereits alle notwendigen Pakete und Versionen für die GPU-Variante von MMSegmentation. Falls du keine GPU zur Verfügung hast, folge der [manuellen Installationsanleitung](#manuelles-aufsetzen-der-conda-umgebung).
</br>
</br>
Um die Umgebung automatisch einzurichten, führe folgenden Befehl aus:

```bash
conda create --name mmsegmentation --file requirements.txt
```

Dieser Befehl erstellt eine Conda-Umgebung mit dem Namen `mmsegmentation` und installiert alle erforderlichen Pakete aus der `requirements.txt`-Datei.

Nach erfolgreicher Installation aktiviere die Umgebung:

```bash
conda activate mmsegmentation
```

Springe anschließend direkt zum Abschnitt [Verifizierung der Installation](#verifizierung-der-installation), um zu testen, ob alles korrekt eingerichtet wurde.

---

## Manuelles Aufsetzen der Conda-Umgebung

Falls du die Umgebung manuell einrichten möchtest, folge den nachstehenden Schritten.

### 1. Erstellen einer Conda-Umgebung

Erstelle zuerst eine neue Conda-Umgebung mit Python 3.8:

```bash
conda create --name mmsegmentation python=3.8 -y
```

Dieser Befehl erstellt eine Umgebung namens `mmsegmentation` und installiert Python 3.8. Das `-y` bestätigt automatisch alle Rückfragen während der Installation.

### 2. Aktivieren der Conda-Umgebung

Aktiviere die Umgebung, damit alle weiteren Installationen innerhalb dieser Umgebung stattfinden:

```bash
conda activate mmsegmentation
```

### 3. Installation von PyTorch

Je nach System kannst du entweder die GPU- oder die CPU-Variante von PyTorch installieren:

**Für Systeme mit GPU:**

```bash
conda install pytorch torchvision pytorch-cuda=12.4 -c pytorch -c nvidia
```

**Für Systeme ohne GPU (nur CPU):**

```bash
conda install pytorch torchvision cpuonly -c pytorch
```

### 4. Installation der OpenMMLab-Pakete

Installiere die benötigten Bibliotheken von OpenMMLab sowie zusätzliche Pakete:

```bash
pip install mmengine
pip install mmcv==2.1.0
pip install "mmsegmentation>=1.0.0"
pip install ftfy
```

---

## Verifizierung der Installation

Unabhängig davon, ob du die automatische oder die manuelle Methode gewählt hast, kannst du die Installation überprüfen, indem du ein Beispielskript ausführst.

Im Ordner `model` findest du die Konfigurations- und Checkpoint-Dateien für das PSPNet-Modell ([PSPNet](https://arxiv.org/abs/1612.01105)).

Führe das Skript `installation_verification.py` aus, um das Bild `demo/inputs/demo.png` zu segmentieren. Das Ergebnis wird im Ordner `demo/results` gespeichert:

```bash
python installation_verification.py
```

Wenn alles korrekt eingerichtet ist, solltest du das segmentierte Bild im Ordner `demo/results` finden.
