from log_processor import LogProcessor

class InfoLogProcessor(LogProcessor):
    
    def __init__(self, next_log_processor: LogProcessor):
        super().__init__(next_log_processor)

    def log(self, log_level, message):
        print(f"Log level : {log_level}")
        if log_level == self.INFO:
            print(f"INFO : {message}")
        else:
            super().log(log_level, message)

    
