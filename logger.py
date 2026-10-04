"""
logger.py - Audit & Logging Module
Provides decorator and higher-order functions for logging transactions.
"""

from functools import wraps
from datetime import datetime

# In-memory storage for execution logs
LOG_HISTORY = []

def log_transaction(action_name):
    """
    Decorator factory that wraps functions to log execution time and status.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                log_entry = {
                    "timestamp": timestamp,
                    "action": action_name,
                    "status": "SUCCESS",
                    "details": f"Function '{func.__name__}' executed successfully."
                }
                LOG_HISTORY.append(log_entry)
                return result
            except Exception as e:
                log_entry = {
                    "timestamp": timestamp,
                    "action": action_name,
                    "status": "FAILED",
                    "details": str(e)
                }
                LOG_HISTORY.append(log_entry)
                raise e
        return wrapper
    return decorator

def summarize_logs(logs, filter_func=None):
    """
    Higher-order function: Processes log records using an optional filter function.
    """
    target_logs = filter(filter_func, logs) if filter_func else logs
    return list(target_logs)