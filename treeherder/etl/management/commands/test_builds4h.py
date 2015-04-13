# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, you can obtain one at http://mozilla.org/MPL/2.0/.

from django.core.management.base import BaseCommand
from treeherder.etl import buildapi


class Command(BaseCommand):

    """Management command to run the builds-4hr analyser."""

    help = (
        "Tests the buildernames and data structures in the builds4h.js"
        "generated by buildbot"
    )

    def handle(self, *args, **options):

        ba = buildapi.Builds4hAnalyzer()
        ba.run()
