import json, sys

sec_file = sys.argv[1]
out_file = sys.argv[2]

with open(sec_file, 'r', encoding='utf-8') as f:
    items = json.load(f)

with open(out_file, 'w', encoding='utf-8') as out:
    for item in items:
        idx = item['index']
        if item['type'] == 'paragraph':
            out.write(f"[{idx}] ({item['style']}): {item['text']}\n")
        elif item['type'] == 'table':
            out.write(f"[{idx}] TABLE: {len(item['rows'])} rows x {len(item['rows'][0])} cols\n")
            for r in item['rows']:
                out.write('  | ' + ' | '.join(c.replace('\n', ' ') for c in r) + ' |\n')
print(f"Dumped {sec_file} to {out_file}")
