#!/usr/bin/env python3
"""
Antigravity Agent - Entry Point
Launch the TUI or run a single command from the CLI.

Usage:
    python main.py              # Launch the TUI
    python main.py --build "a portfolio website"   # One-shot mode
    python main.py --index      # Re-index the knowledge base
"""

import argparse
import sys
import os

# Fix Windows console encoding for Unicode
if sys.platform == "win32":
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from antigravity.config import Config


def main():
    parser = argparse.ArgumentParser(
        description="Antigravity Agent - Build anything with AI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--build", "-b",
        type=str,
        help="Run a single build command without the TUI",
    )
    parser.add_argument(
        "--index", "-i",
        action="store_true",
        help="Re-index the knowledge base and exit",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate configuration and exit",
    )

    args = parser.parse_args()

    # Ensure directories exist
    Config.ensure_dirs()

    # -- Check mode --
    if args.check:
        print("[*] Antigravity Agent - Configuration Check")
        print(f"   Model:     {Config.OLLAMA_MODEL}")
        print(f"   Ollama:    {Config.OLLAMA_BASE_URL}")
        print(f"   Workspace: {Config.WORKSPACE_DIR}")
        print(f"   Knowledge: {Config.KNOWLEDGE_DIR}")
        print(f"   ChromaDB:  {Config.CHROMA_DB_DIR}")
        warnings = Config.validate()
        if warnings:
            print("\n[!] Warnings:")
            for w in warnings:
                print(f"   - {w}")
        else:
            print("\n[OK] All checks passed!")
        return

    # -- Index mode --
    if args.index:
        from antigravity.knowledge_base import KnowledgeBase
        kb = KnowledgeBase()
        count = kb.index_knowledge_files()
        print(f"[OK] Indexed {count} knowledge chunks.")
        return

    # -- One-shot build mode --
    if args.build:
        from antigravity.crew import run_crew
        print(f"[*] Building: {args.build}")
        print("=" * 60)
        result = run_crew(args.build)
        print("\n" + "=" * 60)
        print("Result:")
        print(result)
        return

    # -- TUI mode (default) --
    from antigravity.tui import AntigravityApp
    app = AntigravityApp()
    app.run()


if __name__ == "__main__":
    main()
