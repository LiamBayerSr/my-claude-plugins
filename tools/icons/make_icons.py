#!/usr/bin/env python3
"""Draw the plugin icons as SVG and render 1024x1024 PNGs with rsvg-convert.

Usage (from the repo root):  python3 tools/icons/make_icons.py
Teacher icons go to tools/ca-teacher/icons/ (copied into each plugin by
tools/ca-teacher/build.py); the tax icon goes straight into its plugin.

Note: the plugin directory keeps the first icon it sees for a listing, so
settle on a design before submitting a plugin.
"""
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
OUT_SVG = REPO / "tools" / "icons" / "svg"
TEACHER_ICONS = REPO / "tools" / "ca-teacher" / "icons"

GRADES = {
    # code: (label, background, darker shade)
    "K": ("K", "#D64545", "#A83232"),
    "1": ("1", "#DE7318", "#B05A10"),
    "2": ("2", "#2E9E5B", "#227A45"),
    "3": ("3", "#2B7BB9", "#1F5E8F"),
    "4": ("4", "#6A4FB3", "#523C8C"),
    "5": ("5", "#C2407A", "#97305E"),
}

APPLE = """
  <g transform="translate(790 250)">
    <path d="M0,-38 C-32,-74 -98,-58 -98,4 C-98,64 -52,110 -20,104 C-8,102 -5,95 0,95 C5,95 8,102 20,104 C52,110 98,64 98,4 C98,-58 32,-74 0,-38 Z" fill="#FFFFFF"/>
    <path d="M0,-38 C2,-60 8,-76 20,-92" stroke="#FFFFFF" stroke-width="14" stroke-linecap="round" fill="none"/>
    <path d="M14,-70 C34,-104 76,-104 88,-86 C66,-60 34,-58 14,-70 Z" fill="#FFFFFF"/>
  </g>"""


def teacher_svg(label: str, bg: str, dark: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
  <rect width="1024" height="1024" rx="224" fill="{bg}"/>
  <circle cx="440" cy="520" r="330" fill="{dark}" opacity="0.35"/>
  <text x="440" y="700" text-anchor="middle" font-family="Inter Display" font-weight="900" font-size="600" fill="#FFFFFF">{label}</text>
  {APPLE}
  <g transform="translate(0 0)">
    <rect x="200" y="800" width="72" height="76" rx="18" fill="#F6C1C1"/>
    <rect x="262" y="800" width="30" height="76" fill="#D9D9D9"/>
    <rect x="292" y="800" width="420" height="76" fill="#FFFFFF"/>
    <rect x="292" y="800" width="420" height="25" fill="#000000" opacity="0.06"/>
    <polygon points="712,800 812,838 712,876" fill="#F3D7A6"/>
    <polygon points="782,827 812,838 782,849" fill="#2B2B2B"/>
  </g>
</svg>
"""


TAX_SVG = """<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024">
  <rect width="1024" height="1024" rx="224" fill="#1E5F4A"/>
  <circle cx="512" cy="512" r="360" fill="#164A39" opacity="0.6"/>
  <path d="M290 190 H620 L740 310 V820 Q740 850 710 850 H320 Q290 850 290 820 Z" fill="#FFFFFF"/>
  <path d="M620 190 V280 Q620 310 650 310 H740 Z" fill="#D6E4DE"/>
  <rect x="350" y="300" width="200" height="34" rx="17" fill="#1E5F4A" opacity="0.85"/>
  <rect x="350" y="390" width="320" height="22" rx="11" fill="#9DB8AD"/>
  <rect x="350" y="450" width="320" height="22" rx="11" fill="#9DB8AD"/>
  <rect x="350" y="510" width="240" height="22" rx="11" fill="#9DB8AD"/>
  <rect x="350" y="570" width="160" height="22" rx="11" fill="#9DB8AD"/>
  <circle cx="700" cy="740" r="160" fill="#F2C14E"/>
  <circle cx="700" cy="740" r="160" fill="none" stroke="#1E5F4A" stroke-width="16"/>
  <path d="M626 742 L680 796 L780 690" stroke="#1E5F4A" stroke-width="40" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
</svg>
"""


def render(svg: str, svg_path: Path, png_path: Path) -> None:
    svg_path.parent.mkdir(parents=True, exist_ok=True)
    png_path.parent.mkdir(parents=True, exist_ok=True)
    svg_path.write_text(svg)
    subprocess.run(["rsvg-convert", "-w", "1024", "-h", "1024", str(svg_path), "-o", str(png_path)], check=True)
    print(f"wrote {png_path.relative_to(REPO)}")


if __name__ == "__main__":
    for code, (label, bg, dark) in GRADES.items():
        render(teacher_svg(label, bg, dark), OUT_SVG / f"teacher-{code}.svg", TEACHER_ICONS / f"{code}.png")
    render(TAX_SVG, OUT_SVG / "tax-preparer.svg", REPO / "plugins" / "tax-preparer" / ".claude-plugin" / "icon.png")
