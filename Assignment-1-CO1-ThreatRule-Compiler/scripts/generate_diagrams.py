"""Generate original, lightweight SVG diagrams used in the submission."""
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "Diagrams"
root.mkdir(exist_ok=True)

def svg(name, title, labels):
    boxes = []
    for index, label in enumerate(labels):
        x = 30 + index * (720 / max(1, len(labels) - 1))
        boxes.append(f'<rect x="{x - 55:.0f}" y="150" width="110" height="52" rx="7" fill="#e8f1fb" stroke="#1769aa"/>')
        boxes.append(f'<text x="{x:.0f}" y="181" text-anchor="middle">{label}</text>')
        if index:
            previous = 30 + (index - 1) * (720 / max(1, len(labels) - 1))
            boxes.append(f'<line x1="{previous + 55:.0f}" y1="176" x2="{x - 55:.0f}" y2="176" stroke="#333" marker-end="url(#arrow)"/>')
    text = f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="260" viewBox="0 0 800 260">
<defs><marker id="arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto"><polygon points="0 0, 10 3.5, 0 7"/></marker></defs>
<style>text{{font:14px Arial;fill:#16212d}} .title{{font-size:20px;font-weight:bold}}</style>
<text class="title" x="400" y="45" text-anchor="middle">{title}</text>{''.join(boxes)}</svg>'''
    (root / name).write_text(text, encoding="utf-8")

svg("language_processing_system.svg", "Language Processing System", ["Source", "Scanner", "Parser", "Rule engine"])
svg("compiler_phases.svg", "Compiler Phases", ["Lexer", "Parser", "Semantic", "IR", "Target"])
svg("frontend_backend.svg", "Front End and Back End", ["Front end", "IR", "Back end"])
svg("scanner_parser_interaction.svg", "Scanner and Parser Interaction", ["Characters", "Tokens", "Parser"])
svg("buffer_pair_and_sentinel.svg", "Input Buffering Concept", ["Buffer A", "Sentinel", "Buffer B"])
svg("token_transition_diagrams.svg", "Identifier Recognition", ["Start", "Letter", "Identifier", "Accept"])
svg("testing_workflow.svg", "Testing Workflow", ["Input", "Scanner", "Logs", "Review"])
svg("threatrule_architecture.svg", "ThreatRule Architecture", ["Branch SOC", "Validation", "Central SOC"])
svg("design_challenge_comparison.svg", "Live Feed Extension", ["Legacy tokens", "New token rules", "Validated feed"])
print("Generated SVG diagrams")
