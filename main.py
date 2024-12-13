import os
import json

def py2json(directory, output_file):
    # Tworzymy pusty słownik na zawartość plików
    py_files_content = {}

    try:
        # Przeszukiwanie katalogów i podkatalogów
        for root, dirs, files in os.walk(directory):
            # Pomijanie ukrytych katalogów
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for filename in files:
                # Sprawdzamy, czy plik ma rozszerzenie .py
                if filename.endswith('.py'):
                    file_path = os.path.join(root, filename)
                    # Otwieramy i czytamy zawartość pliku
                    with open(file_path, 'r', encoding='utf-8') as file:
                        relative_path = os.path.relpath(file_path, directory)
                        py_files_content[relative_path] = file.read()

        # Zapisujemy słownik do pliku JSON
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(py_files_content, json_file, indent=4, ensure_ascii=False)

    except FileNotFoundError as e:
        print(f"Błąd: {e}")
    except PermissionError:
        print("Błąd: Brak uprawnień do odczytu/zapisu plików.")
    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Tworzenie pliku JSON z zawartością plików .py w katalogu i podkatalogach.")
    parser.add_argument("directory", help="Ścieżka do katalogu z plikami .py")
    parser.add_argument("output", help="Ścieżka do pliku wynikowego JSON")

    args = parser.parse_args()

    py2json(args.directory, args.output)
