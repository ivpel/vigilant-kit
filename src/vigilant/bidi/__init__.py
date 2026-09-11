"""
Internal helpers for Selenium 4 BiDi/CDP-style event access.

Selenium's Python API has evolved across 4.x and, depending on browser/driver,
the `bidi_connection()` helper may be backed by a direct DevTools (CDP) socket.
Checks raise when unavailable unless the caller explicitly opts into a warning.
"""

from vigilant.bidi._bidi import BiDiUnavailableError

__all__ = ["BiDiUnavailableError"]
