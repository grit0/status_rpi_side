kill $(ps -aux | grep /status_app/__init__.py | awk '{print $2}')
