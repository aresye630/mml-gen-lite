import logging

class GrpcFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        if record.name == "grpc._server" and "Method not implemented!" in record.getMessage():
            return False
        return True

def get_logger(name: str):
    logging.basicConfig(level=logging.ERROR)
    logger = logging.getLogger(name)
    logger.addFilter(GrpcFilter())
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)
    return logger
