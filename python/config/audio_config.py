from dataclasses import dataclass

@dataclass
class AudioConfig:
    SAMPLE_RATE: int = 16000
    CHANNELS: int = 1
    FORMAT: str = "wav"
    MIN_DBFS: int = -20
    MAX_CHUNK_SIZE_MS: int = 15000
    OVERLAP_PERCENT: float = 0.2