from pathlib import Path

input_file = (
    "babyslm_models/stela_audiobooks_1024h/quantized/lexical/dev/quantized_outputs.txt"
)
output_dir = Path("babyslm_models/stela_audiobooks_1024h/quantized/lexical/dev")

output_dir.mkdir(exist_ok=True)

count = 0
with open(input_file) as f:
    for line in f:
        parts = line.strip().split("\t")
        if len(parts) != 2:
            continue

        name, seq = parts

        # convert CPC format → token sequence
        # 12-3,45-1,22-9 → 12 3 45 1 22 9
        tokens = seq.replace(",", "-").split("-")

        with open(output_dir / f"{name}.txt", "w") as out:
            out.write(" ".join(tokens))

        count += 1

print("created", count, "files")
