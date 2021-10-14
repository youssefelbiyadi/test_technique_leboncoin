#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys


class Map:
    """
    Les objets de cette classe représentent le contenu des fichiers à analyser pour trouver le plus grand carré sur un
    plateau en évitant les obstacles.
    L'instanciation de ces objets se fait par les paramètres "card" et "characters".
    L'objectif est de renvoyer un plateau (str) sur lequel est déssiné le plus grand carré possible le plus à gauche.

    """

    def __init__(self, card: str, characters: str):
        """
        :param card: le plateau à analyser.
        :param characters: les caractères utilisés.
        """

        self.card = [list(s) for s in card.split()]
        if self.card:
            self.rows = len(self.card)
            self.columns = len(self.card[0])
        self.empty_char, _, self.fill_char = characters
        self.valid_characters = all(char in characters + "\n" for char in card)

    def card_is_valid(self) -> bool:
        """
        Permet de vérifier si un plateau est valide ou pas.
        :return: True si le plateau est valide, False sinon.
        """

        valid_lines = all(list(map(lambda line: len(line) == self.columns, self.card)))
        card_not_empty = bool(self.card)
        is_valid = valid_lines and card_not_empty and self.valid_characters
        return is_valid

    def find_largest_square(self) -> dict or str:
        """
        Trouve le plus grand carré.
        En commence par la position (i, j), puis on vérifie la présence d'un obstacle dans les cellules voisines i.e
        adjacentes (i+1, j), (i, j+1) et (i+1, j+1) toute en mémorisant l'état de ces cellules dans une matrice de mémo
        (memo card).
        :return: - un dictionnaire contenant la taille et les coordonnées du point le plus haut à gauche du plus grand
                 carré.
                 - un message d'erreur si le plateau est non valide.
        """

        if self.card_is_valid():
            square_x, square_y = 0, 0
            square_side = 0
            memo_card = [[0] * (self.columns + 1) for _ in range(self.rows + 1)]
            for r in range(self.rows):
                for c in range(self.columns):
                    if self.card[r][c] == self.empty_char:
                        memo_card[r + 1][c + 1] = min(memo_card[r][c], memo_card[r + 1][c], memo_card[r][c + 1]) + 1
                        if memo_card[r + 1][c + 1] > square_side:
                            square_side = memo_card[r + 1][c + 1]
                            square_x = r + 1 - square_side
                            square_y = c + 1 - square_side
            return {
                "side": square_side,
                "x": square_x,
                "y": square_y
            }
        return "map error\n"

    @staticmethod
    def draw_square(square: dict, card: list[list[str]], fill_char: str) -> list[list[str]]:
        start_x, start_y, side = square["x"], square["y"], square["side"]
        for i in range(start_x, start_x + side):
            for j in range(start_y, start_y + side):
                card[i][j] = fill_char
        return card

    def display_largest_square(self) -> str:
        """
        Affiche le plus grand carré sur le plateau.
        :return: plateau final.
        """

        largest_square = self.find_largest_square()
        if isinstance(largest_square, dict):
            lines = []
            draw = self.draw_square(largest_square, self.card, self.fill_char)
            for line in draw:
                lines.append("".join(line))
            return "\n".join(lines)
        else:
            return largest_square


if __name__ == "__main__":
    for filename in sys.argv[1:]:
        with open(filename) as f:
            chars = f.readline().strip()[-3:]
            map_ = Map(
                f.read(),
                chars
            )
        print(map_.display_largest_square())
