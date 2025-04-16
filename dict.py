import re;

abbrev = {
    "ab.": "abbas",
    "arch.": "archidiaconus",
    "archipresb.": "archipresbiter",
    "ass.": "assessor",
    "bur.": "burgum",
    "ca.": "castrum",
    "can.": "canonicus",
    "capl.": "capellanus",
    "card.": "cardinalis",
    "cast.": "castellanus",
    "ci.": "civis",
    "civ.": "civitas",
    "cler.": "clericus",
    "co.": "comune, comunis, comunitas, ete",
    "cogn.": "cognatus",
    "com.": "comes, comitis, comites",
    "conv.": "conventus",
    "coss.": "consules",
    "diac.": "diaconus",
    "dioc.": "diocesis",
    "dom.": "dominus, domina, domini",
    "e.": "ecclesia, ecclesie, etc",
    "ep.": "episcopus, episcopi, etc",
    "f.": "filius, filia, filii, ete",
    "fl.": "flumen, fluvius",
    "fr.": "frater, fratres, ete",
    "gen.": "gener",
    "guard.": "guardator",
    "her.": "heres, heredes",
    "ibid": "ibidem",
    "iud.": "iudex, iudicis, iudices, etc",
    "iug.": "iugalis, iugales",
    "1.": "locus, loci",
    "le.": "legatus, legati",
    "mag.": "magister, magistri, etc",
    "mar.": "marchio, marchiones",
    "mat.": "mater",
    "mo.": "monacus, monaci",
    "mon.": "monasterium, monasterii, etc",
    "n.": "notarius, notarii",
    "nep.": "nepos, neptis, nepotis, nepotes, ete",
    "no.": "nobilis, nobiles",
    "nu.": "nurus",
    "pat.": "pater, patris, eic",
    "po.": "potestas, potestates",
    "prep.": "prepositus",
    "presb.": "presbiter",
    "proc.": "procurator",
    "q.": "quondam",
    "Rom.": "romanus, romana, ete",
    "S.": "Sancta, Sanctus, Sancti, ete",
    "Sac.": "sacerdos, sacerdotes",
    "serv.": "serviens",
    "si.": "sindicus, sindici",
    "so.": "socius",
    "soc.": "socrus",
    "sor.": "soror, sorores",
    "sp.": "sponsus, sponsa",
    "subd.": "subdiaconus",
    "t.": "testis, testes",
    "terr.": "territorium, territorii, etc",
    "ux.": "uxor, uxoris",
    "vi.": "vicus",
    "vil.": "villa, villae, ete"
}

pattern = re.compile(r'(?<!\w)(' + '|'.join(re.escape(k) for k in abbrev.keys()) + r')(?!\w)')

def replace_abbreviations(text):
    return pattern.sub(lambda match: abbrev[match.group(0)], text)

Test1 = "Petraca bisancios .cvar. marabutinos et in domo eius habeo lb. .m. $ quas uxori prestavi." # vi. in the end shouldn't be replaced
Test2 = "Hi, I'm Andrew Lin from Emory vi. and i love skateboarding."
Test3 = "d fsdf iweuhfdu .xxxxwvi. dfweifjwi."

# print(replace_abbreviations(Test1)) 
# print(replace_abbreviations(Test2))
# print(replace_abbreviations(Test3))