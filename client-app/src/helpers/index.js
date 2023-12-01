export function getObjectiveName(name) {
  switch (name) {
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
export function getObjectiveId(id) {
  switch (id) {
    case 1:
      return 'cookie.png';
    case 2:
      return 'petit_piege.png';
    case 3:
      return 'potion_magique.png';
    case 4:
      return 'monstre.png';
    case 5:
      return 'piege_mortel.png';
    case 6:
      return 'alcool.png';
    default:
      return 'inconnu.png';
  }
}
