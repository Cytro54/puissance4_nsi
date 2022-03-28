# Comment de servir de `git`

Git est utilisé comme logiciel de controle de version

## Se mettre a jour, (se syncroniser avec le depot)
Pour mettre a jour le dossier local et obtenir les derniéres modifications faites par les autres; il faut faire `git pull`

```bash
# Telecharger les modifications fait par les autres collaborateurs
$ git pull
```


## Modifier le projet , (faire un commit)
Git fonctionne par un systéme de "commit", un commit est une modification apportée par un contributeur au projet.

Pour faire un commit , rien est plus simple:

1. Effectuez vos modifications sur le code
2. Ouvrez la ligne de commande
3. ```bash
   # Valider les modifications actuelles avec pour message de commit "Modification du module console"
   $ git commit -a -m "Modification du module console"

   # Sauvegarder les modifications sur le serveur
   $ git push
   ```
4. _Il se peut qu'une erreur arrive lors du `git push`_, si une erreur du type arrive:
    ```bash
        $ git push
        To https://github.com/Cytro54/puissance4_nsi.git
        ! [rejected]        main -> main (fetch first)
        error: impossible de pousser des références vers 'https://github.com/Cytro54/puissance4_nsi.git'
        astuce: Les mises à jour ont été rejetées car la branche distante contient du travail que
        astuce: vous n'avez pas en local. Ceci est généralement causé par un autre dépôt poussé
        astuce: vers la même référence. Vous pourriez intégrer d'abord les changements distants
        astuce: (par exemple 'git pull ...') avant de pousser à nouveau.
        astuce: Voir la 'Note à propos des avances rapides' dans 'git push --help' pour plus d'information.
    ```
    En fait, git vous previent d'une erreur commune : Vous tentez d'envoyer des modifications alors que vous n'etes pas a jour. Vous devez avant faire un `git pull` avant de continuer