# app/access.py
import pathlib, yaml, time

class AccessControl:
    """Loads whitelist from YAML; watches file for live edits."""
    def __init__(self, cfg='config/whitelist.yaml'):
        self.path = pathlib.Path(cfg)
        self.mtime = 0
        self.authorized = set()
        self.reload()

    def reload(self):
        """Reload whitelist if the file was modified."""
        if not self.path.exists():
            return
        stat = self.path.stat().st_mtime
        if stat > self.mtime:
            self.mtime = stat
            data = yaml.safe_load(self.path.read_text()) or {}
            self.authorized = {p.upper() for p in data.get('plates', [])}
            print(f'🔄  Whitelist loaded: {len(self.authorized)} plates')

    def allowed(self, plate: str) -> bool:
        self.reload()
        return plate.upper() in self.authorized

