#!/bin/bash

# Liste der Sprachcodes
languages=("de" "en" "fr" "it" "rm" "ru" "sr" "sq" "mk")

# Wechseln Sie in das Stammverzeichnis des Projekts
cd "$(dirname "$0")/.."

# Durchlaufe jede Sprache und führe makemessages aus
for lang in "${languages[@]}"; do
    python manage.py makemessages -l $lang
done
