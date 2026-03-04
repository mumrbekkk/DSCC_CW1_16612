import multiprocessing

# Bind to all interfaces
bind = "0.0.0.0:8000"

# Worker configuration
# Rule of thumb: (2 x CPU cores) + 1
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
worker_tmp_dir = "/dev/shm"

# Timeouts
timeout = 30
graceful_timeout = 30

# Restart workers periodically (prevent memory leaks)
max_requests = 1000
max_requests_jitter = 50

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Security
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# Process name
proc_name = "django_app"

# Faster worker startup
preload_app = True