import logging
from typing import override, Dict
import json
import datetime

class JSONFormatter(logging.Formatter):
    def __init__(self, *, fmt_keys: Dict[str, str] | None = None):
        super().__init__()
        self.fmt_keys = fmt_keys if fmt_keys is not None else {}

    @override
    def format(self, record: logging.LogRecord) -> Dict:
        message = self._prepare_log_dict(record)
        return json.dumps(message, default=str)
    
    def _prepare_log_dict(self, record: logging.LogRecord) -> None:
        always_fields: Dict = {
            "message": record.getMessage(),
            "timestamp": datetime.datetime.fromtimestamp(
                record.created, tz=datetime.timezone.utc
            ).isoformat()
        }

        if record.exc_info is not None:
            always_fields["exc_info"] = self.formatException(record.exc_info)
        
        if record.stack_info is not None:
            always_fields["stack_info"] = self.formatStack(record.stack_info)

        message = {
            key: msg_val 
            if (msg_val := always_fields.pop(val, None)) is not None
            else getattr(record, val)
            for key, val in self.fmt_keys.items()
        }

        message.update(always_fields)

        return message
    

class UnnecessaryFilter(logging.Filter):
    @override 
    def filter(self, record: logging.LogRecord) -> bool | logging.LogRecord:
        return record.levelno <= logging.INFO