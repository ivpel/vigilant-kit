"""
Internal helpers for Selenium 4 BiDi/CDP-style event access.

Selenium's Python API has evolved across 4.x and, depending on browser/driver,
the `bidi_connection()` helper may be backed by a direct DevTools (CDP) socket.
This package keeps Vigilant's public API stable by feature-detecting support and
gracefully skipping when unavailable (common on cloud/grid providers).
"""

