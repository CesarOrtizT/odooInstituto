Para descartar cambios locales:
git checkout -- instituto/models/nombre-de-la-clase.py

Crear rama y colocarse en ella:
git checkout -b nombre-de-la-rama
git switch -c nombre-de-la-rama

Cambiar de rama:
git switch nombre-de-la-rama

Para eliminar una rama:
git push origin --delete nombre-de-la-rama

Subir la rama al GitHub:
git push -u origin rama1

Eliminar la rama github:
git push origin --delete nombre-de-la-rama

Eliminar rama local:
git branch -d nombre-de-la-rama
