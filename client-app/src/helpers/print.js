export function exportLog() {
  const mywindow = window.open('', 'PRINT', 'height=400,width=600');
  mywindow.document.write(`<html><head><title>${document.title}</title>`);
  mywindow.document.write('</head><body >');
  mywindow.document.write(`<h1>${document.title.toUpperCase()} - Résultat de la simulation</h1>`);
  mywindow.document.write(document.getElementById('content').innerHTML);
  mywindow.document.write('</body></html>');

  mywindow.document.close();
  mywindow.focus();

  mywindow.print();
  mywindow.close();

  return true;
}
