from logging import getLogger
import sys

from auxtest.util.logging import configure_logger


configure_logger()
log = getLogger(__name__)


def run_dev():
    from auxtest.entrypoint import api
    api.app.run(host='0.0.0.0', debug=True)


if __name__ == '__main__':
    # use a proper arg-parser as soon as it's worth it
    cli_options = ['dev']
    if len(sys.argv) < 2 or sys.argv[1] not in cli_options:
        log.error(f"Invalid module parameters, try one of {cli_options}.")
        exit(1)
    if sys.argv[1] == 'dev':  # start in debug mode
        log.info("Starting entrypoint")
        run_dev()
