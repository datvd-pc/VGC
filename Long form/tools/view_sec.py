import json, sys

def view_section(sec_file):
    with open(sec_file, 'r', encoding='utf-8') as f:
        items = json.load(f)
    for item in items:
        idx = item['index']
        if item['type'] == 'paragraph':
            print(f"[{idx}] ({item['style']}): {item['text']}")
        elif item['type'] == 'table':
            print(f"[{idx}] TABLE: {len(item['rows'])} rows x {len(item['rows'][0])} cols")
            for r in item['rows']:
                print('  | ' + ' | '.join(c.replace('\n', ' ') for c in r) + ' |')

if __name__ == '__main__':
    view_section(sys.argv[1])
