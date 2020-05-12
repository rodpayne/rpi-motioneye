**motionEye** is a web-based frontend for `motion <https://motion-project.github.io>`_. Check out the `wiki <https://github.com/ccrisan/motioneye/wiki>`_ for more details.


.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/ccrisan/motioneye
   :target: https://gitter.im/ccrisan/motioneye?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

You can support the development of motionEye by making a small donation.

.. image:: https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif
   :alt: [paypal]
   :target: https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=ccrisan%40gmail%2ecom&lc=US&item_name=motionEye&no_note=0&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_LG%2egif%3aNonHostedGuest

Building Docker Container for Raspberry Pi
==========================================

- ``mkdir ~/git-repos``
- ``cd ~/git-repos``
- ``git clone -b dev https://github.com/rodpayne/rpi-motioneye.git``
	
- ``cd ~/git-repos/rpi-motioneye``
- ``docker build --build-arg VCS_REF=$(git rev-parse HEAD) --build-arg BUILD_DATE=$(date +"%Y-%m-%dT%H:%M:%SZ") -t rodpayne/rpi-motioneye:dev-armhf -f extra/Dockerfile.armv7-armhf .``
	
- ``cd ~/git-repos/rpi-motioneye/extra``
- ``docker-compose up``
