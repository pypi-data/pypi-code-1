# encoding: utf-8

"""TurboGears extension startup and shutdown interface."""

import logging
log = logging.getLogger("turbomail")

import turbogears

import turbomail
from turbomail.exceptions import *
from turbomail.pool import MailPool


__all__ = ['start_extension', 'shutdown_extension']


def start_extension():
	"""TurboGears extension startup.
	
	Exits immediately if TurboMail is not enabled and creates a MailPool
	instance if all is well.
	"""
	
	if not turbogears.config.get("mail.on", False):
		return
	
	if turbogears.config.get("mail.server", None) is None:
		raise MailConfigurationException("Outbound server must be specified.")
	
	log.info("Outbound mail queue manager starting.")
	
	turbomail.queue = MailPool(
			interval=turbogears.config.get("mail.interval", 10),
			threads=turbogears.config.get("mail.threads", 4),
			jobs=turbogears.config.get("mail.jobs", 10),
			timeout=turbogears.config.get("mail.timeout", 60),
			server=turbogears.config.get("mail.server"),
			username=turbogears.config.get("mail.username", None),
			password=turbogears.config.get("mail.password", None),
			debug=turbogears.config.get("mail.debug", False)
		)
	turbomail.queue.start()
	turbomail.enqueue = turbomail.queue.enqueue


def shutdown_extension():
	"""TurboGears extension shutdown.
	
	Exits immediately if TurboMail is not enabled and shuts down the
	MailPool object safely.
	"""
	
	if not turbogears.config.get("mail.on", False):
		return

	log.info("Outbound mail queue manager shutting down.")
	
	turbomail.enqueue = None
	turbomail.queue.shutdown()
	turbomail.queue = None
