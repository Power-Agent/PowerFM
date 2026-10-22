# Machine-readable PowerFM project catalog

\`projects.json\` is a structured companion to the project links currently described in the repository README. It records each resource's stable ID, category, short description, project URL, supported task areas, modalities, and one or more resource links.

The catalog intentionally records only the project descriptions and links represented in the README. It does not claim that external URLs are currently reachable or that a listed model has been independently benchmarked.

Validate the file from the repository root:

\`\`\`bash
python scripts/validate_project_catalog.py
python -m unittest discover -s tests -v
\`\`\`

To validate a different catalog file:

\`\`\`bash
python scripts/validate_project_catalog.py path/to/projects.json
\`\`\`

The validator uses Python's standard library and checks required fields, unique project IDs, non-empty task/modality labels, resource records, and absolute HTTPS URLs. It does not make network requests.
