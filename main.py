import pandas as pd
from openpyxl import Workbook
from io import StringIO

def opschonen_regel(regel):
    """Verwijder accolades van de regel en strip spaties."""
    return regel.replace('{', '').replace('}', '').strip()

def opslaan_in_excel(csv_bestandsnaam, excel_bestandsnaam="CoordinatenSpanten.xlsx"):
    with open(csv_bestandsnaam, 'r') as bestand:
        schone_regels = [opschonen_regel(regel) for regel in bestand]

    # Converteer de schone regels naar een StringIO object en laad in pandas DataFrame
    schone_data = StringIO('\n'.join(schone_regels))
    df = pd.read_csv(schone_data, header=None, names=['SpantNummer', 'X', 'Y'])
    # ".0" van SpantNummer verwijderen en omzetten naar int
    df['SpantNummer'] = df['SpantNummer'].apply(lambda x: int(float(x)))
    
    # Een nieuw Excel-bestand aanmaken en default sheet verwijderen
    wb = Workbook()
    wb.remove(wb.active)

    # Unieke spantnummers verwerken en data per spantnummer in tabbladen zetten
    unique_spant_numbers = df['SpantNummer'].unique()
    for spant in unique_spant_numbers:
        ws = wb.create_sheet(title=str(spant))
        ws.append(['X', 'Y'])
        for _, row in df[df['SpantNummer'] == spant].iterrows():
            ws.append([row['X'], row['Y']])
    
    # Opslaan van het Excel-bestand
    wb.save(excel_bestandsnaam)
    print(f"Data opgeslagen in {excel_bestandsnaam}.")


def main():
    opslaan_in_excel('pias export.csv')

if __name__ == "__main__":
    main()