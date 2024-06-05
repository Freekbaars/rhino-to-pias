dit programma gebruikt de input van grasshopper om een cordinaten excel temaken om de cordinaten makelijk in pias tezetten

## uitleg
 het programma is ontworpen om schepen van rhino in pias te zetten. hier voor moet het rhino bestand wel voldoen aan een paar regels
 - het schip is getekend Z up en X+ boeg
 - het schip in gespiegeld om de XZ plane
 - het model bestaat uit vlakken die opelkaar aansluiten (1 brep/closet poly surface)


## gebruik
1. open het rhino bestand
2. open grasshopper
3. laad het script in
    - volg de stappen in het script
4. laad de csv in in het python script
    - pas de naam van de csv aan in het script
```python
CSV_betandsnaam = 'pias export.csv'
```

5. pas de unit aan 
    - van m naar m = 1
    - van mm naar m = 1000
```python
omrekenFactor = 1000
```
6. run het script
7. de spanten zullen nu per spand in een blad te staan je kan deze nu kopieren en plakken in pias
