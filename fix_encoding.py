import re


def fix_encoding(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    fixes = {
        'Ã¡': 'á', 'Ã ': 'à', 'Ã¢': 'â', 'Ã£': 'ã',
        'Ã©': 'é', 'Ãª': 'ê', 'Ã­': 'í',
        'Ã³': 'ó', 'Ã´': 'ô', 'Ãµ': 'õ',
        'Ãº': 'ú', 'Ã§': 'ç',
        'Ã': 'Á', 'Ã': 'É', 'Ã': 'Í',
        'Ã': 'Ó', 'Ã': 'Ú', 'Ã': 'Ç',
        'â€¢': '•', 'â€œ': '"', 'â€': '"',
        'â€™': "'", 'â€"': '—', 'â€“': '–',
        'ðŸ': '🔒', 'âš ': '⚠️', 'ðŸŽ¯': '🎯',
        'ðŸ›¡': '🛡️', 'âš"': '⚔️'
    }

    for old, new in fixes.items():
        content = content.replace(old, new)

    return content


if __name__ == '__main__':
    fixed_content = fix_encoding('Instructions.html')
    with open('Instructions_FIXED.html', 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    print('Encoding corrections applied: Instructions_FIXED.html generated.')
