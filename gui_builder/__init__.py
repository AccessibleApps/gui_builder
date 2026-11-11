import sys

if sys.version_info >= (3, 11):
    from enum import StrEnum
else:
    from enum import Enum

    # Defined here rather than taken from backports.strenum: py2exe does not
    # package the "backports" namespace package, so frozen apps on older
    # Pythons died at startup with "No module named 'backports.strenum'".
    class StrEnum(str, Enum):
        def __str__(self):
            return str.__str__(self)


class DialogResult(StrEnum):
    OK = "ok"
    APPLY = "apply"
    CANCEL = "cancel"
    YES = "yes"
    NO = "no"
    CLOSE = "close"
    FIND = "find"
    VETO = "veto"


# Maintain backward compatibility
OK = DialogResult.OK
APPLY = DialogResult.APPLY
CANCEL = DialogResult.CANCEL
YES = DialogResult.YES
NO = DialogResult.NO
CLOSE = DialogResult.CLOSE
FIND = DialogResult.FIND
VETO = DialogResult.VETO
