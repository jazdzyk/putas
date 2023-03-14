import json
from typing import List, Tuple, Dict, Type, TypeVar

KT = TypeVar("KT", str, int, float)
VT = TypeVar("VT", str, int, float)


def to_dict(s: str, key_type: Type[KT] = str, val_type: Type[VT] = str) -> Dict[KT, VT]:
    return {key_type(k): val_type(v) for k, v in json.loads(s).items()}


def to_list(s: str, delimiter=",") -> List[str]:
    return s.split(delimiter)


def to_int_list(s: str, delimiter=",") -> List[int]:
    return [int(n) for n in to_list(s, delimiter)]


def to_float_list(s: str, delimiter=",") -> List[float]:
    return [float(f) for f in to_list(s, delimiter)]


def to_tuple(s: str, delimiter=",") -> Tuple[str, ...]:
    return tuple(to_list(s, delimiter))


def to_int_tuple(s: str, delimiter=",") -> Tuple[int, ...]:
    return tuple(int(n) for n in to_list(s, delimiter))


def to_float_tuple(s: str, delimiter=",") -> Tuple[float, ...]:
    return tuple(float(f) for f in to_list(s, delimiter))


def to_bool(s: str) -> bool:
    return s.lower() in ["true", "t", "1", "yes", "y"]
