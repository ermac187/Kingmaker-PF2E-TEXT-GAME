import json, shutil, sys
sys.stdout.reconfigure(encoding='utf-8')
f = 'C:/KMG/.saves/0_pregame.txt'
t = open(f, encoding='utf-8').read(); ob = len(t.encode('utf-8'))
shutil.copy(f, f + '.bak')

REPL = [
    # chronicler flavor (specific first)
    ('played with its bow', 'plucked by hand'),
    ('Unfinished Violin', 'Wayworn Harp'),
    ('Endless Violin', 'Endless Harp'),
    ('Violin', 'Harp'),
    ('violin', 'harp'),
    ('BOOK OF DIARY + SONG', 'BOOK OF DIARY + BALLAD'),
    ('a song she composed', 'a ballad she composed'),
    # chronicler flags/keys (longer before shorter prefix)
    ('kaori_chronicler_mode', 'storm_chronicler_mode'),
    ('kaori_score_archive', 'storm_ballad_cycle'),
    ('kaori_opus_named', 'storm_opus_named'),
    ('kaori_opus_performed', 'storm_opus_performed'),
    ('kaori_opus_name', 'storm_opus_name'),
    ('kaori_illness_disclosed', 'storm_illness_disclosed'),
    # seekers
    ('Morgan le Fay', 'Bellatrix Lestrange'),
    ('Cagliostro', 'Poison Ivy'),
    ('Jeanne Alter', 'Viconia DeVir'),
    ('Esdeath', 'Kitiara uth Matar'),
    ('Medusa', 'Callisto'),
    # party (underscore/multiword before generic)
    ('Kaori_Miyazono', 'Storm_Silverhand'),
    ('KAORI', 'STORM'),
    ('Kaori', 'Storm'),
    ('Erza_Scarlet', 'Saber'),
    ('Erza Scarlet', 'Saber'),
    ('Erza', 'Saber'),
    ('Atalanta', 'Ciri'),
    ('Kasumi', 'Yor_Forger'),
    ('Aqua', 'Goldmoon'),
]
n = 0
for old, new in REPL:
    c = t.count(old)
    if c: t = t.replace(old, new); n += c

# validate JSON before writing
try:
    json.loads(t)
except Exception as e:
    print('!! JSON INVALID after replace:', e); sys.exit(1)

open(f, 'w', encoding='utf-8', newline='').write(t)
print(f'0_pregame.txt: {ob} -> {len(t.encode("utf-8"))} bytes  ({n} replacements)  JSON OK')
for nm in ['Kaori','kaori_','Erza','Atalanta','Kasumi','Aqua','Morgan','Cagliostro','Esdeath','Jeanne','Medusa','Violin','violin']:
    c = t.count(nm)
    if c: print(f'  leftover {nm}: {c}')
