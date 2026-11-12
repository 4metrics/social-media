#!/usr/bin/env bash
# Prepara o ambiente da rotina de conteúdo da 4metrics a partir do kit deste repositório.
set -e
K="$(cd "$(dirname "$0")" && pwd)"
mkdir -p /home/claude/fonts/package/dist/fonts/geist-sans /home/claude/assets /home/claude/out
rm -rf /home/claude/tools /home/claude/fonts/fs /home/claude/assets/plataforma /home/claude/logos
cp -r "$K/tools" /home/claude/tools
cp -r "$K/fonts/fs" /home/claude/fonts/fs
cp "$K/fonts/geist/Geist-SemiBold.ttf" /home/claude/fonts/package/dist/fonts/geist-sans/
cp -r "$K/assets/plataforma" /home/claude/assets/plataforma
cp -r "$K/logos" /home/claude/logos
python3 -c "import playwright, PIL, fontTools" 2>/dev/null || pip install --break-system-packages -q playwright pillow fonttools
echo "kit pronto"
