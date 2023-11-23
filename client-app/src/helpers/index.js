export function obtenirNomImage(objet) {
  switch (objet.name) {
    case 'Cookie':
      return 'cookie.png';
    case 'Petit piège':
      return 'petit_piege.png';

    case 'Potion Magique':
      return 'potion_magique.png';

    case 'Monstre':
      return 'monstre.png';

    case 'Piège mortel':
      return 'piege_mortel.png';

    case 'Alcool':
      return 'alcool.png';

    default:
      return 'inconnu.png';
  }
}
