#!/usr/bin/env bash
set -euo pipefail
batch=${1:?batch identifier required}
root=$(cd "$(dirname "$0")/../.." && pwd)
record="/workspace/volume1-checkpoints/$batch"
mkdir -p "$record"
cd "$root"
tar -czf "$record/source-before-build.tar.gz" tome1-integers review/volume1-reconstruction
source /workspace/order-chance-system/activate.sh
./build.sh --pdf-only tome1-integers > "$record/build.log" 2>&1
cp "dist/Volume 1 - The Integers.pdf" "$record/Volume1.pdf"
cp "dist/kdp/Volume 1 - The Integers - Print.pdf" "$record/Volume1-interior.pdf"
cp build/tome1-integers/main.{aux,toc,log} "$record/"
python3 review/volume1-reconstruction/inventory.py > "$record/structure.json"
git diff --check
printf 'Cumulative manuscript and logs: %s\n' "$record"
