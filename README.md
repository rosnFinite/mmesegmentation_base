# MMSegmentation: Installation und Ausführung (Windows)

In dieser Anleitung wird erklärt, wie du MMSegmentation installieren kannst, und wie du die erfolgreiche Installation überprüfst, indem du ein Beispielskript ausführst.

---

## Voraussetzungen

Die Anleitung setzt voraus, dass du **Anaconda** oder eine seiner Varianten bereits auf deinem System installiert hast. Falls nicht, kannst du eine der folgenden Optionen installieren:

- **[Miniconda](https://docs.anaconda.com/miniconda/)**: Eine minimalistische Version von Anaconda, die nur die wichtigsten Befehle über die Kommandozeile (CLI) enthält.
- **[Miniforge](https://github.com/conda-forge/miniforge?tab=readme-ov-file)**: Eine vorkonfigurierte Variante, die den `conda-forge` Kanal und `mamba` (einen schnelleren Paketmanager) enthält.

---

# Installation der Conda-Umgebung

Die folgenden Schritte sind angelehnt an die [Get Started Dokumentation von MMsegmentation](https://mmsegmentation.readthedocs.io/en/main/get_started.html), wobei problematische Versionsunterschiede einzelner Pakete behoben sind.

### 1. Erstellen einer Conda-Umgebung

Erstelle zuerst eine neue Conda-Umgebung mit Python 3.8:

```bash
conda create --name mmseg python=3.8 -y
```

Dieser Befehl erstellt eine Umgebung namens `mmseg` und installiert Python 3.8. Das `-y` bestätigt automatisch alle Rückfragen während der Installation.

### 2. Aktivieren der Conda-Umgebung

Aktiviere die Umgebung, damit alle weiteren Installationen innerhalb dieser Umgebung stattfinden:

```bash
conda activate mmseg
```

### 3. Installation von PyTorch

Je nach System kannst du entweder die GPU- oder die CPU-Variante von PyTorch installieren:

**Für Systeme mit GPU:**
- Pytorch 2.1.2
- Cuda 12.1

```bash
conda install pytorch==2.1.2 torchvision==0.16.2 pytorch-cuda=12.1 fsspec -c pytorch -c nvidia -c conda-forge -y
```

**Für Systeme ohne GPU (nur CPU):**

```bash
conda install pytorch torchvision cpuonly -c pytorch -y
```

### 4. Installation notwendiger OpenMMLab-Pakete

Installation von MIM, des eigenen Paketmanagers von OpenMMLab (ermöglicht das einfache installieren von Modellen):

```bash
pip install -U openmim
```

```bash
mim install mmengine
```

**Für Systeme mit GPU:**

Neuere Versionen von mmcv (bspw. 2.2.0) werden zum aktuellen Zeitpunkt ohne zusätzlicher manueller Anpassung von MMEngine nicht unterstützt. Siehe zugehöriges [GitHub-Issue](https://github.com/open-mmlab/mmcv/issues/3096).
Demnach wird auf Version 2.1.0 zurückgegriffen und durch Angabe der URL (-f) festgelegt welche prebuild Version installiert werden soll.
```bash
pip install mmcv==2.1.0 -f https://download.openmmlab.com/mmcv/dist/cu121/torch2.1/index.html
```
**Für Systeme ohne GPU (nur CPU):**
```bash
pip install mmcv==2.1.0
```

### 5. Installation von MMSegmentation
Neben MMSegmentation muss hier das Modul `ftfy` installiert werden, da es nicht in den Abhängigkeiten von MMSegmentation enthalten und somit nicht automatisch installiert wird.
```bash
pip install "mmsegmentation>=1.0.0" ftfy
```

---

## Verifizierung der Installation

Du kannst die Installation überprüfen, indem du ein Beispielskript ausführst.

Vergewissere dich, dass du dich innerhalb des Projektordners befindest und lade im ersten Schritt die Konfigurations- und Checkpointdatei des PSPNet-Modell ([PSPNet](https://arxiv.org/abs/1612.01105)) herunter (werden unter `./model` gespeichert).

```bash
mim download mmsegmentation --config pspnet_r50-d8_4xb2-40k_cityscapes-512x1024 --dest ./model
```

Führe das Skript `installation_verification.py` aus, um das Bild `demo/inputs/demo.png` zu segmentieren. Das Ergebnis wird im Ordner `demo/results` gespeichert:

```bash
python installation_verification.py
```

Wenn alles korrekt eingerichtet ist, solltest du das segmentierte Bild im Ordner `demo/results` finden.

---

## Fehlerbehebung

### Failed to build `mmcv`
Falls dieser Fehler auftritt, wurde `mmcv` als Quellpaket (.tar.gz) heruntergeladen, welche daraufhin manuell in das eigentliche `mmcv`-Paket gebaut werden müssten.

```bash
> Failed to build mmcv
> ERROR: Could not build wheels for mmcv, which is required to install
> pyproject.toml-based projects
```
Um diesen Fehler zu beheben, geben wir bei der Installation von `mmcv` ein Webverzeichnis an, aus dem die passende prebuild Version geladen werden soll: 
1. Vergewissere dich, dass du CUDA 12.1 und pytorch 2.1 installiert hat.
2. Überprüfe, ob `mmcv` bereits in der Umgebung hinterlegt ist. Führe dazu `conda env list` aus und schau ob `mmcv` in der Liste der installierten Pakete auftaucht und deinstalliere es in dem Fall mit `pip uninstall mmcv`
3. Installiere `mmcv` von einem manuell hinterlegten Webverzeichnis `pip install mmcv==2.1.0 -f https://download.openmmlab.com/mmcv/dist/cu121/torch2.1/index.html`. Dies garantiert, dass die korrekte prebuild Version (.whl) installiert wird.

### ERROR: pip's dependency resolver does not currently take into account all the packages that are installed
In den meisten Fällen kann dieser Fehler ignoriert werden. Er tritt auf, weil sowohl Pip als auch Conda als Paketmanager verwendet werden. Jeder dieser Paketmanager kann jedoch nur die Versionen der Pakete überwachen, die er selbst installiert hat. Daher kommt es gelegentlich zu Fehlermeldungen, wenn der jeweilige Paketmanager auf Pakete stößt, die vom anderen installiert wurden oder diese nicht finden kann, obwohl sie vorhanden sind.
