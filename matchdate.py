import re

# Key: Italian -> Month: Latin month
month_trans_dict = {
    "gennaio": "Ianuarii",
    "febbraio": "Februarii",
    "marzo": "Martii",
    "aprile": "Aprilis",
    "maggio": "Maii",
    "giugno": "Iunii",
    "luglio": "Iulii",
    "agosto": "Augusti",
    "settembre": "Septembris",
    "ottobre": "Octobris",
    "novembre": "Novembris",
    "dicembre": "Decembris"
}

# Pattern to match Italian-style dates (5 marzo 1161)
pattern = re.compile(
    r"\(\s*(\d{1,2})\s+(" + "|".join(month_trans_dict.keys()) + r")\s+(\d{4})\s*\)",
    flags=re.IGNORECASE
)
def extract_latin_date(paragraph):
    match = pattern.search(paragraph)
    if match:
        day, month_it, year = match.groups() # tuple (day, month, year)
        latin_month = month_trans_dict[month_it.lower()]
        return f"(die {day} mensis {latin_month} anno {year})"
    return ""

# Example
# text = "Ansaldo Abaialardi si rende garante verso Oberto di Buon Tommaso di quanto questi aveva pagato al proprio padre (2 marzo 1161)."
# converted_text = extract_latin_date(text)

# print(converted_text)
