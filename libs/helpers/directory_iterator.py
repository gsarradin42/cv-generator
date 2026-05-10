from pathlib import Path


class DirectoryIterator:
    def __init__(self, chemin):
        self.chemin = Path(chemin)
        self.elements = [item for item in self.chemin.iterdir() if item.is_dir()]
        self.index = 0

    def __iter__(self):
        return self

    def has_next(self):
        """Vérifie s'il reste des éléments à parcourir."""
        return self.index < len(self.elements)

    def __next__(self):
        """Retourne le prochain dossier dans le répertoire."""
        if self.has_next():
            dossier = self.elements[self.index]
            self.index += 1
            return dossier  # Retourne l'objet Path du dossier
        raise StopIteration  # Aucun élément à retourner
