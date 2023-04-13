# env_color_logger

A simple logger that prints colored messages to the console and uses environment variables to control the basic setup.

See [example.env](example.env) for a list of environment variables that can be used to control the logger.

## Usage

The usage in Python is very basic. Just import the logger and use it as you would use the standard `logging` module. The logger will automatically use the environment variables to configure itself. This is done to aid in development of apps that are run in isolated environments, such as Docker containers.

```python
from env_color_logger import EnvLogger

logger = EnvLogger(__name__)
logger.info("Hello World!")
```
